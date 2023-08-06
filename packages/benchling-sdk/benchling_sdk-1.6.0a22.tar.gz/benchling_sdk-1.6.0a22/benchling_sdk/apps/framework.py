from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, Type, TypeVar, Union

import attr
from benchling_api_client.v2.benchling_client import AuthorizationMethod
from benchling_api_client.webhooks.v0.alpha.models.webhook_envelope import (
    WebhookEnvelope as WebhookEnvelopeAlpha,
)
from benchling_api_client.webhooks.v0.beta.models.webhook_envelope import (
    WebhookEnvelope as WebhookEnvelopeBeta,
)
import httpx
from typing_extensions import Protocol

from benchling_sdk.apps import helpers
from benchling_sdk.apps.config.decryption_provider import BaseDecryptionProvider
from benchling_sdk.apps.config.dependencies import BaseDependencies
from benchling_sdk.benchling import (
    _DEFAULT_BASE_PATH,
    _DEFAULT_RETRY_STRATEGY,
    Benchling,
    BenchlingApiClientDecorator,
)
from benchling_sdk.helpers.logging_helpers import log_stability_warning, StabilityLevel
from benchling_sdk.helpers.retry_helpers import RetryStrategy

log_stability_warning(StabilityLevel.ALPHA)


ConfigType = TypeVar("ConfigType", bound=BaseDependencies)
AppType = TypeVar("AppType", bound="App")
AppWebhookType = Union[WebhookEnvelopeAlpha, WebhookEnvelopeBeta]


class MissingTenantUrlProviderError(Exception):
    """Error when a base URL is expected but unspecified."""

    pass


class MissingAppConfigTypeError(Exception):
    """Error when app config is expected but unspecified."""

    pass


class MalformedAppWebhookError(Exception):
    """Error when a webhook cannot be read by an app."""

    pass


class TenantUrlProvider(Protocol):
    """Return a base URL."""

    def __call__(self) -> str:
        """Return a base URL."""
        pass


def tenant_url_provider_static(tenant_url: str) -> TenantUrlProvider:
    """Create a provider function that always returns a static tenant URL."""

    def _url() -> str:
        return tenant_url

    return _url


def tenant_url_provider_lazy() -> TenantUrlProvider:
    """
    Create a provider function for app that will be initialized at runtime, such as from a webhook.

    Useful for when a base_url for Benchling is not known in advance but can be supplied at runtime.
    """

    def _deferred() -> str:
        raise MissingTenantUrlProviderError(
            "Unable to initialize base URL for tenant. Expected a URL to "
            "be provided at runtime but none was specified. Either specify "
            "a url provider or use TenantUrlProvider.static_url"
        )

    return _deferred


class BenchlingProvider(Protocol):
    """Return a Benchling instance."""

    def __call__(self, tenant_url_provider: TenantUrlProvider) -> Benchling:
        """Return a Benchling instance."""
        pass


class ConfigProvider(Protocol[ConfigType]):
    """Return a ConfigType instance."""

    def __call__(self, app: App[ConfigType]) -> ConfigType:
        """Return a ConfigType instance."""
        pass


def config_provider_static(config: ConfigType) -> ConfigProvider[ConfigType]:
    """Create a provider function that always returns a static app config."""

    def _static_config(app: App[ConfigType]) -> ConfigType:
        return config

    return _static_config


def config_provider_error_on_call() -> ConfigProvider[ConfigType]:
    """
    Create a provider function that raises an error.

    Used as a ConfigProvider for apps which don't support config and don't expect to invoke it.
    """

    def _error_on_call(app: App[ConfigType]) -> ConfigType:
        raise MissingAppConfigTypeError(
            "No app config class was defined for this app. "
            "Initialize an app with a ConfigProvider to use config."
        )

    return _error_on_call


def benchling_provider_static(benchling: Benchling) -> BenchlingProvider:
    """Create a provider function that always returns a static Benchling."""

    def _static_benchling(tenant_url_provider: TenantUrlProvider) -> Benchling:
        return benchling

    return _static_benchling


