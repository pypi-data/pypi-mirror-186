from benchling_api_client.v2.stable.client import Client

from benchling_sdk.helpers.logging_helpers import log_stability_warning, StabilityLevel
from benchling_sdk.helpers.retry_helpers import RetryStrategy
from benchling_sdk.services.v2.base_service import BaseService
from benchling_sdk.services.v2.v2_alpha_service import V2AlphaService
from benchling_sdk.services.v2.v2_beta_service import V2BetaService
from benchling_sdk.services.v2.v2_stable_service import V2StableService


class V2Service(BaseService):
    """
    V2.

    Namespace containing support for the V2 Benchling API.
    """

    _v2_alpha_service: V2AlphaService
    _v2_beta_service: V2BetaService
    _v2_stable_service: V2StableService

    def __init__(self, client: Client, retry_strategy: RetryStrategy = RetryStrategy()):
        """
        Initialize a service.

        :param client: Underlying generated Client.
        :param retry_strategy: Retry strategy for failed HTTP calls
        """
        super().__init__(client, retry_strategy)
        self._v2_stable_service = V2StableService(client, retry_strategy)
        self._v2_alpha_service = V2AlphaService(client, retry_strategy)
        self._v2_beta_service = V2BetaService(client, retry_strategy)

    @property
    def alpha(self) -> V2AlphaService:
        """
        V2-alpha.

        Alpha endpoints have different stability guidelines than other stable endpoints.

        See https://benchling.com/api/v2-alpha/reference
        """
        log_stability_warning(StabilityLevel.ALPHA, package="v2.alpha")
        return self._v2_alpha_service

    @property
    def beta(self) -> V2BetaService:
        """
        V2-beta.

        Beta endpoints have different stability guidelines than other stable endpoints.

        See https://benchling.com/api/v2-beta/reference
        """
        log_stability_warning(StabilityLevel.BETA, package="v2.beta")
        return self._v2_beta_service

    @property
    def stable(self) -> V2StableService:
        """
        Stable.

        See https://docs.benchling.com/docs/stability#are-breaking-changes-made-to-the-api-or-events
        """
        return self._v2_stable_service
