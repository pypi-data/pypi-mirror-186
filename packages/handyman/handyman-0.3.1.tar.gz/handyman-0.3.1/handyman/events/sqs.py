import json
from typing import List, Tuple
from boto3 import resource, client as boto_client
from botocore.exceptions import ClientError
from uuid import uuid4

from handyman.log import get_logger
from handyman.events import AWS_REGION as DEFAULT_AWS_REGION, AWS_ACCESS_KEY_ID as DEFAULT_AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY as DEFAULT_AWS_SECRET_ACCESS_KEY
from handyman.events.exceptions import SQSErrorCodes, SQSException
from handyman.events.event_types import Events, Service, Vendor
from handyman.helpers import retry_with_backoff, return_exception_as_parameter


AWS_REGION = DEFAULT_AWS_REGION
AWS_ACCESS_KEY_ID = DEFAULT_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = DEFAULT_AWS_SECRET_ACCESS_KEY
SQS = None
SQS_CLIENT = None
SQS_CLIENT_CACHE = {}
SQS_QUEUE_BATCH_LENGTH = 10 # This should be less than or equal to 10 always
LOGGER = get_logger("events")
WAREHOUSE_QUEUE_NAME = "warehouse-data-transfer"


def _init_sqs_client(region_name: str, aws_access_key_id: str, aws_secret_access_key: str):
    '''
    Initialize sqs client
    '''
    global SQS_CLIENT

    SQS_CLIENT = boto_client(
        'sqs',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def _init_sqs_resource(region_name: str, aws_access_key_id: str, aws_secret_access_key: str):
    '''
    Initialize sqs resource
    '''
    global SQS
    SQS = resource(
        'sqs',
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )


def use_credentials(aws_access_key_id: str, aws_secret_access_key: str, aws_region: str = None):
    '''
    Replace default credentials

    :type aws_access_key_id: str
    :param aws_access_key_id: AWS access key id.

    :type aws_secret_access_key: str
    :param aws_secret_access_key: AWS secret access key.

    :type aws_region: str
    :param aws_region: AWS region.
    '''
    global AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

    AWS_ACCESS_KEY_ID = aws_access_key_id
    AWS_SECRET_ACCESS_KEY = aws_secret_access_key

    # If aws region is to be changed
    if aws_region and isinstance(aws_region, str):
        AWS_REGION = aws_region

    # Re-initialize clients
    _init_sqs_client(AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    _init_sqs_resource(AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)


def get_queue_url(queue_name: str):
    '''
    Get queue's url.

    :type queue_name: str
    :param queue_name: The name of a queue.

    :rtype: str
    :return: The queue's url
    '''
    global SQS_CLIENT

    queue_url = ''

    try:
        response = SQS_CLIENT.get_queue_url(QueueName=queue_name)

        url = response.get('QueueUrl')
        if not url or url == '':
            err_msg = 'Queue Url cannot be retrieved from AWS, are you sure you provided the correct queue name.'
            LOGGER.error(err_msg)
            raise SQSException(SQSErrorCodes.QUEUE_DOES_NOT_EXIST, err_msg)

        queue_url = url
    except Exception as e:
        LOGGER.error(e)
        raise SQSException(SQSErrorCodes.UNKNOWN, f'Unknown error while retrieving queue url, are you sure you provided the correct queue name and aws credentials?. Error: {str(e)}')


    return queue_url


def get_sqs_client(queue_name: str):
    '''
    Get connection object to SQS Queue

    :type queue_name: str
    :param queue_name: The name of a queue.

    :rtype: str
    :return: The queue's url
    '''
    global SQS_CLIENT, SQS_CLIENT_CACHE, SQS, AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

    client = None

    # Initialize client (for queue url)
    if not SQS_CLIENT:
        _init_sqs_client(AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    # Initialize resource
    if not SQS:
        _init_sqs_resource(AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

    # Check if queue url exists
    if queue_name not in SQS_CLIENT_CACHE:
        queue_url = get_queue_url(queue_name)
        client = SQS.Queue(queue_url)

        # Cache the response
        SQS_CLIENT_CACHE[queue_name] = client
    else:
        client = SQS_CLIENT_CACHE[queue_name]

    return client


def get_messages_batch(messages: List[any]):
    '''
    Get message batch iterator
    '''
    global SQS_QUEUE_BATCH_LENGTH

    total_messages = len(messages)
    start_pos = 0

    while start_pos < total_messages:
        end_pos = min(start_pos + SQS_QUEUE_BATCH_LENGTH, total_messages)
        yield messages[start_pos:end_pos]
        start_pos += SQS_QUEUE_BATCH_LENGTH


@retry_with_backoff(retries=3)
@return_exception_as_parameter
def send_messages(queue_name: str, messages: List[str], e_type: Events, extra_attributes: dict = None) -> Tuple[bool, List[dict], Exception]:
    '''
    Send message to a queue

    :type queue_name: str
    :param queue_name: The name of a queue.

    :type message: str
    :param message: Message to be sent to the queue.

    :type attributes: dict
    :param attributes: Message attributes.

    :rtype: Tuple[[bool, List[dict]], Exception]
    :return: Returns failed to send messages as a boolean, and list of messages with message Id
    '''

    failed_to_send_messages = False
    messages_failed = []

    # Get client
    client = get_sqs_client(queue_name)

    # Assign each message an id
    messages_dict = [{
            'text': message,
            'id': uuid4().hex,
        } for message in messages
    ]

    for messages_ in get_messages_batch(messages_dict):
        entries = [
            {
                'Id': msg['id'],
                'MessageBody': str(msg['text']),
                'MessageAttributes': {
                    'EventType': {
                        'StringValue': str(e_type.value),
                        'DataType': 'String'
                    }
                }
            } for msg in messages_
        ]
        try:
            response = client.send_messages(Entries=entries)
            if "Failed" in response:
                messages_failed.append([
                    {
                        "Id": failed_message.get("Id"),
                        "Message": failed_message.get("Message"),
                    }
                    for failed_message in response["Failed"]
                ])

        except ClientError as err:
            LOGGER.error(err)

            if err.response['Error']['Code'] == 'InternalError':
                raise SQSException(SQSErrorCodes.CLIENT_INTERNAL_ERROR, f"Error Message: {str(err.response['Error']['Message'])}. Http code: {str(err.response['ResponseMetadata']['HTTPStatusCode'])}")
            else:
                raise SQSException(SQSErrorCodes.UNKNOWN, f'Unknown client error. Err: {str(err)}')
        except Exception as e:
            LOGGER.error(e)
            raise SQSException(SQSErrorCodes.UNKNOWN, str(e))

    return failed_to_send_messages, messages_failed


def send_cost_event(service_type: Service, vendor: Vendor, client_uuid: str, flow_uuid: str, call_uuid: str, conversation_uuid: str, num_hits=1, cost=0):
    # Get client
    client = get_sqs_client(WAREHOUSE_QUEUE_NAME)

    if cost > 0:
        num_hits = 0
    
    response = client.send_message(
        MessageAttributes={
            'EventType': {
                'StringValue': Events.WAREHOUSE_COST_TRACKER.value,
                'DataType': 'String'
            }
        },
        MessageBody=json.dumps({
            "service": service_type.value,
            "vendor": vendor.value,
            "client_uuid": client_uuid,
            "flow_uuid": flow_uuid,
            "call_uuid": call_uuid,
            "conversation_uuid": conversation_uuid,
            "num_hits": num_hits,
            "cost": cost,
        }),
    )

    return response
