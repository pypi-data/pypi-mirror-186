"""Parse json config to swagger."""
import copy
import json
from copy import deepcopy
from typing import Any, Optional, Tuple, Union, cast

import pandas as pd

from rime_sdk.swagger.swagger_client.models import (
    CliconfigConnectionInfo,
    CliconfigHuggingFaceSingleDataLoadingInfo,
    CliconfigImagesCLIConfig,
    CliconfigImagesDataInfo,
    CliconfigImagesSingleDataFileInfo,
    CliconfigImagesSingleDataInfo,
    CliconfigNLPCLIConfig,
    CliconfigNLPDataInfo,
    CliconfigNLPSingleDataFileInfo,
    CliconfigNLPSingleDataInfo,
    CliconfigPredictionParams,
    CliconfigRankingInfo,
    CliconfigSingleDataCollectorInfo,
    CliconfigSingleDataLoadingInfo,
    CliconfigSingleDeltaLakeInfo,
    CliconfigSingleHuggingFaceDataInfo,
    CliconfigSinglePredictionInfo,
    CliconfigSinglePredInfo,
    CliconfigTabularCLIConfig,
    CliconfigTabularDataInfo,
    CliconfigTabularPredictionInfo,
    CliconfigTabularSingleDataFileInfo,
    CliconfigTabularSingleDataInfo,
    CliconfigTabularSingleDataInfoParams,
    CliconfigTypedCLIConfig,
    CliconfigUnstructuredEmbeddingInfo,
    CliconfigUnstructuredSingleDataInfoParams,
    ModelHuggingFaceModelInfo,
    ModelLoaderModelInfo,
    ModelModelInfo,
    ModelPathModelInfo,
    RimeDataType,
    RimeImagesIncrementalConfig,
    RimeNLPIncrementalConfig,
    RimeTabularIncrementalConfig,
    RimeTypedIncrementalConfig,
)

DEFAULT_DO_SAMPLING = True


def _formatted_time_to_int_time(loaded_timestamp: Union[int, str]) -> int:
    """Convert formatted time to integer time."""
    if isinstance(loaded_timestamp, int):
        return loaded_timestamp
    # TODO: change function once we replace protobuf start_time/end_time
    # int type with protobuf Timestamp type
    # TODO: consolidate timestamp format with rime-engine
    # NOTE: we use pd.to_datetime instead of datetime.strptime because
    # to_datetime allows a subset of values (e.g. just year and month)
    timestamp = pd.to_datetime(loaded_timestamp)
    return int(timestamp.timestamp())


def convert_pred_params_to_swagger(
    config: dict,
) -> Optional[CliconfigPredictionParams]:
    """Convert prediction params dictionary to swagger."""
    proto_names = CliconfigPredictionParams.swagger_types
    param_config = {name: config.pop(name) for name in proto_names if name in config}
    if len(param_config) == 0:
        return None
    return CliconfigPredictionParams(**param_config)


def convert_tabular_params_to_swagger(
    config: dict,
) -> Optional[CliconfigTabularSingleDataInfoParams]:
    """Convert tabular params dictionary to swagger."""
    field_names = CliconfigTabularSingleDataInfoParams.swagger_types
    param_config = {name: config.pop(name) for name in field_names if name in config}
    if "sample" not in param_config:
        param_config["sample"] = DEFAULT_DO_SAMPLING
    if len(param_config) == 0:
        return None
    if "loading_kwargs" in param_config and param_config["loading_kwargs"] is not None:
        param_config["loading_kwargs"] = json.dumps(param_config["loading_kwargs"])
    if "ranking_info" in param_config and param_config["ranking_info"] is not None:
        param_config["ranking_info"] = CliconfigRankingInfo(
            **param_config["ranking_info"]
        )
    if "intersections" in param_config and param_config["intersections"] is not None:
        param_config["intersections"] = param_config["intersections"]
    for param in ["text_features", "image_features"]:
        unstructured_feats = param_config.get(param)
        if unstructured_feats is not None and not isinstance(unstructured_feats, list):
            raise ValueError(
                f"`{param}` must be type `List[str]`. Got '{unstructured_feats}'."
            )
    return CliconfigTabularSingleDataInfoParams(**param_config)


