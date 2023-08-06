from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import cast, Dict, Generic, List, Optional, Tuple, Type, TypeVar, Union

from benchling_api_client.v2.extensions import UnknownType
from ordered_set import OrderedSet
from typing_extensions import Protocol

from benchling_sdk.apps.config.decryption_provider import BaseDecryptionProvider
from benchling_sdk.apps.config.scalars import (
    DEFAULT_SCALAR_DEFINITIONS,
    scalar_definition_from_field_type,
    ScalarConfigItemType,
    ScalarDefinition,
    ScalarType,
)
from benchling_sdk.benchling import Benchling
from benchling_sdk.models import (
    AppConfigItem,
    ArrayElementAppConfigItem,
    BooleanAppConfigItem,
    DateAppConfigItem,
    DatetimeAppConfigItem,
    EntitySchemaAppConfigItem,
    Field,
    FieldAppConfigItem,
    FloatAppConfigItem,
    GenericApiIdentifiedAppConfigItem,
    InaccessibleResource,
    IntegerAppConfigItem,
    JsonAppConfigItem,
    LinkedAppConfigResourceSummary,
    ListAppConfigurationItemsSort,
    SecureTextAppConfigItem,
    TextAppConfigItem,
)


class MissingDependencyError(Exception):
    """
    Missing dependency error.

    Indicates a dependency was missing from app config.
    For instance, no dependency with that name was in the list.
    """

    pass


class UnsupportedDependencyError(Exception):
    """
    Unsupported dependency error.

    The manifest and configuration specified a dependency which the SDK is incapable of handling yet.
    """

    pass


class MissingScalarDefinitionError(Exception):
    """
    Missing scalar definition error.

    The manifest and configuration specified a scalar type which the SDK does not know how to translate
    to Python values yet.
    """

    pass


class InaccessibleAppConfigResourceError(Exception):
    """
    Inaccessible app config resource error.

    A resource was linked in app config, but the permissions do not allow access to it. Most likely happens
    when an app lacks the necessary permissions.
    """

    pass


ConfigItemPath = Tuple[str, ...]

# Everything from AppConfigItem except UnknownType
ConfigurationReference = Union[
    ArrayElementAppConfigItem,
    DateAppConfigItem,
    DatetimeAppConfigItem,
    JsonAppConfigItem,
    EntitySchemaAppConfigItem,
    FieldAppConfigItem,
    BooleanAppConfigItem,
    IntegerAppConfigItem,
    FloatAppConfigItem,
    GenericApiIdentifiedAppConfigItem,
    SecureTextAppConfigItem,
    TextAppConfigItem,
]

ConfigWithLinkedResource = Union[
    EntitySchemaAppConfigItem,
    FieldAppConfigItem,
    GenericApiIdentifiedAppConfigItem,
]

ScalarConfigReference = Union[
    BooleanAppConfigItem,
    DateAppConfigItem,
    DatetimeAppConfigItem,
    FloatAppConfigItem,
    IntegerAppConfigItem,
    JsonAppConfigItem,
    SecureTextAppConfigItem,
    TextAppConfigItem,
]

D = TypeVar("D", bound="BaseDependencies")
F = TypeVar("F", bound="BaseField")


class ConfigProvider(Protocol):
    """
    Config provider.

    Provides a BenchlingAppConfiguration.
    """

    def config(self) -> List[ConfigurationReference]:
        """Implement to provide a Benchling app configuration."""
        pass


class BenchlingConfigProvider(ConfigProvider):
    """
    Benchling Config provider.

    Provides a BenchlingAppConfiguration retrieved from Benchling's API.
    """

    _client: Benchling
    _app_id: str

    def __init__(self, client: Benchling, app_id: str):
        """
        Initialize Benchling Config Provider.

        :param client: A configured Benchling instance for making API calls.
        :param app_id: The app_id from which to retrieve configuration.
        """
        self._client = client
        self._app_id = app_id

    def config(self) -> List[ConfigurationReference]:
        """Provide a Benchling app configuration from Benchling's APIs."""
        app_pages = self._client.apps.list_app_configuration_items(
            app_id=self._app_id,
            page_size=100,
            # TODO BNCH-57121 this sort probably needs to be created_at but not currently available to us
            sort=ListAppConfigurationItemsSort.MODIFIEDATASC,
        )

        # Eager load all config items for now since we don't yet have a way of lazily querying by path
        all_config_pages = list(app_pages)
        # Punt on UnknownType for now as apps using manifests with new types could lead to unpredictable results
        all_config_items = [
            _supported_config_item(config_item) for page in all_config_pages for config_item in page
        ]

        return all_config_items


