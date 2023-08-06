import json
import logging
import os

import numpy as np
import pandas as pd
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import censius.utils as utils
from censius.constants import *
from censius.schemas import (
    batch_log_schema,
    bulk_log_schema,
    explanations_tabular_schema,
    individual_log_schema,
    log_explanations_schema,
    prediction_tabular_schema,
    process_model_schema,
    register_dataset_schema,
    register_model_schema,
    register_new_model_version_schema,
    register_project_schema,
    revise_model_schema,
    update_actual_schema,
    update_model_iteration_schema,
    update_model_schema,
)
from censius.utils import check_time_format, make_post_request


class CensiusClient(object):
    def __init__(self, api_key, tenant_id):
        if api_key == None or len(api_key) == 0:
            raise ValueError("You need to pass an API key")
        if tenant_id == None or len(tenant_id) == 0:
            raise ValueError("You need to pass a tenant ID")
        self.api_key = api_key
        self.tenantKey = tenant_id

    def register_project(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=register_project_schema)
        except ValidationError as e:
            return e.message

        Icon = None
        if "icon" in kwargs:
            Icon = str(kwargs["icon"])

        Type = None
        if "type" in kwargs:
            Type = kwargs["type"]

        Key = None
        if "key" in kwargs:
            Key = kwargs["key"]

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "icon": Icon,
                    "name": kwargs["name"],
                    "key": Key,
                    "type": Type,
                    "apiKey": self.api_key,
                    "tenantKey": self.tenantKey,
                }.items()
                if v
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request("POST", REGISTER_PROJECT_URL(), headers=headers, data=payload)
        return self.__return_message(response)

    def register_new_model_version(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=register_new_model_version_schema)
        except ValidationError as e:
            return e.message

        WindowSize = None
        if "window_size" in kwargs:
            WindowSize = kwargs["window_size"]

        WindowStartTime = None
        if "start_time" in kwargs:
            WindowStartTime = kwargs["start_time"]

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "userDefinedModelID": kwargs["model_id"],
                    "version": kwargs["model_version"],
                    "datasetId": kwargs["training_info"]["id"],
                    "targets": kwargs["targets"],
                    "features": kwargs["features"],
                    "apiKey": self.api_key,
                    "windowSize": WindowSize,
                    "window_start_time": WindowStartTime,
                    "tenantKey": self.tenantKey,
                }.items()
                if v
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request(
            "POST", REGISTER_NEW_MODEL_VERSION(), headers=headers, data=payload
        )
        if "error" in response.json().keys():
            return self.__return_message(response)
        else:
            values = []
            for i in kwargs["targets"]:
                temp = {}
                temp["target"] = i
                values.append(temp)
            primary_response = response
            self.process_model(
                dataset_id=kwargs["training_info"]["id"],
                model_id=response.json()["message"]["ID"],
                project_id=kwargs["project_id"],
                values=values,
            )
            return self.__return_message(primary_response)

    def register_dataset(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=register_dataset_schema)
        except ValidationError as e:
            return e.message

        rawValues = None
        if "raw_values" in kwargs:
            rawValues = str(kwargs["raw_values"])

        timestampBase = None
        timestampCol = None
        unixInterval = None
        timestampType = None
        if "timestamp" in kwargs:
            timestampBase = kwargs["timestamp"]
            timestampCol = timestampBase["name"]
            if "iso" not in timestampBase["type"]:
                timestampType = "unix"
                unixInterval = timestampBase["type"]
            else:
                timestampType = timestampBase["type"]

        Version = None
        if "version" in kwargs:
            Version = kwargs["version"]

        file = None
        if "file" in kwargs:
            file = kwargs["file"]
        file_path = None
        if "file_path" in kwargs:
            file_path = kwargs["file_path"]

        file_name = kwargs["name"] + ".csv"
        if file_path:
            if ".csv" not in file_path:
                return {"error": "Please provide a valid path for the csv file"}
            try:
                file = pd.read_csv(file_path)
                if (file.memory_usage().sum()) // 1000000 > 500:
                    return {"error": "Max allowed file size is 500 MB"}
                file.to_csv(file_name, index=False)

            except Exception as e:
                return {"error": "unable to read the csv file"}
        elif file is not None:
            if (file.memory_usage().sum()) // 1000000 > 500:
                return {"error": "Max allowed file size is 500 MB"}
            file.to_csv(file_name, index=False)
        else:
            return {"error": "Please provide a df object or a file path"}

        headers = {"Authorization": f"Bearer {self.api_key}"}

        payload = {
            "name": kwargs["name"],
            "projectId": kwargs["project_id"],
            "version": Version,
            "features": json.dumps(kwargs["features"]),
            "apiKey": self.api_key,
            "timestampCol": timestampCol,
            "unixInterval": unixInterval,
            "timestampType": timestampType,
            "rawValues": json.dumps(rawValues),
            "tenantKey": self.tenantKey,
        }
        files = [("File", (file_name, open(os.getcwd() + "/" + file_name, "rb"), "text/csv"))]

        response = requests.request(
            "POST", REGISTER_DATASET_URL(), headers=headers, data=payload, files=files
        )
        os.remove(os.getcwd() + "/" + file_name)
        return self.__return_message(response)

    def process_model(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=process_model_schema)
        except ValidationError as e:
            return e.message

        WindowSize = None
        if "window_size" in kwargs:
            WindowSize = kwargs["window_size"]

        WindowStartTime = None
        if "window_start_time" in kwargs:
            WindowStartTime = kwargs["window_start_time"]

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "windowSize": WindowSize,
                    "window_start_time": WindowStartTime,
                    "dataset_id": kwargs["dataset_id"],
                    "model_id": kwargs["model_id"],
                    "values": kwargs["values"],
                    "apiKey": self.api_key,
                    "project_id": kwargs["project_id"],
                }.items()
                if v
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request("POST", PROCESS_MODEL_URL(), headers=headers, data=payload)
        return self.__return_message(response)

    def register_model(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=register_model_schema)
        except ValidationError as e:
            return e.message

        targets = kwargs["targets"]

        features = kwargs["features"]

        WindowSize = None
        if "window_size" in kwargs:
            WindowSize = kwargs["window_size"]

        WindowStartTime = None
        if "start_time" in kwargs:
            WindowStartTime = kwargs["start_time"]

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "userDefinedModelID": kwargs["model_id"],
                    "version": kwargs["model_version"],
                    "datasetId": kwargs["training_info"]["id"],
                    "name": kwargs["model_name"],
                    "projectId": kwargs["project_id"],
                    "type": kwargs["model_type"],
                    "targets": targets,
                    "features": features,
                    "apiKey": self.api_key,
                    "windowSize": WindowSize,
                    "window_start_time": WindowStartTime,
                    "tenantKey": self.tenantKey,
                }.items()
                if v
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request("POST", REGISTER_MODEL_URL(), headers=headers, data=payload)
        if "error" in response.json().keys():
            return self.__return_message(response)
        else:
            values = []
            for i in targets:
                temp = {}
                temp["target"] = i
                values.append(temp)
            primary_response = response
            self.process_model(
                dataset_id=kwargs["training_info"]["id"],
                project_id=kwargs["project_id"],
                model_id=response.json()["message"]["ID"],
                values=values,
            )
            return self.__return_message(primary_response)

    def update_model(self, *args, **kwargs):
        """
        Update the model iteration
        :param kwargs:
        :return:
        """
        try:
            validate(instance=kwargs, schema=update_model_schema)
        except ValidationError as e:
            validationError = e.schema["errorMessage"] if "errorMessage" in e.schema else e.message
            return "ValidationError: " + validationError

        # replace the model_id with user_defined_model_id
        kwargs["user_defined_model_id"] = kwargs["model_id"]
        del kwargs["model_id"]

        header = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = json.dumps(kwargs)

        response = make_post_request(
            UPDATE_MODEL_META,
            header,
            payload,
        )
        return self.__return_message(response)

    def log(self, *args, **kwargs):
        if len(args) > 0 and str(type(args[0])) == "<class 'list'>":
            return self.__batch_log(args[0])
        else:
            return self.__individual_log(**kwargs)

    def bulk_log(self, input, **kwargs):
        # check in input is dataframe or not
        from collections import defaultdict

        predictions_received, actuals_received, explanations_received = False, False, False
        bulk_input_validation = utils.BulkLogsValidation()
        bulk_input_processing = utils.BulkLogProcessing()
        # ..> Standard Validation of datatypes and JSON schema
        """
            Standard validation for input dataframe
            1. Check if input is dataframe
            2. Check if input is empty
            3. Check if input dataframe has any empty row in the middle
        """
        error_flag, error_message = bulk_input_validation.check_for_input_dataframe(input)
        if error_flag:
            return {"error": True, "message": error_message}

        """
            Validation for kwargs parameters
        """
        try:
            validate(instance=kwargs, schema=bulk_log_schema)
        except ValidationError as e:
            return e.message

        """
            Standard Validation for <prediction_id_column>
            1. Check if <prediction_id_column> is in <input>
            2. Check if <prediction_id_column> is not Null
            3. Check if <prediction_id_column> is unique
        """

        error_flag, error_message = bulk_input_validation.checks_for_prediction_id_column(
            kwargs["prediction_id_column"], input
        )
        if error_flag:
            return {"error": True, "message": error_message}
        # if validation sucessful, change prediction_id_column datatype to string
        input[kwargs["prediction_id_column"]] = input[kwargs["prediction_id_column"]].astype(str)

        """
            Check if "predictions" has been passed by user or not
            1. Check if "predictions" is in <kwargs>
            if yes, then perform further checks
                2. "prediction" schema validation
                3. Validations for "prediction_column"
                4. Validations for "prediction_confidence_column"
                5. Validations for "timestamp_column"
        """
        if "predictions" in kwargs.keys():
            try:
                prediction_tabular = kwargs["predictions"]
                validate(instance=prediction_tabular, schema=prediction_tabular_schema)
                predictions_received = True
            except ValidationError as e:
                return "PredictionsTabular ValidationError : " + e.message

            """
                Standard Validation for <prediction_column> 
                1. Check if <prediction_column> is in <input>
                2. Check if <prediction_column> is not Null

                Note: <prediction_column>  datatype validation happens in the later section 
                ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            """
            error_flag, error_message = bulk_input_validation.checks_for_prediction_column(
                prediction_tabular["prediction_column"], input
            )
            if error_flag:
                return {"error": True, "message": error_message}
            prediction_column = prediction_tabular["prediction_column"]
            prediction_column_dt = str(input[prediction_column].dtype)

            """
                Standard Validation for <prediction_confidence_column>
                1. Check if <prediction_confidence_column> is in <input>
                2. Check if <prediction_confidence_column> is not Null
                3. Check if <prediction_confidence_column> is of type float
                ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            """
            (
                error_flag,
                error_message,
            ) = bulk_input_validation.prediction_confidence_column_checks(
                prediction_tabular["prediction_confidence_column"], input
            )
            if error_flag:
                return {"error": True, "message": error_message}

            """
                Standard Validation for <timestamp_column>
                1. Check if <timestamp_column> is in <input>
                2. Check if <timestamp_column> is not Null
                3. Check if <timestamp_column> is of type datetime
                ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
            """
            (error_flag, error_message,) = bulk_input_validation.timestamp_column_checks(
                prediction_tabular["timestamp_column"], input
            )
            if error_flag:
                return {"error": True, "message": error_message}

        if "explanations" in kwargs.keys():
            try:
                explanations_tabular = kwargs["explanations"]
                validate(instance=explanations_tabular, schema=explanations_tabular_schema)
                explanations_received = True
            except ValidationError as e:
                return "ExplanationsTabular ValidationError : " + e.message
            print(" [info] Validating the input for Explainabtion.Tabular.")
            """
                Standard Validation for <Explanations.Tabular>
                1. Check if <explaination_input_column(s)> are in <input> dataframe
                2. Check if <explaination_input_column(s)> are not Null
                3. Check if <explaination_input_column(s)> is of type float64
            """
            exp_registered_to_provided = utils.extract_features_details(
                explanations_tabular["explanation_mapper"]
            )
            exp_provided_columns = list(exp_registered_to_provided.values())
            (
                error_flag,
                error_message,
            ) = bulk_input_validation.explainations_checks(input, exp_provided_columns)

            if error_flag:
                return {"error": True, "message": error_message}

        """
            Check if "actuals_column" has been passed by user or not
            if yes, then perform further checks
                2. "actuals_column" present in <input>
        """

        if "actuals" in kwargs.keys():
            actuals_column = kwargs["actuals"]
            if kwargs["actuals"] not in input.columns:
                return f"ValidationError: <actuals>={actuals_column} not found in input dataframe"
            actuals_received = True
            actuals_column_dt = str(input[actuals_column].dtype)

        # if actuals_received false and predictions_received false and explanations_received false return error
        if not actuals_received and not predictions_received and not explanations_received:
            return "ValidationError: No data received to log"

        # if explanations_received true and predictions_received false and actuals_received false return error
        if explanations_received and not predictions_received and not actuals_received:
            return "ValidationError: Explanations cannot be logged without predictions or actuals"

        """
            Check if "predictions_received" is True
            if yes, then perform further checks
                1. Check for "features" key to be present in <prediction_tabular>
                if yes, then perform further checks
                    2. "features" key should be empty or list of objects
                    3. Check if provided "features" are present in <input>
            else
                1. Consider all <input> columns as <features>
                2. Except timestamp_column, prediction_column, prediction_confidence_column
        """
        if predictions_received:
            if "features" in prediction_tabular.keys():
                print(" [info] Considering Prediction.Tabular columns as features.")
                registered_to_provided = dict()
                if len(prediction_tabular["features"]) == 0:
                    return "ValidationError: <features> in Prediction.Tabular can be absent OR must be a list of maps {'feature':'<registered_feature_name>','input_column':'<column_name>'}"
                # print(" - Column name validation for features in Prediction.Tabular")
                registered_to_provided = utils.extract_features_details(
                    prediction_tabular["features"]
                )
                provided_feature_columns = list(registered_to_provided.values())
                missing_columns = bulk_input_validation.check_provided_column_with_input_columns(
                    provided_feature_columns, input.columns
                )
                if len(missing_columns) > 0:
                    return (
                        "[error]  ValidationError: <input> dataframe columns mismatching in Prediction.Tabular, MissmatchingCols - "
                        + str(missing_columns)
                    )

            else:
                print(" [info] Considering all of dataframe columns as features.")
                provided_feature_columns = list(input.columns)
                provided_feature_columns.remove(prediction_tabular["timestamp_column"])
                provided_feature_columns.remove(prediction_tabular["prediction_column"])
                provided_feature_columns.remove(prediction_tabular["prediction_confidence_column"])
                registered_to_provided = {col: col for col in provided_feature_columns}

        # input_inferred_datatype = { column: str(input.dtypes[column]) for column in provided_columns }

        """
            fetching registered dataset datatype from the server
        """
        payload = json.dumps(
            {"modelID": kwargs["model_id"], "modelVersion": kwargs["model_version"]}
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        try:
            response = requests.request(
                "POST", BULK_LOG_DATATYPE_VALIDATION_URL, headers=headers, data=payload
            )
        except:
            return self.__return_message(
                {"error": True, "message": "ConnectionError: Unable to connect to server."}
            )

        if response.status_code == 200:
            registered_dataset_details = json.loads(response.content)
            registered_dataset_to_datatype, registered_model_target = dict(), list()
            registered_dataset_to_datatype = registered_dataset_details["dataset_datatype"]
            registered_model_target_to_datatype = registered_dataset_details[
                "model_target_datatype"
            ]
            registered_model_target = registered_dataset_details["model_target"]
            model_target_col = registered_model_target[0]

            # merge registered_model_target_to_datatype with registered_dataset_to_datatype
            """
            registered_dataset_to_datatype = {"Age": "integer","Pclass": "integer"}
            registered_model_target_to_datatype = {"Survived": "integer"} # then
            registered_dataset_to_datatype = {"Age": "integer",
                                           "Pclass": "integer",
                                           "Survived": "integer"}
            """
            registered_dataset_to_datatype.update(registered_model_target_to_datatype)

            # remove model_target from registered_dataset_to_datatype
        else:
            return self.__return_message(response)

        if predictions_received:
            """
            Check if "features" key is present in <prediction_tabular>
            if yes, then perform further checks
                1. Check if all registered_features are present in provided_feature_columns
                    1.1: Except "registered_model_target"
                2. Check if datatype of provided_features is same as registered_features

            if no, then perform further checks
                1. Check if all registered_features are present input dataframe columns
                    1.1: Except "registered_model_target"
                2. Check if datatype of dataframe column is same as registered_features
                3. Check if datatype of prediction column is same as registered_model_target
            """
            (error_flag, error_message,) = bulk_input_validation.prediction_tabular_checks(
                input,
                registered_dataset_to_datatype,
                registered_model_target,
                registered_to_provided,
            )

            if error_flag:
                return {"error": True, "message": error_message}

            """
                <prediction_column> datatype check
            """
            feature_dt = str(registered_dataset_to_datatype[model_target_col])
            match_result = bulk_input_validation.registered_datatype_vs_input_datatype(
                feature_dt, prediction_column_dt
            )
            if not match_result:
                datatype_error = f"Input <{prediction_column}> has datatype {prediction_column_dt} while expected is datatype {feature_dt}"
                return (
                    f" [error] ValidationError: <prediction_column> datatype mismatch with model_target: <{model_target_col}>, "
                    + datatype_error
                )

        if actuals_received:
            """
            <actuals_column> datatype check
            """
            feature_dt = str(registered_dataset_to_datatype[model_target_col])
            match_result = bulk_input_validation.registered_datatype_vs_input_datatype(
                feature_dt, actuals_column_dt
            )
            if not match_result:
                datatype_error = f"Input <{actuals_column}> has datatype {actuals_column_dt} while expected is datatype {feature_dt}"
                return (
                    f" [error] ValidationError: <actuals> datatype mismatch with model_target: <{model_target_col}>, "
                    + datatype_error
                )

        if explanations_received:
            explanations_received = True
            exp_tab_specified_feat = list(exp_registered_to_provided.keys())
            model_registered_feat = list(registered_dataset_to_datatype.keys())
            error_columns = bulk_input_validation.exp_tabular_feature_with_registered(
                exp_tab_specified_feat, model_registered_feat, registered_model_target
            )

            if len(error_columns) > 0:
                return f" [error] ValidationError: In Explanation.Tabular No column(s) in <input> dataframe is mapped to following registered_feature(s): {error_columns}"

        ##########################################
        ###### BULK INPUT PROCESSING START #######
        ###### FOR PREDICTONS AND ACTUALS ########
        ##########################################
        """
            Renaming & Cleaning the dataframe columns to registered dataset columns
            1. if prediction exists, then rename prediction column to registered model_target
            2. if actuals exists, then rename actuals column to registered model_target
            3. if features exists, then rename features columns to registered features
            4. Replacing all NaN values with None
        """
        if predictions_received or actuals_received:
            input_map = dict()
            input_map[kwargs["prediction_id_column"]] = "log_id"
            if predictions_received:
                input_map = utils.bulk_col_renaming_map_for_preds(
                    input_map,
                    registered_to_provided,
                    registered_dataset_to_datatype,
                    registered_model_target,
                )
                input_map[prediction_tabular["timestamp_column"]] = "timestamp"
                input_map[prediction_tabular["prediction_column"]] = (
                    f"prediction_class_" + model_target_col.lower()
                )
                input_map[prediction_tabular["prediction_confidence_column"]] = (
                    f"prediction_score_" + model_target_col.lower()
                )

            if actuals_received:
                input_map[actuals_column] = f"actual_" + model_target_col.lower()

            processed_input = input.rename(columns=input_map, inplace=False)
            # only keep the columns that are required for bulk logging
            processed_input = processed_input[list(input_map.values())]
            # processed_input = processed_input.where(pd.notnull(processed_input), None)
            processed_input = processed_input.replace({np.nan: None})

            """
                Call in bulk processing class to divide the dataframe into chunks and process.
                Send the following inputs to Censius Log Server via POST request
                Inputs:
                    1. input dataframe
                    2. input_map
                    3. headers
                Headers:
                    1. Authorization (using API Key)
                    2. Content-Type   
            """
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            model_details = {
                "modelID": kwargs["model_id"],
                "modelVersion": kwargs["model_version"],
                "predicitionsRecvd": predictions_received,
                "actualsRecvd": actuals_received,
                "actualColumn": input_map[actuals_column] if actuals_received else "None",
            }
            # input rename column name using input_map
            # print(input_map)
            # process_bulk
            response = bulk_input_processing.process_bulk(processed_input, headers, model_details)

        ##########################################
        ###### BULK INPUT PROCESSING START #######
        ########## FOR EXPLANATIONS ##############
        ##########################################

        if explanations_received:
            # print(input.head())
            exp_input_map = dict()
            exp_input_map[kwargs["prediction_id_column"]] = "log_id"
            exp_input_map = utils.bulk_col_renaming_map_for_exp(
                exp_input_map,
                exp_registered_to_provided,
                registered_dataset_to_datatype,
                registered_model_target,
            )

            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            model_details = {
                "modelID": kwargs["model_id"],
                "modelVersion": kwargs["model_version"],
            }
            processed_input = input.rename(columns=exp_input_map, inplace=False)
            # only keep the columns that are required for bulk logging
            processed_input = processed_input[list(exp_input_map.values())]
            response = bulk_input_processing.process_bulk_explain(
                processed_input, headers, model_details
            )

        return self.__return_message(response)

    def update_model_iteration(self, **kwargs):
        """
        Update the model iteration
        :param kwargs:
        :return:
        """
        try:
            validate(instance=kwargs, schema=update_model_iteration_schema)
        except ValidationError as e:
            validationError = e.schema["errorMessage"] if "errorMessage" in e.schema else e.message
            return "ValidationError: " + validationError

        # replace the model_id with user_defined_model_id
        kwargs["user_defined_model_id"] = kwargs["model_id"]
        del kwargs["model_id"]

        header = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = json.dumps(kwargs)

        # check if dataset_start_time is smaller than dataset_end_time
        if kwargs["dataset_start_datetime"] >= kwargs["dataset_end_datetime"]:
            return "ValidationError:  dataset_end_datetime must be greater than dataset_start_datetime"

        response = make_post_request(
            ADD_MODEL_ITERATION,
            header,
            payload,
        )
        return self.__return_message(response)

    def __individual_log(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=individual_log_schema)
        except ValidationError as e:
            return e.message

        raw_values = None
        if "raw_values" in kwargs:
            raw_values = kwargs["raw_values"]

        actual = None
        if "actual" in kwargs:
            actual = kwargs["actual"]

        rightFormat = check_time_format(kwargs["timestamp"])
        if not rightFormat:
            return "Timestamp is not of the Unix MS format"

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "predictionID": kwargs["prediction_id"],
                    "modelVersion": kwargs["model_version"],
                    "modelID": kwargs["model_id"],
                    "features": kwargs["features"],
                    "prediction": kwargs["prediction"],
                    "timestamp": kwargs["timestamp"],
                    "rawValues": raw_values,
                    "actual": actual,
                }.items()
                if v
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request("POST", LOG_URL(), headers=headers, data=payload)

        return self.__return_message(response)

    def __batch_log(self, *args, **kwargs):
        try:
            validate(instance=args[0], schema=batch_log_schema)
        except ValidationError as e:
            return e.message

        payload = []
        for log_data in args[0]:
            raw_values = None
            if "raw_values" in log_data:
                raw_values = log_data["raw_values"]

            actual = None
            if "actual" in log_data:
                actual = log_data["actual"]

            payload.append(
                {
                    k: v
                    for k, v in {
                        "predictionID": log_data["prediction_id"],
                        "modelVersion": log_data["model_version"],
                        "modelID": log_data["model_id"],
                        "features": log_data["features"],
                        "prediction": log_data["prediction"],
                        "timestamp": log_data["timestamp"],
                        "rawValues": raw_values,
                        "actual": actual,
                    }.items()
                    if v
                }
            )

        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request("POST", LOG_URL(), headers=headers, data=json.dumps(payload))
        return self.__return_message(response)

    def update_actual(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=update_actual_schema)
        except ValidationError as e:
            return e.message

        payload = json.dumps(
            {
                "modelID": kwargs["model_id"],
                "modelVersion": kwargs["model_version"],
                "actual": kwargs["actual"],
            }
        )
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        response = requests.request(
            "POST", UPDATE_ACTUAL_URL(kwargs["prediction_id"]), headers=headers, data=payload
        )
        return self.__return_message(response)

    def log_explanation(self, *args, **kwargs):
        try:
            validate(instance=kwargs, schema=log_explanations_schema)
        except ValidationError as e:
            return e.message

        payload = json.dumps(
            {
                k: v
                for k, v in {
                    "modelID": kwargs["model_id"],
                    "modelVersion": kwargs["model_version"],
                    "log_id": kwargs["prediction_id"],
                    "apiKey": self.api_key,
                    "explanation_type": kwargs["explanation_type"],
                    "explanation_values": kwargs["explanation_values"],
                    "tenantKey": self.tenantKey,
                }.items()
                if v
            }
        )
        headers = {"Authorization": "Bearer " + self.api_key, "Content-Type": "application/json"}
        response = requests.request("POST", LOG_EXPLAINATIONS_URL(), headers=headers, data=payload)
        return self.__return_message(response)

    def __return_message(self, response):
        # if response is dict
        if isinstance(response, dict):
            return response
        try:
            return response.json()["message"]
        except:
            if "error" in response.json().keys():
                return response.json()["error"]
            else:
                return (
                    "Something went wrong. Request failed with status code"
                    + " "
                    + str(response.status_code)
                )
