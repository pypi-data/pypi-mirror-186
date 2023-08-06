from benchling_api_client.v2.beta.api.custom_entities import bulk_upsert_custom_entities, upsert_custom_entity
from benchling_api_client.v2.beta.models.custom_entities_bulk_upsert_request import (
    CustomEntitiesBulkUpsertRequest,
)
from benchling_api_client.v2.beta.models.custom_entity_upsert_request import CustomEntityUpsertRequest

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AsyncTaskLink, CustomEntity
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaCustomEntityService(BaseService):
    """
    V2-Beta Custom Entities.

    Benchling supports custom entities for biological entities that are neither sequences or proteins. Custom
    entities must have an entity schema set and can have both schema fields and custom fields.

    See https://benchling.com/api/v2-beta/reference#/Custom%20Entities
    """

    @api_method
    def upsert(self, entity_registry_id: str, entity: CustomEntityUpsertRequest) -> CustomEntity:
        """
        Create or modify a custom entity.

        See https://benchling.com/api/v2-beta/reference#/Custom%20Entities/upsertCustomEntity
        """
        response = upsert_custom_entity.sync_detailed(
            client=self.client, entity_registry_id=entity_registry_id, json_body=entity
        )
        return model_from_detailed(response)

    @api_method
    def bulk_upsert(self, body: CustomEntitiesBulkUpsertRequest) -> AsyncTaskLink:
        """
        Bulk update custom entities.

        See https://benchling.com/api/v2-beta/reference#/Custom%20Entities/bulkUpsertCustomEntities
        """
        response = bulk_upsert_custom_entities.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)
