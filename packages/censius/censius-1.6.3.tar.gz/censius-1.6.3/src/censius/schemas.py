from censius import ExplanationType, ModelType, DatasetType, Dataset
from censius.constants import BASE_MILLISECONDS_2000, CEIL_MILLISECONDS_2100

register_new_model_version_schema = {
    "type": "object",
    "properties": {
        "model_id": {"type": "string"},
        "training_info": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "method": {"type": "string", "enum": [Dataset.ID]},
            },
            "required": ["id", "method"],
        },
        "model_version": {"type": "string"},
        "targets": {"type": "array", "items": {"type": "string"}},
        "features": {"type": "array", "items": {"type": "string"}},
        "window_size": {
            "type": "object",
            "properties": {
                "number": {"type": "integer"},
                "unit": {"type": "string", "enum": ["day", "week", "hour"]},
            },
            "required": ["number", "unit"],
        },
        "start_time": {"type": "integer"},
    },
    "required": ["training_info", "model_id", "model_version", "targets", "features"],
}


register_model_schema = {
    "type": "object",
    "properties": {
        "model_id": {"type": "string"},
        "training_info": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "method": {"type": "string", "enum": [Dataset.ID]},
            },
            "required": ["id", "method"],
        },
        "model_name": {"type": "string"},
        "model_version": {"type": "string"},
        "project_id": {"type": "integer"},
        "model_type": {
            "type": "string",
            "enum": [ModelType.BINARY_CLASSIFICATION, ModelType.REGRESSION],
        },
        "targets": {"type": "array", "items": {"type": "string"}},
        "features": {"type": "array", "items": {"type": "string"}},
        "window_size": {
            "type": "object",
            "properties": {
                "number": {"type": "integer"},
                "unit": {"type": "string", "enum": ["day", "week", "hour"]},
            },
            "required": ["number", "unit"],
        },
        "start_time": {"type": "integer"},
    },
    "required": [
        "training_info",
        "model_id",
        "model_version",
        "model_name",
        "project_id",
        "model_type",
        "targets",
        "features",
    ],
}
register_dataset_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "project_id": {"type": "integer"},
        "features": {
            "type": "array",
            "properties": {
                "name": {"type": "string"},
                "type": {
                    "type": "string",
                    "enum": [DatasetType.DECIMAL, DatasetType.INT, DatasetType.STRING],
                },
            },
            "required": ["name", "type"],
        },
        "raw_values": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "type": {
                    "type": "string",
                    "enum": [
                        DatasetType.DECIMAL,
                        DatasetType.INT,
                        DatasetType.STRING,
                        DatasetType.BOOLEAN,
                    ],
                },
            },
            "required": ["name", "type"],
        },
        "version": {"type": "string"},
        "file_path": {"type": "string"},
        "timestamp": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "type": {
                    "type": "string",
                    "enum": [
                        DatasetType.UNIX_MS,
                        DatasetType.UNIX_NS,
                        DatasetType.UNIX_S,
                        DatasetType.ISO,
                    ],
                },
            },
            "required": ["name", "type"],
        },
    },
    "required": ["name", "project_id", "features"],
}


process_model_schema = {
    "type": "object",
    "properties": {
        "dataset_id": {"type": "integer"},
        "model_id": {"type": "integer"},
        "values": {
            "type": "array",
            "properties": {"target": {"type": "string"}, "perdiction": {"type": "string"}},
            "required": ["target"],
        },
        "window_start_time": {"type": "integer"},
        "window_size": {
            "type": "object",
            "properties": {
                "number": {"type": "integer"},
                "unit": {"type": "string", "enum": ["day", "week", "hour"]},
            },
            "required": ["number", "unit"],
        },
    },
    "required": ["dataset_id", "model_id", "values"],
}


revise_model_schema = {
    "type": "object",
    "properties": {
        "model_id": {"type": "string"},
        "model_version": {"type": "string"},
        "training_info": {
            "type": "object",
            "properties": {
                "start_time": {"type": "integer"},
                "end_time": {"type": "integer"},
                "window_size": {"type": "integer"},
                "method": {"type": "string", "enum": [Dataset.FIXED, Dataset.ROLLING]},
            },
            "required": ["method"],
        },
    },
    "required": ["model_id", "model_version", "training_info"],
}

update_actual_schema = {
    "type": "object",
    "properties": {
        "prediction_id": {"type": "string"},
        "actual": {"type": "object"},
        "model_version": {"type": "string"},
        "model_id": {"type": "string"},
    },
    "required": ["model_id", "model_version", "actual", "prediction_id"],
}


prediction_tabular_schema = {
    "type": "object",
    "properties": {
        "prediction_column": {"type": "string"},
        "prediction_confidence_column": {"type": "string"},
        "timestamp_column": {"type": "string"},
        "features": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "feature": {"type": "string"},
                    "input_column": {"type": "string"},
                },
                "required": ["feature", "input_column"],
            },
        },
    },
    "required": ["prediction_column", "timestamp_column", "prediction_confidence_column"],
}

explanations_tabular_schema = {
    "type": "object",
    "properties": {
        "type": {"type": "string"},
        "explanation_mapper": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "feature": {"type": "string"},
                    "input_column": {"type": "string"},
                },
                "required": ["feature", "input_column"],
            },
        },
    },
    "required": ["type", "explanation_mapper"],
}