def process_connector_info_to_swagger(
    config: dict, config_type: str,
) -> Tuple[str, Any]:
    """Process config connector info into a connection swagger and its swagger key."""
    if config_type == "default":
        swagger_key = "single_data_file_info"
        swagger: Any = CliconfigTabularSingleDataFileInfo(
            file_name=config.pop("file_name"),
        )
    elif config_type == "custom":
        loader_kwargs_json = ""
        if "loader_kwargs" in config and "loader_kwargs_json" in config:
            raise ValueError(
                "Got both loader_kwargs and loader_kwargs_json, "
                "but only one should be provided."
            )
        elif "loader_kwargs" in config:
            # This can be None, but we don't want to set, so check first.
            _val = config.pop("loader_kwargs")
            if _val is not None:
                loader_kwargs_json = json.dumps(_val)
        elif "loader_kwargs_json" in config:
            # This can be None, but we don't want to set, so check first.
            _val = config.pop("loader_kwargs_json")
            if _val is not None:
                loader_kwargs_json = _val
        else:
            pass
        swagger_key = "single_data_loading_info"
        swagger = CliconfigSingleDataLoadingInfo(
            load_path=config.pop("load_path"),
            load_func_name=config.pop("load_func_name"),
            loader_kwargs_json=loader_kwargs_json,
        )
    elif config_type == "data_collector":
        start_time = _formatted_time_to_int_time(config.pop("start_time"))
        end_time = _formatted_time_to_int_time(config.pop("end_time"))
        swagger_key = "single_data_collector_info"
        swagger = CliconfigSingleDataCollectorInfo(
            start_time=start_time, end_time=end_time
        )
    elif config_type == "delta_lake":
        start_time = _formatted_time_to_int_time(config.pop("start_time"))
        end_time = _formatted_time_to_int_time(config.pop("end_time"))
        swagger_key = "single_delta_lake_info"
        swagger = CliconfigSingleDeltaLakeInfo(
            table_name=config.pop("table_name"),
            start_time=start_time,
            end_time=end_time,
            time_col=config.pop("time_col"),
        )
    elif config_type == "huggingface":
        swagger_key = "single_huggingface_info"
        swagger = CliconfigSingleHuggingFaceDataInfo(
            dataset_uri=config.pop("dataset_uri"),
            split_name=config.pop("split_name", None),
            loading_params_json=json.dumps(config.pop("loading_params", None)),
        )
    else:
        raise ValueError(f"Unsupported config type: {config_type}")
    if config:
        raise ValueError(
            f"Found parameters in the data info config that do not belong: {config}"
        )
    return swagger_key, swagger


def convert_single_tabular_pred_info_to_swagger(
    config: dict,
) -> Optional[CliconfigSinglePredInfo]:
    """Convert a dictionary to single pred info swagger message."""
    if config is None or len(config) == 0:
        return None
    pred_params_dict = config.pop("pred_params", dict())
    pred_params = convert_pred_params_to_swagger(pred_params_dict)

    connector_info = config.pop("connector_info")
    config_type = connector_info.pop("type", "default")
    field, conn_swagger = process_connector_info_to_swagger(connector_info, config_type)
    connection_info = CliconfigConnectionInfo()
    setattr(connection_info, field, conn_swagger)

    proto = CliconfigSinglePredInfo(
        pred_params=pred_params, connection_info=connection_info
    )
    return proto


def convert_single_tabular_data_info_to_swagger(
    config: dict,
) -> CliconfigTabularSingleDataInfo:
    """Convert a dictionary to single tabular data info swagger message."""
    if "connector_info" in config:
        tabular_params_dict = config.pop("tabular_params", dict())
        tabular_params = convert_tabular_params_to_swagger(tabular_params_dict)
        connector_info = config.pop("connector_info")
        config_type = connector_info.pop("type", "default")
        field, conn_swagger = process_connector_info_to_swagger(
            connector_info, config_type
        )
    else:
        tabular_params = convert_tabular_params_to_swagger(config)
        config_type = config.pop("type", "default")
        field, conn_swagger = process_connector_info_to_swagger(config, config_type)

    swagger = CliconfigTabularSingleDataInfo(single_params=tabular_params)
    setattr(swagger, field, conn_swagger)
    return swagger


