import datetime as dt
import json
import random
import string
import threading
import time
from multiprocessing.pool import ThreadPool
from typing import Any, Tuple
from urllib import request

import numpy as np
import pandas as pd
import requests

from censius.constants import *


class BulkLogsValidation:
    def __init__(self):
        self.datatype_mapper = {
            "int64": "integer",
            "float64": "decimal",
            "object": "text",
        }

    def check_for_input_dataframe(self, input: Any) -> Tuple[bool, str]:
        # if input is not pandas dataframe return error
        if not isinstance(input, pd.DataFrame):
            return True, f" ValidationError: <input> is not a pandas dataframe"
        if input.empty:
            return True, "  ValidationError: <input> dataframe is empty"
        # ..> if dataframe has empty row in middle return error
        # if input.isnull().any().any():
        #     return True, "  ValidationError: <input> dataframe has empty row in middle"
        return False, ""

    def check_registered_with_provided_columns(
        self, registered_features: list, provided_features: list
    ) -> Tuple[bool, list]:
        error_list = list()
        for single_feature in provided_features:
            if provided_features not in registered_features:
                error_list.append(f"'{provided_features}' is not a registered feature")
        if len(error_list) > 0:
            return True, error_list
        else:
            return False, error_list

    def checks_for_prediction_column(
        self, prediction_column: str, input: pd.DataFrame
    ) -> Tuple[bool, str]:
        if prediction_column not in input.columns:
            return (
                True,
                f"  ValidationError: <prediction_column>='{prediction_column}' not found in <input> dataframe",
            )

        # if prediction_id_column has null return error
        if input[prediction_column].isnull().any():
            return (
                True,
                f"  ValidationError: <prediction_column>='{prediction_column}' has null values, <prediction_column> must be NOT NULL",
            )
        return False, ""

    def prediction_confidence_column_checks(
        self, prediction_confidence_column: str, input: pd.DataFrame
    ) -> Tuple[bool, str]:

        if prediction_confidence_column not in input.columns:
            return (
                True,
                f"  ValidationError: <prediction_confidence_column>='{prediction_confidence_column}' not found in <input>",
            )

        # if prediction_confidence_column has null return error
        if input[prediction_confidence_column].isnull().any():
            return (
                True,
                f"  ValidationError: <prediction_confidence_column>='{prediction_confidence_column}' has null values, <prediction_confidence_column> must be NOT NULL",
            )

        # if prediction_confidence_column doesnt has float or int values return error
        if str(input[prediction_confidence_column].dtype) not in ["float64", "int64"]:
            return (
                True,
                f"  ValidationError: <prediction_confidence_column>='{prediction_confidence_column}' has to be of type float64 or int64",
            )

        return False, ""

    def timestamp_column_checks(
        self, timestamp_column: str, input: pd.DataFrame
    ) -> Tuple[bool, str]:
        if timestamp_column not in input.columns:
            return (
                True,
                f"  ValidationError: <timestamp_column>='{timestamp_column}' not found in <input> dataframe",
            )

        # if timestamp_column has null return error
        if input[timestamp_column].isnull().any():
            return (
                True,
                f"  ValidationError: <timestamp_column>='{timestamp_column}' has null values, <timestamp_column> must be NOT NULL",
            )

        try:
            input[timestamp_column] = input.apply(
                lambda x: x[timestamp_column] * 1000
                if len(str(x[timestamp_column])) == 10
                else x[timestamp_column],
                axis=1,
            )
        except:
            return (
                True,
                f"  ValidationError: <timestamp_column>='{timestamp_column}' has to be of type int64 or float64, and is supposed to be in milliseconds, example: 1620000000000",
            )
        # if timestamp_column cannot be converted to datetime return error
        try:
            input["timestamp_val"] = pd.to_datetime(input[timestamp_column], unit="ms")
            # pd.to_datetime(input[timestamp_column])
        except:
            return (
                True,
                f"  ValidationError: <timestamp_column>='{timestamp_column}' incorrect format cannot be converted to datetime. <timestamp_column>= is supposed to be in milliseconds, example: 1620000000000",
            )
        return False, ""

    def checks_for_prediction_id_column(
        self, prediction_id_column: str, input: pd.DataFrame
    ) -> Tuple[bool, str]:
        """
        input:
            prediction_id_column - prediction_id_column name
            input - input dataframe
        output:
            error_flag: True - if any validation failed else False
            error_message: error message
        This function will check if the registered datatype with the input dataframe is same or not.
        """
        if prediction_id_column not in input.columns:
            return True, "  ValidationError: <prediction_id_column> not found in <input> dataframe"

        # if prediction_id_column has null return error
        if input[prediction_id_column].isnull().any():
            return (
                True,
                "  ValidationError: <prediction_id_column> has null values, <prediction_id_column> must be unique and NOT NULL",
            )

        # if prediction_id_column has duplicates return error
        if input[prediction_id_column].duplicated().any():
            return (
                True,
                "  ValidationError: <prediction_id_column> has duplicates, <prediction_id_column> must be unique and NOT NULL",
            )
        return False, ""

    def check_provided_column_with_input_columns(
        self,
        provided_columns: list,
        input_columns: list,
        missing_columns=[],
    ) -> list:
        for column in provided_columns:
            # check if all the provided column name present in the dataframe or not.
            if column not in input_columns:
                missing_columns.append(column)
        return missing_columns

    def registered_datatype_vs_input_datatype(
        self, registered_datatype: str, input_datatype: str
    ) -> bool:
        input_datatype = self.datatype_mapper[input_datatype]
        if registered_datatype == input_datatype:
            return True
        else:
            return False

    def registered_datatype_with_input(
        self,
        registered_dataset: dict,
        input: pd.DataFrame,
        registered_model_target: list,
        registered_to_provided: dict = None,
    ) -> list:
        """
        This function will check if the registered datatype with the input dataframe is same or not.
        """
        datatype_error_list = []
        for (feature_name, feature_dt) in registered_dataset.items():
            if feature_name.lower() in registered_model_target:
                continue
            if registered_to_provided is not None:
                """
                if Prediction.Tabular is used then registered_to_provided will be mapped to provided_columns
                """
                feature_name = registered_to_provided[feature_name]

            input_column_dt = str(input[feature_name].dtype)
            match_result = self.registered_datatype_vs_input_datatype(feature_dt, input_column_dt)
            if not match_result:
                datatype_error_list.append(
                    f" <{feature_name}> has datatype `{input_column_dt}`, expected datatype `{feature_dt}`"
                )

        return datatype_error_list

    def registered_names_with_input(
        self,
        registered_dataset_to_datatype: dict,
        registered_model_target: list,
        input_specified_features: list,
    ) -> list:
        error_columns = []
        for feature_name in registered_dataset_to_datatype.keys():
            if feature_name.lower() in registered_model_target:
                continue
            if feature_name not in input_specified_features:
                error_columns.append(feature_name)
        return error_columns

    def registered_model_target_with_input(
        self,
        registered_model_target: list,
        input_specified_features: list,
    ) -> list:
        error_columns = []
        for feature_name in registered_model_target:
            if feature_name not in input_specified_features:
                error_columns.append(feature_name)
        return error_columns

    def prediction_tabular_checks(
        self: object,
        input: pd.DataFrame,
        registered_dataset_to_datatype: dict,
        registered_model_target: list,
        registered_to_provided: dict = None,
    ) -> Tuple[bool, str]:
        print(" [info] Validating Name & Datatype match for provided columns vs registered.")
        # fetch just the user specified registered columns from `registered_to_provided``
        input_specified_registered_features = list(registered_to_provided.keys())

        error_columns = self.registered_names_with_input(
            registered_dataset_to_datatype,
            registered_model_target,
            input_specified_registered_features,
        )
        if len(error_columns) > 0:
            return True, (
                f"  ValidationError: In Predictions.Tabular No column(s) in <input> dataframe is mapped to following registered_feature(s): {error_columns}"
            )

        # Datatype check for registered features vs provided features
        feature_datatype_error_list = self.registered_datatype_with_input(
            registered_dataset_to_datatype,
            input,
            registered_model_target,
            registered_to_provided,
        )
        if len(feature_datatype_error_list) > 0:
            return (
                True,
                " ValidationError: Datatype Missmatch with registered `features` in `input_column` for columns "
                + str(feature_datatype_error_list),
            )

        return False, ""

    def explainations_checks(
        self, input: pd.DataFrame, explainations_col_list: list
    ) -> Tuple[bool, str]:
        """
        input:
            input - input dataframe
            explainations_col_list - list of explainations columns
        output:
            error_flag: True - if any validation failed else False
            error_message: error message
        """
        # check if explainations_col_list is not present in input.columns
        missing_columns = []
        for column in explainations_col_list:
            if column not in input.columns:
                missing_columns.append(column)

        if len(missing_columns) > 0:
            return (
                True,
                f"  ValidationError: following <explaination_input_column(s)> not found in <input> dataframe for columns: {missing_columns}",
            )

        # check if explainations_col_list has null values
        if input[explainations_col_list].isnull().any().any():
            return (
                True,
                "  ValidationError: <explaination_input_column(s)> has null values, <explaination_input_column(s)> must be NOT NULL",
            )

        # check if explainations_col_list float dataype
        if not all(input[explainations_col_list].dtypes == np.float64):
            return (
                True,
                "  ValidationError: <explaination_input_column(s)> has non float values, <explaination_input_column(s)> must be float",
            )
        return False, ""

    def exp_tabular_feature_with_registered(
        self,
        exp_tab_specified_feat: list,
        model_registered_feat: list,
        registered_model_target: list,
    ) -> list:
        """
        This function will check if the registered datatype with the input dataframe is same or not.
        """
        error_columns = []
        for feature_name in model_registered_feat:
            if feature_name.lower() in registered_model_target:
                continue
            if feature_name not in exp_tab_specified_feat:
                error_columns.append(feature_name)

        return error_columns