@attr.s(auto_attribs=True)
class App(Generic[ConfigType]):
    """
    App.

    See https://docs.benchling.com/docs/getting-started-benchling-apps

    Accepts providers as arguments to lazily initialize since some required attributes may not be
    known until runtime. Also allows for easier mocking in tests.
    """

    id: str
    _benchling_provider: BenchlingProvider
    _tenant_url_provider: TenantUrlProvider
    _config_provider: ConfigProvider[ConfigType] = attr.ib(default=config_provider_error_on_call)
    _benchling: Optional[Benchling] = attr.ib(default=None, init=False)
    _config: Optional[ConfigType] = attr.ib(default=None, init=False)

    @property
    def benchling(self) -> Benchling:
        """Return a Benchling instance for the App."""
        if self._benchling is None:
            self._benchling = self._benchling_provider(self._tenant_url_provider)
        return self._benchling

    @property
    def config(self) -> ConfigType:
        """
        Return config for the app.

        Apps which do not have config will raise MissingAppConfigTypeError.
        """
        if self._config is None:
            self._config = self._config_provider(self)
        return self._config

    def reset(self) -> None:
        """
        Reset the app.

        Generally clears all states and internal caches, which may cause subsequent invocations of the App
        to be expensive.
        """
        self._benchling = None
        if self._config is not None:
            self._config.invalidate_cache()

    def with_base_url(self: AppType, base_url: str) -> AppType:
        """Create a new copy of the app with a different base URL."""
        updated_tenant_url_provider = tenant_url_provider_static(base_url)
        modified_app = attr.evolve(self, tenant_url_provider=updated_tenant_url_provider)
        modified_app.reset()
        return modified_app

    def with_webhook(self: AppType, webhook: Union[dict, AppWebhookType]) -> AppType:
        """Create a new copy of the app with a different base URL provided by a webhook."""
        if isinstance(webhook, dict):
            if "baseUrl" not in webhook:
                raise MalformedAppWebhookError("The webhook specified did not contain a baseUrl")
            base_url = webhook["baseUrl"]
        else:
            base_url = webhook.base_url
        return self.with_base_url(base_url)

    def create_session_context(
        self: AppType,
        label: str,
        timeout_seconds: int,
        context_enter_handler: Optional[helpers.session_helpers.SessionContextEnterHandler[AppType]] = None,
        context_exit_handler: Optional[helpers.session_helpers.SessionContextExitHandler[AppType]] = None,
    ) -> helpers.session_helpers.SessionContextManager[AppType]:
        """
        Create Session Context.

        Create a new app session in Benchling.
        """
        # Avoid circular import + MyPy "is not defined" if using relative like above
        from benchling_sdk.apps.helpers.session_helpers import new_session_context

        return new_session_context(self, label, timeout_seconds, context_enter_handler, context_exit_handler)

    def continue_session_context(
        self: AppType,
        session_id: str,
        context_enter_handler: Optional[helpers.session_helpers.SessionContextEnterHandler[AppType]] = None,
        context_exit_handler: Optional[helpers.session_helpers.SessionContextExitHandler[AppType]] = None,
    ) -> helpers.session_helpers.SessionContextManager[AppType]:
        """
        Continue Session Context.

        Fetch an existing app session from Benchling and enter a context with it.
        """
        # Avoid circular import + MyPy "is not defined" if using relative like above
        from benchling_sdk.apps.helpers.session_helpers import continue_session_context

        return continue_session_context(self, session_id, context_enter_handler, context_exit_handler)

    @classmethod
    def init(
        cls: Type[AppType],
        id: str,
        benchling_provider: BenchlingProvider,
        tenant_url_provider: TenantUrlProvider,
        config_provider: Optional[ConfigProvider] = None,
    ) -> AppType:
        """
        Init.

        Initialize an app from its class.
        """
        required_config_provider: ConfigProvider[ConfigType] = (
            config_provider_error_on_call() if config_provider is None else config_provider
        )
        return cls(id, benchling_provider, tenant_url_provider, required_config_provider)