def convert_default_tabular_data_info_to_split(
    config: dict,
) -> Tuple[CliconfigTabularSingleDataInfo, CliconfigTabularSingleDataInfo]:
    """Convert default TabularDataInfo config to split ref and eval SingleDataInfo swaggers."""
    try:
        ref_config = {"file_name": config.pop("ref_path")}
        eval_config = {"file_name": config.pop("eval_path")}
    except KeyError:
        raise ValueError("Missing ref_path and/or eval_path specification")
    if "ref_pred_path" in config:
        ref_config["pred_path"] = config.pop("ref_pred_path")
    if "eval_pred_path" in config:
        eval_config["pred_path"] = config.pop("eval_pred_path")
    ref_config.update(config)
    eval_config.update(config)
    ref_data_info = convert_single_tabular_data_info_to_swagger(ref_config)
    eval_data_info = convert_single_tabular_data_info_to_swagger(eval_config)
    return ref_data_info, eval_data_info


def convert_tabular_pred_info_to_swagger(
    config: dict,
) -> Optional[CliconfigTabularPredictionInfo]:
    """Convert a dictionary to tabular pred info swagger message."""
    if config is None or len(config) == 0:
        return None
    config_type = config.get("type", "split")
    if config_type == "split":
        eval_pred_info = convert_single_tabular_pred_info_to_swagger(
            config["eval_info"]
        )
        ref_pred_info = convert_single_tabular_pred_info_to_swagger(config["ref_info"])
    else:
        raise ValueError(f"Unsupported config type: {config['type']}")
    return CliconfigTabularPredictionInfo(
        ref_info=ref_pred_info, eval_info=eval_pred_info
    )


def convert_tabular_model_info_to_swagger(config: dict) -> ModelModelInfo:
    """Convert a dictionary to tabular model info swagger message."""
    model_type = config.pop("type", "default")

    try:
        if model_type == "default":
            model_info_swagger = ModelModelInfo(
                path_info=ModelPathModelInfo(path=config.pop("path"))
            )
        elif model_type == "model_loader":
            model_path = config.pop("path")
            model_params_str = json.dumps(config.pop("params"))
            model_info_swagger = ModelModelInfo(
                loader_info=ModelLoaderModelInfo(
                    path=model_path, params=model_params_str
                )
            )
        elif model_type == "huggingface":
            model_uri = config.pop("model_uri")
            config_str = json.dumps(config)
            model_info_swagger = ModelModelInfo(
                hugging_face_info=ModelHuggingFaceModelInfo(
                    model_uri=model_uri, kwargs=config_str
                )
            )
        else:
            raise ValueError(
                "model_info type in config should be one of `default`, "
                f"`model_loader`, `huggingface`. Got {model_type}"
            )
    except KeyError:
        raise ValueError(f"Invalid config: {config}")

    return model_info_swagger


def convert_tabular_data_info_to_swagger(config: dict) -> CliconfigTabularDataInfo:
    """Convert a dictionary to tabular data info swagger message."""
    config_type = config.get("type", "default")

    if config_type == "default":
        ref_data_info, eval_data_info = convert_default_tabular_data_info_to_split(
            config
        )
    elif config_type == "custom":
        # TabularDataLoadingInfo
        eval_config = config.copy()
        if "ref_pred_path" in config:
            config["pred_path"] = config.pop("ref_pred_path")
            del eval_config["ref_pred_path"]
        if "eval_pred_path" in config:
            eval_config["pred_path"] = eval_config.pop("eval_pred_path")
            del config["eval_pred_path"]
        config["load_func_name"] = "get_ref_data"
        ref_data_info = convert_single_tabular_data_info_to_swagger(config)
        eval_config["load_func_name"] = "get_eval_data"
        eval_data_info = convert_single_tabular_data_info_to_swagger(eval_config)
    elif config_type == "split":
        eval_data_info = convert_single_tabular_data_info_to_swagger(
            config["eval_data_info"]
        )
        ref_data_info = convert_single_tabular_data_info_to_swagger(
            config["ref_data_info"]
        )
    else:
        raise ValueError(f"Unsupported config type: {config['type']}")

    return CliconfigTabularDataInfo(
        ref_data_info=ref_data_info, eval_data_info=eval_data_info
    )