class BulkLogProcessing:
    def __init__(self):
        self.bulk_log_post_url = BULK_LOG_URL
        self.bulk_explain_post_url = BULK_EXPLAINATIONS_URL
        self.bulk_chunk_size = BULK_CHUNK_SIZE
        self.bulk_log_data_key = "bulk_logs"
        self.bulk_explain_data_key = "bulk_explainations"
        self.insertion_wait_time = 15
        pass

    # generate random 6 digit string for bulk log id
    def _generate_bulk_log_id_(self):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def _dataframe_chunks(
        self,
        dataframe: pd.DataFrame,
        headers: dict,
        model_details: dict,
        post_url: str,
        data_key: str,
    ) -> dict:
        # len of dataframe is greater than 10,000 divide into chunks of 10,000
        bulkID = self._generate_bulk_log_id_()
        if len(dataframe) > self.bulk_chunk_size:
            dataframe_chunks = np.array_split(dataframe, len(dataframe) / self.bulk_chunk_size)
            totalChunk = len(dataframe_chunks)
            for index, chunk in enumerate(dataframe_chunks):
                bulk_log_details = {
                    "bulkID": bulkID,
                    "currentChunk": index + 1,
                    "totalChunks": totalChunk,
                    "totalLogs": len(dataframe),
                }
                output = self._post_dataframe_to_censius_log(
                    chunk, headers, model_details, bulk_log_details, post_url, data_key
                )
        else:
            bulk_log_details = {
                "bulkID": bulkID,
                "currentChunk": 1,
                "totalChunks": 1,
                "totalLogs": len(dataframe),
            }
            output = self._post_dataframe_to_censius_log(
                dataframe, headers, model_details, bulk_log_details, post_url, data_key
            )
        return output

    def _post_dataframe_to_censius_log(
        self,
        dataframe: pd.DataFrame,
        headers: dict,
        model_details: dict,
        bulk_log_details: dict,
        post_url: str,
        data_key: str,
    ) -> dict:
        """
        This function will post the dataframe to censius log
        """
        # convert dataframe to json
        data = {data_key: list(dataframe.to_dict("records"))}
        payload = json.dumps({**data, **model_details, **bulk_log_details})

        # send dataframe to censius log
        try:
            response = requests.post(
                post_url,
                headers=headers,
                data=payload,
            )
        except Exception as e:
            return {"error": "Error while posting dataframe to censius log, " + str(e)}

        if response.status_code == 200:
            return response
        else:
            return response

    def process_bulk(
        self, input_dataframe: pd.DataFrame, headers: dict, model_details: dict
    ) -> dict:

        pool = ThreadPool(processes=1)
        background_worker_thread = pool.apply_async(
            self._dataframe_chunks,
            (
                input_dataframe,
                headers,
                model_details,
                self.bulk_log_post_url,
                self.bulk_log_data_key,
            ),
        )
        print(" [info] Bulk Log Processing Started - may take upto few sec.")

        # while time is less than 15 seconds
        # check if background_worker_thread is alive or not
        # if not alive then break the loop
        start_time = time.time()
        while True:
            if time.time() - start_time > self.insertion_wait_time:
                print(" [info] Bulk Log Processing Running in Background.")
                return {
                    "message": f"Processing: Batch file is of size {len(input_dataframe)}: Uploading in background."
                }
            if background_worker_thread.ready():
                thread_response = background_worker_thread.get()
                print(" [info] Bulk Log Processing Ended.")
                return thread_response

    def _reformat_explain_row(self, single_row: dict) -> dict:
        single_row = single_row.drop("log_id")
        return dict(zip(single_row.index, single_row.values))

    def _restructure_bulk_explain_df(self, input_dataframe: pd.DataFrame) -> pd.DataFrame:
        restructure_dataframe = pd.DataFrame(columns=["log_id", "shap_values"])
        input_dataframe["shap_values"] = input_dataframe.apply(
            lambda x: self._reformat_explain_row(x), axis=1
        )
        # copy log_id, shape_value column to restructure_dataframe
        restructure_dataframe[["log_id", "shap_values"]] = input_dataframe[
            ["log_id", "shap_values"]
        ]
        # delete input_dataframe
        del input_dataframe
        return restructure_dataframe

    def process_bulk_explain(
        self, input_dataframe: pd.DataFrame, headers: dict, model_details: dict
    ) -> dict:

        # restructure input_dataframe
        input_dataframe = self._restructure_bulk_explain_df(input_dataframe)
        pool = ThreadPool(processes=1)
        background_worker_thread = pool.apply_async(
            self._dataframe_chunks,
            (
                input_dataframe,
                headers,
                model_details,
                self.bulk_explain_post_url,
                self.bulk_explain_data_key,
            ),
        )
        print(" [info] Bulk Explaination Processing Started - may take upto few sec.")

        # while time is less than 15 seconds
        # check if background_worker_thread is alive or not
        # if not alive then break the loop
        start_time = time.time()
        while True:
            if time.time() - start_time > self.insertion_wait_time:
                print(" [info] Bulk Explaination Processing Running in Background.")
                return {
                    "message": f"Processing: Batch file is of size {len(input_dataframe)}: Uploading in background."
                }
            if background_worker_thread.ready():
                thread_response = background_worker_thread.get()
                print(" [info] Bulk Explaination Processing Ended.")
                return thread_response