bulk_log_schema = {
    "type": "object",
    "properties": {
        "model_id": {"type": "string"},
        "model_version": {"type": "string"},
        "prediction_id_column": {"type": "string"},
        "predictions": {
            "type": "object",
        },
    },
    "required": ["prediction_id_column", "model_id", "model_version"],
}

individual_log_schema = {
    "type": "object",
    "properties": {
        "prediction_id": {"type": "string"},
        "model_version": {"type": "string"},
        "model_id": {"type": "string"},
        "features": {"type": "object"},
        "prediction": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "label": "integer",
                    "confidence": "integer",
                    "required": ["label", "confidence"],
                }
            },
        },
        "timestamp": {"type": "integer"},
        "raw_values": {"type": "object"},
        "actual": {"type": "object"},
    },
    "required": [
        "prediction_id",
        "model_version",
        "model_id",
        "features",
        "prediction",
        "timestamp",
    ],
}


batch_log_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "prediction_id": {"type": "string"},
            "model_version": {"type": "string"},
            "model_id": {"type": "string"},
            "features": {"type": "object"},
            "prediction": {
                "type": "object",
                "patternProperties": {
                    ".*": {
                        "type": "object",
                        "label": "integer",
                        "confidence": "integer",
                        "required": ["label", "confidence"],
                    }
                },
            },
            "timestamp": {"type": "integer"},
            "raw_values": {"type": "object"},
            "actual": {"type": "object"},
        },
        "required": [
            "prediction_id",
            "model_version",
            "model_id",
            "features",
            "prediction",
            "timestamp",
        ],
    },
}


register_project_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "type": {"type": "string"},
        "key": {"type": "string"},
        "icon": {"type": "string"},
    },
    "required": ["name"],
}

log_explanations_schema = {
    "type": "object",
    "properties": {
        "prediction_id": {"type": "string"},
        "explanation_type": {"type": "string", "enum": [ExplanationType.SHAP]},
        "model_version": {"type": "string"},
        "model_id": {"type": "string"},
        "explanation_values": {"type": "object"},
    },
    "required": [
        "model_id",
        "model_version",
        "explanation_type",
        "prediction_id",
        "explanation_values",
    ],
}

update_model_schema = {
    "type": "object",
    "properties": {
        "model_id": {
            "type": "string",
            "errorMessage": "model_id is required, and must be string.",
        },
        "model_version": {
            "type": "string",
            "errorMessage": "model_version is required, and must be string.",
        },
        "update_meta": {
            "type": "object",
            # either one of the two is required
            "anyOf": [
                {
                    "required": ["model_name"],
                    "errorMessage": "Any of model_name, model_id, and model_version is required in `update_meta`",
                },
                {
                    "required": ["model_id"],
                    "errorMessage": "Any of model_name, model_id, and model_version is required in `update_meta`",
                },
                {
                    "required": ["model_version"],
                    "errorMessage": "Any of model_name, model_id, and model_version is required in `update_meta`",
                },
            ],
            "properties": {
                "model_name": {"type": "string"},
                "model_id": {"type": "string"},
                "model_version": {"type": "string"},
            },
        },
    },
    "required": [
        "model_id",
        "model_version",
        "update_meta",
    ],
}


update_model_iteration_schema = {
    "type": "object",
    "properties": {
        "model_id": {
            "type": "string",
            "errorMessage": "model_id is required, and must be string.",
        },
        "model_version": {
            "type": "string",
            "errorMessage": "model_version is required, and must be string.",
        },
        "model_iteration_id": {
            "type": "string",
            "maxLength": 16,
            "errorMessage": "model_iteration_id must be string, and max length is 16.",
        },
        "release_datetime": {
            "type": "number",
            "exclusiveMinimum": BASE_MILLISECONDS_2000,
            "exclusiveMaximum": CEIL_MILLISECONDS_2100,
            "errorMessage": "release_datetime must be in milliseconds, example: 1600000000000",
        },
        "dataset_start_datetime": {
            "type": "number",
            "exclusiveMinimum": BASE_MILLISECONDS_2000,
            "exclusiveMaximum": CEIL_MILLISECONDS_2100,
            "errorMessage": "dataset_start_datetime must be in milliseconds, example: 1600000000000",
        },
        "dataset_end_datetime": {
            "type": "number",
            "exclusiveMinimum": BASE_MILLISECONDS_2000,
            "exclusiveMaximum": CEIL_MILLISECONDS_2100,
            "errorMessage": "dataset_end_datetime must be in milliseconds, example: 1600000000000",
        },
        "training_accuracy": {
            "type": "number",
            "minimum": 0.01,
            "maximum": 100,
            "multipleOf": 0.01,
            "errorMessage": "training_accuracy must be between 0.01 and 1",
        },
        "validation_accuracy": {
            "type": "number",
            "minimum": 0.01,
            "maximum": 100,
            "multipleOf": 0.01,
            "errorMessage": "validation_accuracy must be between 0.01 and 1",
        },
        "area_under_curve": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "multipleOf": 0.0001,
            "errorMessage": "area_under_curve must be between 0.0001 and 1",
        },
        "samples_count": {"type": "integer"},
    },
    "required": [
        "model_id",
        "model_version",
        "release_datetime",
        "dataset_start_datetime",
        "dataset_end_datetime",
    ],
}