def convert_tabular_config_to_swagger(config: dict) -> CliconfigTabularCLIConfig:
    """Convert config to tabular swagger."""
    # pop to remove from original config dict
    data_info = convert_tabular_data_info_to_swagger(config.pop("data_info"))
    pred_info = convert_single_tabular_pred_info_to_swagger(
        config.pop("pred_info", dict())
    )
    swagger = CliconfigTabularCLIConfig(data_info=data_info, pred_info=pred_info)
    config_field_names = CliconfigTabularCLIConfig.swagger_types
    for name in config_field_names:
        if name in config and config[name] is not None:
            # pop to remove from original config dict
            setattr(swagger, name, json.dumps(config.pop(name)))
    return swagger


def convert_single_unstructured_params_to_swagger(
    config: dict,
) -> Optional[CliconfigUnstructuredSingleDataInfoParams]:
    """Convert unstructured params dictionary to proto."""
    complicated_fields = {"prediction_info", "embeddings"}
    proto_names = [
        field
        for field in CliconfigUnstructuredSingleDataInfoParams.swagger_types
        if field not in complicated_fields
    ]
    param_config = {name: config.pop(name) for name in proto_names if name in config}
    if "sample" not in param_config:
        param_config["sample"] = DEFAULT_DO_SAMPLING
    if "prediction_info" in config and config["prediction_info"] is not None:
        single_pred_info = CliconfigSinglePredictionInfo(**config["prediction_info"])
        param_config["prediction_info"] = single_pred_info
    if "embeddings" in config and config["embeddings"] is not None:
        embeddings = [
            CliconfigUnstructuredEmbeddingInfo(**info) for info in config["embeddings"]
        ]
        param_config["embeddings"] = embeddings
    return (
        CliconfigUnstructuredSingleDataInfoParams(**param_config)
        if param_config
        else None
    )


def convert_single_nlp_data_info_to_swagger(config: dict) -> CliconfigNLPSingleDataInfo:
    """Convert a dictionary to single nlp data info swagger message."""
    unstructured_params = convert_single_unstructured_params_to_swagger(config)
    config_type = config.pop("type", "default")
    if config_type == "default":
        return CliconfigNLPSingleDataInfo(
            single_data_file_info=CliconfigNLPSingleDataFileInfo(
                file_name=config["file_name"]
            ),
            single_params=unstructured_params,
        )
    elif config_type == "custom":
        loader_kwargs_json = ""
        if "loader_kwargs" in config and config["loader_kwargs"] is not None:
            loader_kwargs_json = json.dumps(config["loader_kwargs"])
        if "loader_kwargs_json" in config and config["loader_kwargs_json"] is not None:
            loader_kwargs_json = config["loader_kwargs_json"]
        single_data_loading_info = CliconfigSingleDataLoadingInfo(
            load_path=config["load_path"],
            load_func_name=config["load_func_name"],
            loader_kwargs_json=loader_kwargs_json,
        )
        return CliconfigNLPSingleDataInfo(
            single_data_loading_info=single_data_loading_info,
            single_params=unstructured_params,
        )
    elif config_type == "huggingface":
        huggingface_single_info = CliconfigHuggingFaceSingleDataLoadingInfo(
            dataset_uri=config["dataset_uri"],
            split_name=config["split_name"],
            text_key=config.get("text_key", "text"),
            loading_params_json=json.dumps(config.get("loading_params")),
        )
        if "label_key" in config:
            huggingface_single_info.label_key = json.dumps(config["label_key"])
        if config.get("text_pair_key") is not None:
            huggingface_single_info.text_pair_key = config["text_pair_key"]
        return CliconfigNLPSingleDataInfo(
            huggingface_single_data_loading_info=huggingface_single_info,
            single_params=unstructured_params,
        )
    elif config_type == "delta_lake":
        start_time = _formatted_time_to_int_time(config["start_time"])
        end_time = _formatted_time_to_int_time(config["end_time"])
        single_delta_lake_info_swagger = CliconfigSingleDeltaLakeInfo(
            table_name=config["table_name"],
            start_time=start_time,
            end_time=end_time,
            time_col=config["time_col"],
        )
        return CliconfigNLPSingleDataInfo(
            single_delta_lake_info=single_delta_lake_info_swagger,
            single_params=unstructured_params,
        )
    elif config_type == "data_collector":
        start_time = _formatted_time_to_int_time(config["start_time"])
        end_time = _formatted_time_to_int_time(config["end_time"])
        single_data_collector_info_swagger = CliconfigSingleDataCollectorInfo(
            start_time=start_time, end_time=end_time
        )
        if unstructured_params is not None and getattr(
            unstructured_params, "prediction_info"
        ):
            raise ValueError(
                "'prediction_info' cannot be specified with data config"
                f" of type {config_type}"
            )
        return CliconfigNLPSingleDataInfo(
            single_data_collector_info=single_data_collector_info_swagger,
            single_params=unstructured_params,
        )
    else:
        raise ValueError(f"Unsupported config type: {config_type}")


