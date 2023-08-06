from censius.endpoint import CENSIUS_ENDPOINT


BASE_URL = f"{CENSIUS_ENDPOINT}/logs-svc/v1"
AMS_URL = f"{CENSIUS_ENDPOINT}/ams-svc"
MONITORS_PROGRAMMATIC_BASE_URL = f"{CENSIUS_ENDPOINT}/v1/programmatic"

# Models
REGISTER_MODEL_URL = lambda: f"{AMS_URL}/models/"
REVISE_MODEL_URL = lambda: f"{AMS_URL}/models/revise"
PROCESS_MODEL_URL = lambda: f"{AMS_URL}/models/schema-updation"
REGISTER_NEW_MODEL_VERSION = lambda: f"{AMS_URL}/models/model_version"
ADD_MODEL_ITERATION = f"{AMS_URL}/models/addModelIteration"
UPDATE_MODEL_META = f"{AMS_URL}/models/updateModelMeta"

# Logs
LOG_URL = lambda: f"{BASE_URL}/logs"
UPDATE_ACTUAL_URL = lambda prediction_id: f"{BASE_URL}/logs/{prediction_id}/updateActual"
BULK_LOG_DATATYPE_VALIDATION_URL = f"{BASE_URL}/logs/validate_bulk_datatype"
BULK_LOG_URL = f"{BASE_URL}/logs/bulk_logs"
LOG_EXPLAINATIONS_URL = lambda: f"{BASE_URL}/explainations"
BULK_EXPLAINATIONS_URL = f"{BASE_URL}/explainations/bulk_explainations"

# Dataset
REGISTER_DATASET_URL = lambda: f"{AMS_URL}/datasets/create-and-upload"

# Project
REGISTER_PROJECT_URL = lambda: f"{AMS_URL}/projects/"

GET_MODEL_HEALTH_URL = lambda: f"{MONITORS_PROGRAMMATIC_BASE_URL}/get_model_health"

# General constants
BULK_CHUNK_SIZE = 2000
GENERAL_TIMEOUT = 10
BASE_MILLISECONDS_2000 = 946684800000
CEIL_MILLISECONDS_2100 = 4102444800000
