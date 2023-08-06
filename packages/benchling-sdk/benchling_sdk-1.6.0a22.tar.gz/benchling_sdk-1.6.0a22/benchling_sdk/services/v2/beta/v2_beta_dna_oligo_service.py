from benchling_api_client.v2.beta.api.dna_oligos import bulk_upsert_dna_oligos, upsert_dna_oligo
from benchling_api_client.v2.beta.models.dna_oligos_bulk_upsert_request import DnaOligosBulkUpsertRequest
from benchling_api_client.v2.beta.models.oligo_upsert_request import OligoUpsertRequest

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AsyncTaskLink, DnaOligo
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaDnaOligoService(BaseService):
    """
    V2-Beta DNA Oligos.

    DNA Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other
    entities, they support schemas, tags, and aliases.

    See https://benchling.com/api/v2-beta/reference#/DNA%20Oligos
    """

    @api_method
    def upsert(self, entity_registry_id: str, dna_oligo: OligoUpsertRequest) -> DnaOligo:
        """
        Create or modify a DNA Oligo.

        See https://benchling.com/api/v2-beta/reference#/DNA%20Oligos/upsertDNAOligo
        """
        response = upsert_dna_oligo.sync_detailed(
            client=self.client, entity_registry_id=entity_registry_id, json_body=dna_oligo
        )
        return model_from_detailed(response)

    @api_method
    def bulk_upsert(self, body: DnaOligosBulkUpsertRequest) -> AsyncTaskLink:
        """
        Bulk create or update DNA Oligos.

        See https://benchling.com/api/v2-beta/reference#/DNA%20Oligos/bulkUpsertDnaOligos
        """
        response = bulk_upsert_dna_oligos.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)