def _get_default_nlp_data_info_split_configs(config: dict) -> Tuple[dict, dict]:
    """Get default NLP config type data info split configs."""
    ref_config = {"file_name": config.pop("ref_path")}
    eval_config = {"file_name": config.pop("eval_path")}
    ref_config.update(config)
    eval_config.update(config)
    return ref_config, eval_config


def _get_custom_nlp_data_info_split_configs(config: dict) -> Tuple[dict, dict]:
    """Get custom NLP config type data info split configs."""
    ref_config = {"load_func_name": "get_ref_data"}
    eval_config = {"load_func_name": "get_eval_data"}
    ref_config.update(config)
    eval_config.update(config)
    return ref_config, eval_config


def _get_huggingface_data_info_split_configs(config: dict) -> Tuple[dict, dict]:
    """Get huggingface config type data info split configs."""
    ref_config, eval_config = {}, {}
    ref_config["split_name"] = config.pop("ref_split", "train")
    eval_config["split_name"] = config.pop("eval_split", "test")
    if "eval_label_key" in config:
        eval_config["label_key"] = config.pop("eval_label_key")
    ref_config.update(config)
    if "label_key" in config:
        del config["label_key"]
    eval_config.update(config)
    return ref_config, eval_config


def convert_nlp_data_info_to_swagger(config: dict) -> CliconfigNLPDataInfo:
    """Convert config to swagger message for nlp data."""
    config_type = config.get("type", "default")
    if config_type == "default":
        ref_config, eval_config = _get_default_nlp_data_info_split_configs(config)
    elif config_type == "custom":
        ref_config, eval_config = _get_custom_nlp_data_info_split_configs(config)
    elif config_type == "huggingface":
        ref_config, eval_config = _get_huggingface_data_info_split_configs(config)
    elif config_type == "split":
        ref_config = config["ref_data_info"]
        eval_config = config["eval_data_info"]
    else:
        raise ValueError(f"Unsupported config type: {config['type']}")
    ref_data_info = convert_single_nlp_data_info_to_swagger(ref_config)
    eval_data_info = convert_single_nlp_data_info_to_swagger(eval_config)
    return CliconfigNLPDataInfo(
        ref_data_info=ref_data_info, eval_data_info=eval_data_info
    )


def convert_nlp_config_to_swagger(config: dict) -> CliconfigNLPCLIConfig:
    """Convert config to nlp swagger."""
    # pop to remove from original config dict
    data_info = convert_nlp_data_info_to_swagger(config.pop("data_info"))
    swagger = CliconfigNLPCLIConfig(data_info=data_info)
    config_names = CliconfigNLPCLIConfig.swagger_types
    for name in config_names:
        if name in config and config[name] is not None:
            # pop to remove from original config dict
            setattr(swagger, name, json.dumps(config.pop(name)))
    return swagger


def convert_single_images_data_info_to_swagger(
    config: dict,
) -> CliconfigImagesSingleDataInfo:
    """Convert a dictionary to single image data info swagger message."""
    unstructured_params = convert_single_unstructured_params_to_swagger(config)
    config_type = config.pop("type", "default")
    if config_type == "default":
        swagger = CliconfigImagesSingleDataInfo(
            single_data_file_info=CliconfigImagesSingleDataFileInfo(
                file_name=config["file_name"]
            ),
            single_params=unstructured_params,
        )
    else:
        raise ValueError(f"Unsupported config type: {config_type}")
    if "load_path" in config and config["load_path"] is not None:
        swagger.load_path = config["load_path"]
    return swagger


