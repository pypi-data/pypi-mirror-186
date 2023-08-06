"""Library defining the interface to the Registry."""
import json
import logging
from typing import List, Optional, cast

from rime_sdk.internal.config_parser import (
    convert_single_tabular_data_info_to_swagger,
    convert_single_tabular_pred_info_to_swagger,
    convert_tabular_model_info_to_swagger,
)
from rime_sdk.internal.rest_error_handler import RESTErrorHandler
from rime_sdk.swagger import swagger_client
from rime_sdk.swagger.swagger_client import ApiClient
from rime_sdk.swagger.swagger_client.models import (
    DatasetProjectIdUuidBody,
    ModelIdUuidDatasetIdBody,
    ModelProjectIdUuidBody,
    RegistryMetadata,
    RimeRegisterDatasetResponse,
    RimeRegisterModelResponse,
    RimeUUID,
)

logger = logging.getLogger(__name__)


class Registry:
    """Registry object wrapper with helpful methods for working with the Registry.

    Attributes:
        api_client: ApiClient
                The client used to query about the status of the job.
    """

    def __init__(self, api_client: ApiClient) -> None:
        """Create a new Registry wrapper object.

        Arguments:
            api_client: ApiClient
                The client used to query about the status of the job.
        """
        self._api_client = api_client

    def register_dataset(
        self,
        project_id: str,
        name: str,
        data_config: dict,
        integration_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
    ) -> str:
        """Register a new dataset."""
        data_info_swagger = convert_single_tabular_data_info_to_swagger(data_config)
        req = DatasetProjectIdUuidBody(
            project_id=RimeUUID(uuid=project_id), name=name, data_info=data_info_swagger
        )

        metadata_str: Optional[str] = None
        if metadata is not None:
            metadata_str = json.dumps(metadata)
        if tags is not None or metadata_str is not None:
            req.metadata = RegistryMetadata(tags=tags, extra_info=metadata_str)

        if integration_id is not None:
            req.integration_id = integration_id

        with RESTErrorHandler():
            api = swagger_client.RegistryServiceApi(self._api_client)
            res = api.registry_service_register_dataset(
                body=req, project_id_uuid=project_id,
            )

            res = cast(RimeRegisterDatasetResponse, res)

        return res.dataset_id

    def register_model(
        self,
        project_id: str,
        name: str,
        model_config: Optional[dict] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
        external_id: Optional[str] = None,
    ) -> str:
        """Register a new model."""
        req = ModelProjectIdUuidBody(project_id=RimeUUID(uuid=project_id), name=name,)

        if model_config is not None:
            model_info = convert_tabular_model_info_to_swagger(model_config)
            req.model_info = model_info

        metadata_str: Optional[str] = None
        if metadata:
            metadata_str = json.dumps(metadata)
        if tags or metadata_str:
            req.metadata = RegistryMetadata(tags=tags, extra_info=metadata_str)
        if external_id:
            req.external_id = external_id

        with RESTErrorHandler():
            api = swagger_client.RegistryServiceApi(self._api_client)
            res = api.registry_service_register_model(
                body=req, project_id_uuid=project_id,
            )

            res = cast(RimeRegisterModelResponse, res)

        return cast(RimeUUID, res.model_id).uuid

    def register_predictions(
        self,
        project_id: str,
        dataset_id: str,
        model_id: str,
        pred_config: dict,
        integration_id: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
    ) -> None:
        """Register a new prediction."""
        pred_info_swagger = convert_single_tabular_pred_info_to_swagger(pred_config)

        req = ModelIdUuidDatasetIdBody(
            project_id=RimeUUID(uuid=project_id),
            model_id=RimeUUID(uuid=model_id),
            pred_info=pred_info_swagger,
        )

        metadata_str: Optional[str] = None
        if metadata is not None:
            metadata_str = json.dumps(metadata)
        if tags is not None or metadata_str is not None:
            req.metadata = RegistryMetadata(tags=tags, extra_info=metadata_str)

        if integration_id is not None:
            req.integration_id = integration_id

        with RESTErrorHandler():
            api = swagger_client.RegistryServiceApi(self._api_client)
            _ = api.registry_service_register_prediction_set(
                body=req,
                project_id_uuid=project_id,
                model_id_uuid=model_id,
                dataset_id=dataset_id,
            )