def current_time():
    return time.time() * 1000


def check_time_format(timestamp):
    format = False
    ts = int(timestamp)
    try:
        dt.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        format = False
    except Exception as e:
        format = True

    return format


def extract_tabular_feature_map(tabular_feature_list):
    feature_map = {}
    for single_object in tabular_feature_list:
        feature_map[single_object["feature"]] = single_object["input_column"]
    return feature_map


def extract_features_details(prediction_tabular_input):
    """
    feature_column_map -
    `key` has feature from the Tabular Prediction.Tabular
    `value` has input_column from the Prediction.Tabular
    """
    feature_column_map = extract_tabular_feature_map(prediction_tabular_input)
    return feature_column_map


def bulk_col_renaming_map_for_preds(
    input_map: dict,
    registered_to_provided: dict,
    registered_dataset_to_datatype: dict,
    registered_model_target: list,
):
    for register_col in registered_dataset_to_datatype.keys():
        if register_col.lower() in registered_model_target:
            continue
        input_map[registered_to_provided[register_col]] = "feat_" + register_col.lower()
    return input_map


def bulk_col_renaming_map_for_exp(
    input_map: dict,
    registered_to_provided: dict,
    registered_dataset_to_datatype: dict,
    registered_model_target: list,
):
    for register_col in registered_dataset_to_datatype.keys():
        if register_col.lower() in registered_model_target:
            continue
        input_map[registered_to_provided[register_col]] = register_col.lower()
    return input_map


def make_post_request(url: string, headers: dict, payload: dict) -> dict:
    try:
        response = requests.post(
            url,
            headers=headers,
            data=payload,
            timeout=GENERAL_TIMEOUT,
        )
    # timeout exception
    except requests.exceptions.Timeout:
        return {"message": "NetworkTimeout: while making request to {}".format(url)}
    # other exception
    except requests.exceptions.RequestException as e:
        return {"message": "RequestError: {}".format(e)}

    if response.status_code == 200:
        return response
    else:
        return response