def convert_images_data_info_to_swagger(config: dict) -> CliconfigImagesDataInfo:
    """Convert config to swagger message for images data."""
    config_type = config.get("type", "default")
    if config_type == "default":
        ref_config = copy.deepcopy(config)
        ref_config["file_name"] = config["ref_path"]
        eval_config = copy.deepcopy(config)
        eval_config["file_name"] = config["eval_path"]
        eval_data_info = convert_single_images_data_info_to_swagger(eval_config)
        ref_data_info = convert_single_images_data_info_to_swagger(ref_config)
    elif config_type == "split":
        eval_data_info = convert_single_images_data_info_to_swagger(
            config["eval_data_info"]
        )
        ref_data_info = convert_single_images_data_info_to_swagger(
            config["ref_data_info"]
        )
    else:
        raise ValueError(f"Unsupported config type: {config['type']}")
    return CliconfigImagesDataInfo(
        ref_data_info=ref_data_info, eval_data_info=eval_data_info
    )


def convert_images_config_to_swagger(config: dict) -> CliconfigImagesCLIConfig:
    """Convert config to images swagger."""
    # pop to remove from original config dict
    data_info = convert_images_data_info_to_swagger(config.pop("data_info"))
    swagger = CliconfigImagesCLIConfig(data_info=data_info)
    config_names = CliconfigImagesCLIConfig.swagger_types
    for name in config_names:
        if name in config and config[name] is not None:
            # pop to remove from original config dict
            setattr(swagger, name, json.dumps(config.pop(name)))
    return swagger


def _update_key_names(config: dict) -> dict:
    """Update key names in config for backwards compatibility."""
    key_names = [
        ("test_config", "tests_config"),
        ("subset_profiling_config", "subset_profiling_info"),
    ]
    if "workspace_name" in config:
        config.pop("workspace_name")
    for old_name, new_name in key_names:
        if old_name in config:
            if new_name in config:
                raise ValueError(
                    f"Both {old_name} and {new_name} cannot be present in the config."
                )
            config[new_name] = config.pop(old_name)
    return config


def convert_config_to_swagger(_config: dict, data_type: str) -> CliconfigTypedCLIConfig:
    """Convert a dictionary config to swagger."""
    config = deepcopy(_config)
    config = _update_key_names(config)
    try:
        if data_type == RimeDataType.TABULAR:
            tabular_config = convert_tabular_config_to_swagger(config)
            swagger = CliconfigTypedCLIConfig(tabular_config=tabular_config)
        elif data_type == RimeDataType.NLP:
            nlp_config = convert_nlp_config_to_swagger(config)
            swagger = CliconfigTypedCLIConfig(nlp_config=nlp_config)
        elif data_type == RimeDataType.IMAGES:
            images_config = convert_images_config_to_swagger(config)
            swagger = CliconfigTypedCLIConfig(images_config=images_config)
        else:
            raise ValueError(f"Unknown data type: {data_type}")
    except KeyError:
        raise ValueError(f"Invalid config: {config}")

    for name in config:
        if name not in config or config[name] is None:
            continue
        if name == "tests_config":
            setattr(swagger, name, json.dumps(config[name]))
        else:
            try:
                setattr(swagger, name, config[name])
            except AttributeError:
                raise ValueError(
                    f"Config parsing fails on attribute '{name}'. "
                    "Make sure the data type aligns with the data provided. "
                    "Please specify data_type = 'tabular', 'nlp', or 'images'. "
                )
    return swagger


def convert_tabular_incremental_config_to_swagger(
    config: dict,
) -> RimeTabularIncrementalConfig:
    """Convert a dictionary incremental config to tabular incremental swagger."""
    try:
        if "eval_data_info" in config:
            eval_data_info = convert_single_tabular_data_info_to_swagger(
                config["eval_data_info"]
            )
            swagger = RimeTabularIncrementalConfig(eval_data_info=eval_data_info)

            if "eval_pred_info" in config:
                eval_pred_info = cast(
                    CliconfigSinglePredInfo,
                    convert_single_tabular_pred_info_to_swagger(
                        config["eval_pred_info"]
                    ),
                )
                setattr(swagger, "eval_pred_info", eval_pred_info)
        elif "eval_path" in config:
            data_file_info = CliconfigTabularSingleDataFileInfo(
                file_name=config["eval_path"],
            )
            tabular_params = CliconfigTabularSingleDataInfoParams(
                timestamp_col=config["timestamp_col"]
            )
            if "eval_pred_path" in config:
                tabular_params.pred_path = config["eval_pred_path"]

            eval_data_info = CliconfigTabularSingleDataInfo(
                single_data_file_info=data_file_info, single_params=tabular_params
            )
            swagger = RimeTabularIncrementalConfig(eval_data_info=eval_data_info)
        else:
            raise ValueError(f"Invalid incremental config: {config}")
    except KeyError:
        raise ValueError(f"Invalid incremental config: {config}")

    return swagger


