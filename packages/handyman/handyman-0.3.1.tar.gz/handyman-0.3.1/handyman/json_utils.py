import json


def get_response_json(response):
    """
    Retrieves the JSON body of the response

    :param response: Response whose JSON is to be retrieved
    :return: JSON body of the response
    """
    response_json = {}
    if response is not None:
        try:
            response_json = response.json()
        except:
            pass  # Do nothing. Means the JSON in the response object is either not present or malformed.
    return response_json


def get_status_code(response):
    """
    Determines the status code from the response object.
    In case of an exceptional scenario, the status code returned is 0.

    :param response: response whose status code is to be determined
    :return: status code of the response
    """
    if response is None or not hasattr(response, 'status_code') or response.status_code is None:
        status_code = -1
    else:
        status_code = response.status_code
    return status_code


def json_format(json_body):
    """
    Formats a JSON to make it pretty printed

    :param json_body: JSON body which has to be pretty printed
    :return: An indented, human-readable (pretty printed) JSON string
    """
    pretty_printed_json = json_body
    try:
        if json_body is None:
            return ''
        if type(json_body) is dict:
            json_body = json.dumps(json_body)
        pretty_printed_json = json.dumps(json.loads(str(json_body)), indent=4, sort_keys=True)
    except:
        pass  # do nothing. Simply return the original argument back
    return pretty_printed_json


def load_json(path):
    """
    Load JSON from file

    :param path: Path from which to load the JSON
    :return: loaded JSON object
    """
    with open(path, encoding='utf-8') as fp:
        return json.load(fp)


def write_json_to_file(data, destination: str, mode):
    """
    Writes a JSON to a file

    :param data: JSON data
    :param destination: path of the destination
    :param mode: Mode in which file is to be written to
    """
    with open(destination, mode, encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
