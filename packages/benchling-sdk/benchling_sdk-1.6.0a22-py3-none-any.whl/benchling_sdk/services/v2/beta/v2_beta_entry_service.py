from benchling_api_client.v2.beta.api.entries import create_entry
from benchling_api_client.v2.beta.models.entry import Entry
from benchling_api_client.v2.beta.models.entry_create import EntryCreate

from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.services.v2.base_service import BaseService


class V2BetaEntryService(BaseService):
    """
    V2-Beta Entries.

    Entries are rich text documents that allow you to capture all of your experimental data in one place.

    https://benchling.com/api/v2-beta/reference#/Entries
    """

    @api_method
    def create_entry(self, entry: EntryCreate) -> Entry:
        """
        Create a notebook entry against beta endpoint, supporting initialTables.

        See https://benchling.com/api/v2-beta/reference#/Entries/createEntry
        """
        response = create_entry.sync_detailed(
            client=self.client,
            json_body=entry,
        )
        return model_from_detailed(response)