class BaseAppFactory(ABC, Generic[AppType, ConfigType]):
    """
    Base App Factory.

    Can be used as an alternative to init_app() for those who prefer to import a pre-defined app instance
    globally. Call create() on the factory to initialize an App.

    Users must subclass AppFactory and implement its abstract methods to create a subclass of App.
    """

    _app_type: Type[AppType]
    app_id: str
    benchling_provider: BenchlingProvider
    config_provider: ConfigProvider[ConfigType]

    def __init__(self, app_type: Type[AppType], app_id: str, config_type: Optional[Type[ConfigType]] = None):
        """Initialize App Factory."""
        self._app_type = app_type
        self.app_id = app_id

        # Initialize providers here to fail fast if there is a problem assembling them from the factory

        def benchling_provider(tenant_url_provider):
            tenant_url = tenant_url_provider()
            return Benchling(
                url=tenant_url,
                auth_method=self.auth_method,
                base_path=self.base_path,
                retry_strategy=self.retry_strategy,
                client_decorator=self.client_decorator,
                httpx_client=self.httpx_client,
            )

        if config_type is None:
            config_provider: ConfigProvider[ConfigType] = config_provider_error_on_call()
        else:

            def _config_provider(app: App[ConfigType]) -> ConfigType:
                # MyPy believes config_type can be None despite the conditional
                return config_type.from_app(app.benchling, app.id, self.decryption_provider)  # type: ignore

            config_provider = _config_provider

        self.benchling_provider = benchling_provider
        self.config_provider = config_provider

    def create(self) -> AppType:
        """Create an App instance from the factory."""
        return self._app_type.init(
            self.app_id, self.benchling_provider, self.tenant_url_provider, self.config_provider
        )

    @property
    @abstractmethod
    def auth_method(self) -> AuthorizationMethod:
        """
        Get an auth method to pass to Benchling.

        Must be implemented on all subclasses.
        """
        pass

    @property
    def tenant_url_provider(self) -> TenantUrlProvider:
        """
        Get a tenant URL provider that will provide a base URL for Benchling at runtime.

        By default, assumes that the App has no base_url and will be provided one later (e.g., from a webhook).
        Invoking app.benchling on an App in this state without setting a URL will raise an error.

        Use tenant_url_provider_static("https://myurl...") to specify a single URL.
        """
        return tenant_url_provider_lazy()

    # Benchling overrides

    @property
    def base_path(self) -> Optional[str]:
        """Get a base_path for Benchling."""
        return _DEFAULT_BASE_PATH

    @property
    def client_decorator(self) -> Optional[BenchlingApiClientDecorator]:
        """Get a BenchlingApiClientDecorator for Benchling."""
        return None

    @property
    def httpx_client(self) -> Optional[httpx.Client]:
        """Get a custom httpx Client for Benchling."""
        return None

    @property
    def retry_strategy(self) -> RetryStrategy:
        """Get a RetryStrategy for Benchling."""
        return _DEFAULT_RETRY_STRATEGY

    @property
    def decryption_provider(self) -> Optional[BaseDecryptionProvider]:
        """Get a decryption provider for decryption app config secrets."""
        return None


def init_app(
    app_id: str,
    benchling_provider: BenchlingProvider,
    tenant_url_provider: TenantUrlProvider,
    config_provider: Optional[ConfigProvider[ConfigType]] = None,
) -> App[ConfigType]:
    """
    Init App.

    Initializes a Benchling App with a series of functions to provide App dependencies at runtime.
    """
    if config_provider is None:
        config_provider = config_provider_error_on_call()
    return App(app_id, benchling_provider, tenant_url_provider, config_provider)


def init_static_app(
    app_id: str, benchling: Benchling, config: Optional[ConfigType] = None
) -> App[ConfigType]:
    """
    Init Static App.

    Initializes a Benchling App with static values. Suitable for apps that communicate with a single URL.
    """
    tenant_url_provider = tenant_url_provider_static(benchling.client.base_url)
    benchling_provider = benchling_provider_static(benchling)
    config_provider = config_provider_error_on_call() if config is None else config_provider_static(config)
    return init_app(app_id, benchling_provider, tenant_url_provider, config_provider)