class StaticConfigProvider(ConfigProvider):
    """
    Static Config provider.

    Provides a BenchlingAppConfiguration from a static declaration. Useful for mocking or testing.
    """

    _configuration_items: List[ConfigurationReference]

    def __init__(self, configuration_items: List[ConfigurationReference]):
        """
        Initialize Static Config Provider.

        :param configuration_items: The configuration items to return.
        """
        self._configuration_items = configuration_items

    def config(self) -> List[ConfigurationReference]:
        """Provide Benchling app configuration items from a static reference."""
        return self._configuration_items


class DependencyLinkStore(object):
    """
    Dependency Link Store.

    Marshalls an app configuration from the configuration provider into an indexable structure.
    Only retrieves app configuration once unless its cache is invalidated.
    """

    _configuration_provider: ConfigProvider
    _configuration: Optional[List[ConfigurationReference]] = None
    _configuration_map: Optional[Dict[ConfigItemPath, ConfigurationReference]] = None
    _array_path_row_names: Dict[Tuple[str, ...], OrderedSet[str]] = dict()

    def __init__(self, configuration_provider: ConfigProvider):
        """
        Initialize Dependency Link Store.

        :param configuration_provider: A ConfigProvider that will be invoked to provide the
        underlying config from which to organize dependency links.
        """
        self._configuration_provider = configuration_provider
        self._array_path_row_names = dict()

    @classmethod
    def from_app(cls, client: Benchling, app_id: str) -> DependencyLinkStore:
        """
        From App.

        Instantiate a DependencyLinkStore from an app_id and a configured Benchling instance. Preferred to
        using the class's constructor.
        """
        config_provider = BenchlingConfigProvider(client, app_id)
        return cls(config_provider)

    @property
    def configuration(self) -> List[ConfigurationReference]:
        """
        Get the underlying configuration.

        Return the raw, stored configuration. Can be used if the provided accessors are inadequate
        to find particular configuration items.
        """
        if not self._configuration:
            self._configuration = self._configuration_provider.config()
        return self._configuration

    @property
    def configuration_path_map(self) -> Dict[ConfigItemPath, ConfigurationReference]:
        """
        Config links.

        Return a map of configuration item paths to their corresponding configuration items.
        """
        if not self._configuration_map:
            self._configuration_map = {tuple(item.path): item for item in self.configuration}
        return self._configuration_map

    def config_by_path(self, path: List[str]) -> Optional[ConfigurationReference]:
        """
        Config by path.

        Find an app config item by its exact path match, if it exists. Does not search partial paths.
        """
        # Since we eager load all config now, we know that missing path means it's not configured in Benchling
        # Later if we support lazy loading, we'll need to differentiate what's in our cache versus missing
        return self.configuration_path_map.get(tuple(path))

    def config_keys_by_path(self, path: List[str]) -> OrderedSet[str]:
        """
        Config keys by path.

        Find a set of app config keys at the specified path, if any. Does not return keys that are nested
        beyond the current level. Particularly useful for finding config array row names.

        For instance, given paths:
        ["One", "Two"]
        ["One", "Two", "Three"]
        ["One", "Two", "Four"]
        ["One", "Two", "Three", "Five"]
        ["Zero", "One", "Two", "Three"]

        The expected return from this method when path=["One", "Two"] is a set {"Three", "Four"}.
        """
        # Convert path to tuple, as list is not hashable for dict keys
        path_tuple = tuple(path)
        if path_tuple not in self._array_path_row_names:
            self._array_path_row_names[path_tuple] = OrderedSet(
                [
                    config_item.value
                    # Use the list instead of configuration_map to preserve order
                    for config_item in self.configuration
                    if isinstance(config_item, ArrayElementAppConfigItem)
                    # The +1 is the name of the array row
                    and len(config_item.path) >= len(path) + 1
                    # Ignoring flake8 error E203 because black keeps putting in whitespace padding :
                    and config_item.path[0 : len(path_tuple)] == path  # noqa: E203
                    and config_item.value is not None
                ]
            )
        return self._array_path_row_names[path_tuple]

    def invalidate_cache(self) -> None:
        """
        Invalidate Cache.

        Will force retrieval of configuration from the ConfigProvider the next time the link store is accessed.
        """
        self._configuration = None
        self._configuration_map = None
        self._array_path_row_names = dict()