def convert_nlp_incremental_config_to_swagger(config: dict) -> RimeNLPIncrementalConfig:
    """Convert a dictionary incremental config to nlp incremental swagger."""
    if "eval_data_info" in config:
        eval_data_info = convert_single_nlp_data_info_to_swagger(
            config["eval_data_info"]
        )
        swagger = RimeNLPIncrementalConfig(eval_data_info=eval_data_info)
    elif "eval_path" in config:
        # if config is in the old format, convert to use singledatainfo format
        data_file_info = CliconfigNLPSingleDataFileInfo(file_name=config["eval_path"])
        eval_data_info = CliconfigNLPSingleDataInfo(
            single_data_file_info=data_file_info
        )
        # NOTE: if eval_pred_path specified, create corresponding prediction_info
        # in eval_data_info
        if "eval_pred_path" in config and config["eval_pred_path"] is not None:
            eval_data_info.single_params = CliconfigUnstructuredSingleDataInfoParams(
                prediction_info=CliconfigSinglePredictionInfo(
                    path=config["eval_pred_path"]
                )
            )

        swagger = RimeNLPIncrementalConfig(eval_data_info=eval_data_info)
    else:
        raise ValueError(f"Invalid incremental config: {config}")
    return swagger


def convert_images_incremental_config_to_swagger(
    config: dict,
) -> RimeImagesIncrementalConfig:
    """Convert a dictionary incremental config to image incremental swagger."""
    if "eval_data_info" in config:
        eval_data_info = convert_single_images_data_info_to_swagger(
            config["eval_data_info"]
        )
        swagger = RimeImagesIncrementalConfig(eval_data_info=eval_data_info)
    elif "eval_path" in config:
        # if config is in the old format, convert to use singledatainfo format
        data_file_info = CliconfigImagesSingleDataFileInfo(
            file_name=config["eval_path"]
        )
        eval_data_info = CliconfigImagesSingleDataInfo(
            single_data_file_info=data_file_info
        )
        # NOTE: if eval_pred_path specified, create corresopnding prediction_info
        # in eval_data_info
        if "eval_pred_path" in config and config["eval_pred_path"] is not None:
            eval_data_info.single_params = CliconfigUnstructuredSingleDataInfoParams(
                prediction_info=CliconfigSinglePredictionInfo(
                    path=config["eval_pred_path"]
                )
            )

        swagger = RimeImagesIncrementalConfig(eval_data_info=eval_data_info)
    else:
        raise ValueError(f"Invalid incremental config: {config}")
    return swagger


def convert_incremental_config_to_swagger(
    _config: dict, data_type: str
) -> RimeTypedIncrementalConfig:
    """Convert a dictionary incremental config to swagger."""
    config = deepcopy(_config)
    # TODO: implement other modalities too
    if data_type == RimeDataType.TABULAR:
        tabular_config = convert_tabular_incremental_config_to_swagger(config)
        swagger = RimeTypedIncrementalConfig(tabular_incremental_config=tabular_config)
    elif data_type == RimeDataType.NLP:
        nlp_config = convert_nlp_incremental_config_to_swagger(config)
        swagger = RimeTypedIncrementalConfig(nlp_incremental_config=nlp_config)
    elif data_type == RimeDataType.IMAGES:
        images_config = convert_images_incremental_config_to_swagger(config)
        swagger = RimeTypedIncrementalConfig(images_incremental_config=images_config)
    else:
        raise ValueError(f"Unknown data type: {data_type}")

    if "include_model" in config:
        setattr(swagger, "include_model", config["include_model"])
    return swagger
