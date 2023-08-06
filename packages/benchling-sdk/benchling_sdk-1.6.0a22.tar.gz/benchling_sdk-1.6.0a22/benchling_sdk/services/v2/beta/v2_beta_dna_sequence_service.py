from benchling_api_client.v2.beta.api.dna_sequences import bulk_upsert_dna_sequences, upsert_dna_sequence
from benchling_api_client.v2.beta.models.dna_sequence_upsert_request import DnaSequenceUpsertRequest
from benchling_api_client.v2.beta.models.dna_sequences_bulk_upsert_request import (
    DnaSequencesBulkUpsertRequest,
)

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AsyncTaskLink, DnaSequence
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaDnaSequenceService(BaseService):
    """
    V2-Beta DNA Sequences.

    DNA sequences are the bread and butter of the Benchling Molecular Biology suite. On Benchling, these are
    comprised of a string of nucleotides and collections of other attributes, such as annotations and primers.

    See https://benchling.com/api/v2-beta/reference#/DNA%20Sequences
    """

    @api_method
    def upsert(self, entity_registry_id: str, dna_sequence: DnaSequenceUpsertRequest) -> DnaSequence:
        """
        Create or modify a DNA sequence.

        See https://benchling.com/api/v2-beta/reference#/DNA%20Sequences/upsertDNASequence
        """
        response = upsert_dna_sequence.sync_detailed(
            client=self.client, entity_registry_id=entity_registry_id, json_body=dna_sequence
        )
        return model_from_detailed(response)

    @api_method
    def bulk_upsert(self, body: DnaSequencesBulkUpsertRequest) -> AsyncTaskLink:
        """
        Bulk create or update DNA sequences.

        See https://benchling.com/api/v2-beta/reference#/DNA%20Sequences/bulkUpsertDnaSequences
        """
        response = bulk_upsert_dna_sequences.sync_detailed(client=self.client, json_body=body)
        return model_from_detailed(response)