class HasAppConfigItem(Protocol):
    """
    Has App Config Item.

    A mixin for typing to assert that a class has an optional app config item attribute.
    """

    @property
    def path(self) -> List[str]:
        """Return the path requested by the manifest."""
        pass

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        pass


class HasApiIdentifiedAppConfigItem(Protocol):
    """
    Has Api Identified App Config Item.

    A mixin for typing to assert that a class has an optional app config item attribute.
    That app config item must have a linked_resource property.
    """

    @property
    def path(self) -> List[str]:
        """Return the path requested by the manifest."""
        pass

    @property
    def config_item(self) -> Optional[ConfigWithLinkedResource]:
        """Return the underlying app config item, if present. App config item must have linked_resource."""
        pass


class HasScalarDefinition(Protocol):
    """
    Has Scalar Definition.

    A mixin for typing to assert that a particular class has scalar attributes.
    """

    @property
    def path(self) -> List[str]:
        """Return the path requested by the manifest."""
        pass

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        pass

    @property
    def definition(self) -> Optional[ScalarDefinition]:
        """Return the scalar definition, allowing for conversion to Python types."""
        pass


class HasConfigWithDecryptionProvider(Protocol):
    """
    Has Config With Decryption Provider.

    A mixin for typing to assert that a particular class has a decryption provider and config.
    """

    @property
    def path(self) -> List[str]:
        """Return the path requested by the manifest."""
        pass

    @property
    def config_item(self) -> Optional[ConfigurationReference]:
        """Return the underlying app config item, if present."""
        pass

    @property
    def decryption_provider(self) -> Optional[BaseDecryptionProvider]:
        """Return the decryption provider."""
        pass


class RequiredLinkedResourceDependencyMixin:
    """
    Required Linked Resource Dependency Mixin.

    A mixin for easily accessing attributes from linked_resource for an app config item which is required and
    should always be present. Should only be mixed in with HasApiIdentifiedAppConfigItem
    """

    @property
    def id(self: HasApiIdentifiedAppConfigItem) -> str:
        """Return the API ID of the linked configuration."""
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        # config_item.value and linked_resource.id are the same for now,
        # so we can eschew inaccessible resource checking
        return self.config_item.value

    @property
    def name(self: HasApiIdentifiedAppConfigItem) -> str:
        """Return the name of the linked configuration.

        Raises InaccessibleAppConfigResourceError if the app does not have permission to the linked resource.
        """
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        if isinstance(self.config_item.linked_resource, InaccessibleResource):
            raise InaccessibleAppConfigResourceError(
                f'No permissions to the linked resource "{self.config_item.value}" referenced by {self.path}'
            )
        # Required for type checking
        assert isinstance(
            self.config_item.linked_resource, LinkedAppConfigResourceSummary
        ), f"Expected linked resource from app config item but got {type(self.config_item.linked_resource)}"
        return self.config_item.linked_resource.name


class OptionalLinkedResourceDependencyMixin:
    """
    Optional Linked Resource Dependency Mixin.

    A mixin for easily accessing attributes from linked_resource for an app config item which is optional and
    may not be present. Should only be mixed in with HasApiIdentifiedAppConfigItem
    """

    @property
    def id(self: HasApiIdentifiedAppConfigItem) -> Optional[str]:
        """Return the API ID of the linked configuration, if present."""
        # config_item.value and linked_resource.id are the same for now,
        # so we can eschew inaccessible resource checking
        if self.config_item is not None and self.config_item.value is not None:
            return self.config_item.value
        return None

    @property
    def name(self: HasApiIdentifiedAppConfigItem) -> Optional[str]:
        """Return the name of the linked configuration, if present.

        Raises InaccessibleAppConfigResourceError if the app does not have permission to the linked resource.
        """
        if self.config_item is not None and self.config_item.value is not None:
            if isinstance(self.config_item.linked_resource, InaccessibleResource):
                raise InaccessibleAppConfigResourceError(
                    f'No permissions to the linked resource "{self.config_item.value}" referenced by {self.path}'
                )
            # Required for type checking
            assert isinstance(
                self.config_item.linked_resource, LinkedAppConfigResourceSummary
            ), f"Expected linked resource from app config item but got {type(self.config_item.linked_resource)}"
            return self.config_item.linked_resource.name
        return None


