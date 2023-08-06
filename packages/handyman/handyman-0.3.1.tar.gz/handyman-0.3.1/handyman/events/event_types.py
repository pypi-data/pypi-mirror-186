from enum import Enum

class Events(Enum):
    WAREHOUSE_CALLS = 'WAREHOUSE_CALLS_DATA'
    WAREHOUSE_TCN = 'WAREHOUSE_TCN_DATA'
    WAREHOUSE_LEADS = 'WAREHOUSE_LEADS_DATA'
    WAREHOUSE_COST_TRACKER = 'WAREHOUSE_COST_TRACKER'

class Service(Enum):
    ASR = "ASR"
    TTS = "TTS"
    SLU = "SLU"

class Vendor(Enum):
    GOOGLE = "GOOGLE"
    SKIT = "SKIT"
    AZURE = "AZURE"
