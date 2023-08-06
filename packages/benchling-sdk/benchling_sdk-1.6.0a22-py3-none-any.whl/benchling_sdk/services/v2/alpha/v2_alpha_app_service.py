from typing import List, Optional

from benchling_api_client.v2.alpha.api.apps import (
    create_session,
    get_benchling_app_manifest,
    get_session_by_id,
    list_sessions,
    put_benchling_app_manifest,
    update_session,
)
from benchling_api_client.v2.alpha.models.benchling_app_manifest_alpha import BenchlingAppManifestAlpha
from benchling_api_client.v2.alpha.models.session import Session
from benchling_api_client.v2.alpha.models.session_create import SessionCreate
from benchling_api_client.v2.alpha.models.session_update import SessionUpdate
from benchling_api_client.v2.alpha.models.sessions_paginated_list import SessionsPaginatedList
from benchling_api_client.v2.stable.types import Response

from benchling_sdk.errors import AppSessionClosedError, raise_for_status
from benchling_sdk.helpers.decorators import api_method
from benchling_sdk.helpers.pagination_helpers import NextToken, PageIterator
from benchling_sdk.helpers.response_helpers import model_from_detailed
from benchling_sdk.helpers.serialization_helpers import none_as_unset
from benchling_sdk.services.v2.base_service import BaseService


class V2AlphaAppService(BaseService):
    """
    V2-Alpha Apps.

    Create and manage Apps on your tenant.

    https://benchling.com/api/v2-alpha/reference?stability=not-available#/Apps
    """

    @api_method
    def get_manifest(self, app_id: str) -> BenchlingAppManifestAlpha:
        """
        Get app manifest.

        See https://benchling.com/api/v2-alpha/reference?stability=la/Apps/getBenchlingAppManifest
        """
        response = get_benchling_app_manifest.sync_detailed(client=self.client, app_id=app_id)
        return model_from_detailed(response)

    @api_method
    def update_manifest(self, app_id: str, manifest: BenchlingAppManifestAlpha) -> BenchlingAppManifestAlpha:
        """
        Update an app manifest.

        See https://benchling.com/api/v2-alpha/reference?stability=la#/Apps/putBenchlingAppManifest
        """
        response = put_benchling_app_manifest.sync_detailed(
            client=self.client, app_id=app_id, yaml_body=manifest
        )
        return model_from_detailed(response)

    # Sessions

    @api_method
    def create_session(self, session: SessionCreate) -> Session:
        """
        Create a new session. Sessions cannot be archived once created.

        See https://benchling.com/api/v2-alpha/reference?availability=not-available#/Apps/createSession
        """
        response = create_session.sync_detailed(
            client=self.client,
            json_body=session,
        )
        return model_from_detailed(response)

    @api_method
    def get_session_by_id(self, session_id: str) -> Session:
        """
        Get a session.

        See https://benchling.com/api/v2-alpha/reference?availability=not-available#/Apps/getSessionById
        """
        response = get_session_by_id.sync_detailed(
            client=self.client,
            id=session_id,
        )
        return model_from_detailed(response)

    @api_method
    def update_session(self, session_id: str, session: SessionUpdate) -> Session:
        """
        Update session.

        Raises AppSessionClosedError if trying to update a Session that has already been closed.

        See https://benchling.com/api/v2-alpha/reference?availability=not-available#/Apps/updateSession
        """
        response = update_session.sync_detailed(
            client=self.client,
            id=session_id,
            json_body=session,
        )
        return model_from_detailed(response, error_types=[AppSessionClosedError])

    @api_method
    def _sessions_page(
        self,
        app_id: Optional[str] = None,
        next_token: NextToken = None,
        page_size: Optional[int] = None,
    ) -> Response[SessionsPaginatedList]:
        response = list_sessions.sync_detailed(
            client=self.client,
            app_id=none_as_unset(app_id),
            next_token=none_as_unset(next_token),
            page_size=none_as_unset(page_size),
        )
        raise_for_status(response)
        return response  # type: ignore

    def list_sessions(
        self, app_id: Optional[str] = None, page_size: Optional[int] = None
    ) -> PageIterator[Session]:
        """
        List all sessions.

        See https://benchling.com/api/v2-alpha/reference?availability=not-available#/Apps/listSessions
        """

        def api_call(next_token: NextToken) -> Response[SessionsPaginatedList]:
            return self._sessions_page(
                app_id=app_id,
                next_token=next_token,
                page_size=page_size,
            )

        def results_extractor(body: SessionsPaginatedList) -> Optional[List[Session]]:
            return body.sessions

        return PageIterator(api_call, results_extractor)