class OptionalValueMixin:
    """
    Optional Value Mixin.

    A mixin for accessing a value which is optional and may not be present. Should
    only be mixed in with HasAppConfigItem or another class that provides the `self.config_item` attribute.
    """

    @property
    def value(self: HasAppConfigItem) -> Optional[str]:
        """Return the value of the app config item, if present."""
        if self.config_item and self.config_item.value:
            return str(self.config_item.value)
        return None


class RequiredValueMixin:
    """
    Required Value Mixin.

    A mixin for accessing a value which is required and should always be present. Should
    only be mixed in with HasAppConfigItem or another class that provides the `self.config_item` attribute.
    """

    @property
    def value(self: HasAppConfigItem) -> str:
        """Return the value of the app config item."""
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        return str(self.config_item.value)


class RequiredScalarDependencyMixin(Generic[ScalarType]):
    """
    Require Scalar Config.

    A mixin for accessing a scalar config which is required and should always be present.
    Should only be mixed in with HasScalarDefinition.
    """

    @property
    def value(self: HasScalarDefinition) -> ScalarType:
        """Return the value of the scalar."""
        if self.definition:
            assert (
                self.config_item is not None and self.config_item.value is not None
            ), f"The app config item {self.path} is not set in Benchling"
            optional_typed_value = self.definition.from_str(value=str(self.config_item.value))
            assert optional_typed_value is not None
            return optional_typed_value
        raise MissingScalarDefinitionError(f"No definition registered for scalar config {self.path}")

    @property
    def value_str(self: HasScalarDefinition) -> str:
        """Return the value of the scalar as a string."""
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        # Booleans are currently specified as str in the spec but are bool at runtime in JSON
        return str(self.config_item.value)


class OptionalScalarDependencyMixin(Generic[ScalarType]):
    """
    Optional Scalar Config.

    A mixin for accessing a scalar config which is optional and may not be present.
    Should only be mixed in with HasScalarDefinition.
    """

    @property
    def value(self: HasScalarDefinition) -> Optional[ScalarType]:
        """Return the value of the scalar, if present."""
        if self.config_item and self.config_item.value:
            if self.definition:
                return self.definition.from_str(value=str(self.config_item.value))
            raise MissingScalarDefinitionError(f"No definition registered for scalar config {self.path}")
        return None

    @property
    def value_str(self: HasScalarDefinition) -> Optional[str]:
        """Return the value of the scalar as a string, if present."""
        if self.config_item and self.config_item.value:
            return str(self.config_item.value)
        return None


class RequiredSecureTextDependencyMixin(RequiredScalarDependencyMixin[str]):
    """
    Require Secure Text.

    A mixin for accessing a secure text config which is required and should always be present.
    Should only be mixed in with SecureTextConfig.
    """

    def decrypted_value(self: HasConfigWithDecryptionProvider) -> str:
        """
        Decrypted value.

        Decrypts a secure_text dependency's encrypted value into plain text.
        """
        assert (
            self.config_item is not None and self.config_item.value is not None
        ), f"The app config item {self.path} is not set in Benchling"
        assert (
            self.decryption_provider is not None
        ), f"The app config item {self.config_item} cannot be decrypted because no DecryptionProvider was set"
        return self.decryption_provider.decrypt(str(self.config_item.value))


class OptionalSecureTextDependencyMixin(OptionalScalarDependencyMixin[str]):
    """
    Optional Secure Text.

    A mixin for accessing a secure text config which is optional and may not be present.
    Should only be mixed in with SecureTextConfig.
    """

    def decrypted_value(self: HasConfigWithDecryptionProvider) -> Optional[str]:
        """
        Decrypted value.

        Decrypts a secure_text dependency's encrypted value into plain text, if present.
        """
        if self.config_item and self.config_item.value:
            assert (
                self.decryption_provider is not None
            ), f"The app config item {self.config_item} cannot be decrypted because no DecryptionProvider was set"
            return self.decryption_provider.decrypt(str(self.config_item.value))
        return None


