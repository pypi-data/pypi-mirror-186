from benchling_api_client.v2.beta.api.rna_oligos import bulk_upsert_rna_oligos, upsert_rna_oligo
from benchling_api_client.v2.beta.models.oligo_upsert_request import OligoUpsertRequest
from benchling_api_client.v2.beta.models.rna_oligos_bulk_upsert_request import RnaOligosBulkUpsertRequest

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AsyncTaskLink, RnaOligo
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaRnaOligoService(BaseService):
    """
    V2-Beta RNA Oligos.

    RNA Oligos are short linear RNA sequences that can be attached as primers to full DNA sequences. Just like other
    entities, they support schemas, tags, and aliases.

    See https://benchling.com/api/v2-beta/reference#/RNA%20Oligos
    """

    @api_method
    def upsert(self, entity_registry_id: str, rna_oligo: OligoUpsertRequest) -> RnaOligo:
        """
        Create or modify a RNA Oligo.

        See https://benchling.com/api/v2-beta/reference#/RNA%20Oligos/upsertRNAOligo
        """
        response = upsert_rna_oligo.sync_detailed(
            client=self.client, entity_registry_id=entity_registry_id, json_body=rna_oligo
        )
        return model_from_detailed(response)

    @api_method
    def bulk_upsert(self, body: RnaOligosBulkUpsertRequest) -> AsyncTaskLink:
        """
        Bulk create or update RNA Oligos.

        See https://benchling.com/api/v2-beta/reference#/RNA%20Oligos/bulkUpsertRnaOligos
        """
        response = bulk_upsert_rna_oligos.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)
