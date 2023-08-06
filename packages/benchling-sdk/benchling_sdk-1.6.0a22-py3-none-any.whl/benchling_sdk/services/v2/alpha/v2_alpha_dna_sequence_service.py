from benchling_api_client.v2.alpha.api.dna_sequences import find_matching_regions_dna_sequences
from benchling_api_client.v2.alpha.api.dna_sequences.find_matching_regions_dna_sequences import (
    DnaSequencesFindMatchingRegion,
)

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.models import AsyncTaskLink
from benchling_sdk.services.v2.base_service import BaseService


class V2AlphaDnaSequenceService(BaseService):
    """
    V2-Alpha DNA Sequences.

    DNA sequences are the bread and butter of the Benchling Molecular Biology suite. On Benchling, these are
    comprised of a string of nucleotides and collections of other attributes, such as annotations and primers.

    See https://benchling.com/api/v2-alpha/reference#/DNA%20Sequences
    """

    @api_method
    def find_matching_regions(self, find_matching_region: DnaSequencesFindMatchingRegion) -> AsyncTaskLink:
        """
        Find matching regions for DNA sequences.

        See https://benchling.com/api/v2-alpha/reference#/DNA%20Sequences/findMatchingRegionsDnaSequences
        """
        response = find_matching_regions_dna_sequences.sync_detailed(
            client=self.client, json_body=find_matching_region
        )
        return model_from_detailed(response)