@dataclass
class BaseConfigNode:
    """
    Base Config Node.

    A node in a graph of related config items, referencing its parent.

    All nodes should have a parent, which may be BaseDependencies, but not all nodes represent an AppConfigItem
    in Benchling.
    """

    parent: Union[BaseDependencies, BaseConfigNode]

    def context(self) -> BaseDependencies:
        """Return the dependency class at the root of the dependency graph."""
        if isinstance(self.parent, BaseDependencies):
            return self.parent
        return self.parent.context()

    def full_path(self) -> List[str]:
        """Return the full path of the current node, inheriting from all parents."""
        parent_path = self.parent.full_path() if isinstance(self.parent, BaseConfigNode) else []
        # Fields and options classes typically don't define paths
        last_path = getattr(self, "path", [])
        return parent_path + last_path


@dataclass
class BaseConfigItem(BaseConfigNode):
    """
    Base Config Item.

    A reference to any config item.
    """

    config_item: Optional[ConfigurationReference]


@dataclass
class ApiConfigItem(BaseConfigItem):
    """
    API Config Item.

    A reference to a config item for a Benchling object referencable by the API.
    """

    config_item: Optional[ConfigWithLinkedResource]


class BaseField(ABC, Field, Generic[ScalarType]):
    """
    Base Field.

    Provides additional accessors on top of the OpenAPI Field model.
    """

    @classmethod
    def from_field(cls: Type[F], field: Optional[Field]) -> F:
        """
        From Field.

        Create a new instance from an existing field.
        """
        if field:
            return cls(
                value=field.value,
                display_value=field.display_value,
                is_multi=field.is_multi,
                text_value=field.text_value,
                type=field.type,
            )
        return cls(value=None)

    @property
    def scalar_definition(self) -> ScalarDefinition[ScalarType]:
        """
        Scalar Definition.

        Returns a scalar definition for parsing a concrete type from a field.
        Override to implement custom deserialization.
        """
        return scalar_definition_from_field_type(self.type)


class RequiredField(BaseField, Generic[ScalarType]):
    """
    Required Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with required, single valued fields.
    """

    @dataclass
    class _RequiredFieldTyped:
        base_field: RequiredField

        @property
        def value(self) -> ScalarType:
            """
            Typed Value.

            Returns the value of the field typed as it's specified in an app manifest.
            """
            # Can be None in the case of someone changing config
            typed_value = self.base_field.scalar_definition.from_str(value=str(self.base_field.value))
            assert typed_value is not None
            return typed_value

        @property
        def display_value(self) -> str:
            """
            Display Value.

            Return the field's display value as a string.
            """
            assert self.base_field.display_value is not None
            return self.base_field.display_value

    @property
    def typed(self) -> _RequiredFieldTyped:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._RequiredFieldTyped(self)


class OptionalField(BaseField, Generic[ScalarType]):
    """
    Optional Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with optional, single valued fields.
    """

    @dataclass
    class _OptionalFieldTyped:
        base_field: OptionalField

        @property
        def value(self) -> Optional[ScalarType]:
            """
            Typed Value.

            Returns the value of the field typed as it's specified in an app manifest, if the field is present.
            """
            if self.base_field.value:
                field_value = str(self.base_field.value)
                return self.base_field.scalar_definition.from_str(value=field_value)
            return None

        @property
        def display_value(self) -> Optional[str]:
            """
            Display Value.

            Return the field's display value as a string, if present.
            """
            # Check to ensure linked before display_value, which will raise NotPresentError on unlinked
            if self.base_field.value is None:
                return None
            return None if self.base_field.display_value == "" else self.base_field.display_value

    @property
    def typed(self) -> _OptionalFieldTyped:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._OptionalFieldTyped(self)


