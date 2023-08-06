from benchling_api_client.v2.beta.api.aa_sequences import (
    bulk_upsert_aa_sequences,
    find_matching_regions_aa_sequences,
    upsert_aa_sequence,
)
from benchling_api_client.v2.beta.models.aa_sequence_upsert import AaSequenceUpsert
from benchling_api_client.v2.beta.models.aa_sequences_bulk_upsert_request import AaSequencesBulkUpsertRequest
from benchling_api_client.v2.beta.models.aa_sequences_find_matching_region import (
    AaSequencesFindMatchingRegion,
)

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AaSequence, AsyncTaskLink
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaAaSequenceService(BaseService):
    """
    V2-Beta AA Sequences.

    AA Sequences are the working units of cells that make everything run (they help make structures, catalyze
    reactions and allow for signaling - a kind of internal cell communication). On Benchling, these are comprised
    of a string of amino acids and collections of other attributes, such as annotations.

    See https://benchling.com/api/v2-beta/reference#/AA%20Sequences
    """

    @api_method
    def upsert(self, entity_registry_id: str, aa_sequence: AaSequenceUpsert) -> AaSequence:
        """
        Create or modify an Amino Acid Sequence.

        See https://benchling.com/api/v2-beta/reference#/AA%20Sequences/upsertAaSequence
        """
        response = upsert_aa_sequence.sync_detailed(
            client=self.client, entity_registry_id=entity_registry_id, json_body=aa_sequence
        )
        return model_from_detailed(response)

    @api_method
    def bulk_upsert(self, body: AaSequencesBulkUpsertRequest) -> AsyncTaskLink:
        """
        Bulk create or update AA sequences.

        See https://benchling.com/api/v2-beta/reference#/AA%20Sequences/bulkUpsertAASequences
        """
        response = bulk_upsert_aa_sequences.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)

    @api_method
    def find_matching_regions(self, find_matching_region: AaSequencesFindMatchingRegion) -> AsyncTaskLink:
        """
        Find matching regions for AA sequences.

        See https://benchling.com/api/v2-beta/reference#/AA%20Sequences/findMatchingRegionsAaSequences
        """
        response = find_matching_regions_aa_sequences.sync_detailed(
            client=self.client, json_body=find_matching_region
        )
        return model_from_detailed(response)