class RequiredMultiValueField(BaseField, Generic[ScalarType]):
    """
    Required Multi Value Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with required, multi-valued fields.
    """

    @dataclass
    class _RequiredMultiValueFieldType:
        base_field: RequiredMultiValueField

        @property
        def value(self) -> List[ScalarType]:
            """
            Typed Value.

            Returns the list of values in the field typed as it's specified in an app manifest.
            """
            typed_values: List[ScalarType] = [
                cast(ScalarType, self.base_field.scalar_definition.from_str(value=str(field_value)))
                for field_value in cast(List[str], self.base_field.value)
                if field_value is not None
            ]
            return typed_values

        @property
        def display_value(self) -> str:
            """
            Display Value.

            Return the field's display value as a string.
            """
            # We could try to return display value as List[str] for multi-valued fields, except comma is
            # an unreliable delimiter since the names within each value can contain it
            assert self.base_field.display_value is not None
            return self.base_field.display_value

    @property
    def typed(self) -> _RequiredMultiValueFieldType:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._RequiredMultiValueFieldType(self)


class OptionalMultiValueField(BaseField, Generic[ScalarType]):
    """
    Optional Multi Value Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with optional, multi-valued fields.
    """

    @dataclass
    class _OptionalMultiValueFieldType:
        base_field: OptionalMultiValueField

        @property
        def value(self) -> Optional[List[ScalarType]]:
            """
            Typed Value.

            Returns the list of values in the field typed as it's specified in an app manifest, if present.
            """
            if self.base_field.value:
                typed_values: List[ScalarType] = [
                    cast(ScalarType, self.base_field.scalar_definition.from_str(value=str(field_value)))
                    for field_value in cast(List[str], self.base_field.value)
                    if field_value is not None
                ]
                return typed_values
            return None

        @property
        def display_value(self) -> Optional[str]:
            """
            Display Value.

            Return the field's display value as a string, if present.
            """
            # Check to ensure linked before display_value, which will raise NotPresentError on unlinked
            if self.base_field.value is None:
                return None
            return None if self.base_field.display_value == "" else self.base_field.display_value

    @property
    def typed(self) -> _OptionalMultiValueFieldType:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._OptionalMultiValueFieldType(self)


class RequiredSingleOrMultiValueField(BaseField, Generic[ScalarType]):
    """
    Required Single Or Multi Value Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with required fields where isMulti is unset.
    """

    @dataclass
    class _RequiredSingleOrMultiValueFieldTyped:
        base_field: RequiredSingleOrMultiValueField

        @property
        def value(self) -> Union[ScalarType, List[ScalarType]]:
            """
            Typed Value.

            Returns the value in the field typed as it's specified in an app manifest.
            """
            if isinstance(self.base_field.value, list):
                typed_values: List[ScalarType] = [
                    cast(ScalarType, self.base_field.scalar_definition.from_str(value=str(field_value)))
                    for field_value in cast(List[str], self.base_field.value)
                    if field_value is not None
                ]
                return typed_values
            field_value = str(self.base_field.value)
            return cast(ScalarType, self.base_field.scalar_definition.from_str(value=field_value))

        @property
        def display_value(self) -> str:
            """
            Display Value.

            Return the field's display value as a string.
            """
            assert self.base_field.display_value is not None
            return self.base_field.display_value

    @property
    def typed(self) -> _RequiredSingleOrMultiValueFieldTyped:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._RequiredSingleOrMultiValueFieldTyped(self)


class OptionalSingleOrMultiValueField(BaseField, Generic[ScalarType]):
    """
    Optional Single Or Multi Value Field.

    A decorator class providing typed accessors for an underlying Field.
    Use with optional fields where isMulti is unset.
    """

    @dataclass
    class _OptionalSingleOrMultiValueFieldTyped:
        base_field: OptionalSingleOrMultiValueField

        @property
        def value(self) -> Optional[Union[ScalarType, List[ScalarType]]]:
            """
            Typed Value.

            Returns the value in the field typed as it's specified in an app manifest, if present.
            """
            if self.base_field.value is not None:
                if isinstance(self.base_field.value, list):
                    typed_values: List[ScalarType] = [
                        cast(ScalarType, self.base_field.scalar_definition.from_str(value=str(field_value)))
                        for field_value in cast(List[str], self.base_field.value)
                        if field_value is not None
                    ]
                    return typed_values
                else:
                    field_value = str(self.base_field.value)
                    return self.base_field.scalar_definition.from_str(value=field_value)
            return None

        @property
        def display_value(self) -> Optional[str]:
            """
            Display Value.

            Return the field's display value as a string, if present.
            """
            # Check to ensure linked before display_value, which will raise NotPresentError on unlinked
            if self.base_field.value is None:
                return None
            return None if self.base_field.display_value == "" else self.base_field.display_value

    @property
    def typed(self) -> _OptionalSingleOrMultiValueFieldTyped:
        """
        Typed.

        Return a reference to a typed field with typesafe accessors.
        """
        return self._OptionalSingleOrMultiValueFieldTyped(self)


@dataclass
class ArrayConfigItem(BaseConfigItem):
    """
    Array Config Item.

    An array config item representing a row.
    """

    @property
    def name(self) -> str:
        """Return the user defined name of the array row."""
        # Config item is not optional for arrays
        assert self.config_item is not None
        assert self.config_item.value is not None
        return cast(str, self.config_item.value)

    def full_path(self) -> List[str]:
        """Return the full path of the current array row, inheriting from all parents."""
        path = super().full_path()
        return path + [self.name]


@dataclass
class ScalarConfigItem(BaseConfigItem):
    """
    Scalar Config Item.

    Scalars are values that can be represented outside the Benchling domain.
    """

    config_item: Optional[ScalarConfigReference]
    definition: Optional[ScalarDefinition]


@dataclass
class SecureTextDependency(ScalarConfigItem):
    """
    SecureText Config.

    A dependency for accessing a secure_text config.
    """

    # This is declared Optional because a decryption provider is not required until attempting
    # to decrypt a value.
    decryption_provider: Optional[BaseDecryptionProvider]


class BaseDependencies:
    """
    A base class for implementing dependencies.

    Used as a facade for the underlying link store, which holds dependency links configured in Benchling.
    """

    _store: DependencyLinkStore
    _scalar_definitions: Dict[ScalarConfigItemType, ScalarDefinition]
    _unknown_scalar_definition: Optional[ScalarDefinition]
    # Will be required at runtime if an app attempts to decrypt a secure_text config
    _decryption_provider: Optional[BaseDecryptionProvider]

    def __init__(
        self,
        store: DependencyLinkStore,
        scalar_definitions: Dict[ScalarConfigItemType, ScalarDefinition] = DEFAULT_SCALAR_DEFINITIONS,
        unknown_scalar_definition: Optional[ScalarDefinition] = None,
        decryption_provider: Optional[BaseDecryptionProvider] = None,
    ):
        """
        Initialize Base Dependencies.

        :param store: The dependency link store to source dependency links from.
        :param scalar_definitions: A map of scalar types from the API definitions to ScalarDefinitions which
        determines how we want map them to concrete Python types and values. Can be overridden to customize
        deserialization behavior or formatting.
        :param unknown_scalar_definition: A scalar definition for handling unknown scalar types from the API. Can be
        used to control behavior for forwards compatibility with new types the SDK does not yet support (e.g.,
        by treating them as strings).
        :param decryption_provider: A decryption provider that can decrypt secrets from app config. If
        dependencies attempt to use a secure_text's decrypted value, a decryption_provider must be specified.
        """
        self._store = store
        self._scalar_definitions = scalar_definitions
        self._unknown_scalar_definition = unknown_scalar_definition
        self._decryption_provider = decryption_provider

    @classmethod
    def from_app(
        cls: Type[D],
        client: Benchling,
        app_id: str,
        decryption_provider: Optional[BaseDecryptionProvider] = None,
    ) -> D:
        """Initialize dependencies from an app_id."""
        link_store = DependencyLinkStore.from_app(client=client, app_id=app_id)
        return cls(link_store, decryption_provider=decryption_provider)

    @classmethod
    def from_store(
        cls: Type[D],
        store: DependencyLinkStore,
        decryption_provider: Optional[BaseDecryptionProvider] = None,
    ) -> D:
        """Initialize dependencies from a store."""
        return cls(store=store, decryption_provider=decryption_provider)

    def invalidate_cache(self) -> None:
        """Invalidate the cache of dependency links and force an update."""
        self._store.invalidate_cache()


def _supported_config_item(config_item: AppConfigItem) -> ConfigurationReference:
    if isinstance(config_item, UnknownType):
        raise UnsupportedDependencyError(
            f"Unable to read app configuration with unsupported type: {config_item}"
        )
    return config_item
