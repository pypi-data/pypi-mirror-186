from datetime import date, datetime
from typing import List, Optional, Type, Union

from benchling_api_client.v2.beta.models.app_config_field_type import AppConfigFieldType
from benchling_api_client.v2.beta.models.base_manifest_config import BaseManifestConfig
from benchling_api_client.v2.beta.models.dropdown_dependency import DropdownDependency
from benchling_api_client.v2.beta.models.dropdown_dependency_types import DropdownDependencyTypes
from benchling_api_client.v2.beta.models.entity_schema_dependency import EntitySchemaDependency
from benchling_api_client.v2.beta.models.entity_schema_dependency_type import EntitySchemaDependencyType
from benchling_api_client.v2.beta.models.field_definitions_manifest import FieldDefinitionsManifest
from benchling_api_client.v2.beta.models.manifest_array_config import ManifestArrayConfig
from benchling_api_client.v2.beta.models.manifest_scalar_config import ManifestScalarConfig
from benchling_api_client.v2.beta.models.resource_dependency import ResourceDependency
from benchling_api_client.v2.beta.models.resource_dependency_types import ResourceDependencyTypes
from benchling_api_client.v2.beta.models.scalar_config import ScalarConfig
from benchling_api_client.v2.beta.models.scalar_config_types import ScalarConfigTypes
from benchling_api_client.v2.beta.models.schema_dependency import SchemaDependency
from benchling_api_client.v2.beta.models.schema_dependency_subtypes import SchemaDependencySubtypes
from benchling_api_client.v2.beta.models.schema_dependency_types import SchemaDependencyTypes
from benchling_api_client.v2.beta.models.workflow_task_schema_dependency import WorkflowTaskSchemaDependency
from benchling_api_client.v2.beta.models.workflow_task_schema_dependency_output import (
    WorkflowTaskSchemaDependencyOutput,
)
from benchling_api_client.v2.beta.models.workflow_task_schema_dependency_type import (
    WorkflowTaskSchemaDependencyType,
)
from benchling_api_client.v2.extensions import UnknownType
from benchling_api_client.v2.stable.extensions import NotPresentError

from benchling_sdk.apps.config.dependencies import ConfigurationReference, UnsupportedDependencyError
from benchling_sdk.apps.config.scalars import JsonType, ScalarModelType
from benchling_sdk.models import (
    AaSequence,
    ArrayElementAppConfigItem,
    AssayResult,
    AssayRun,
    BooleanAppConfigItem,
    Box,
    Container,
    CustomEntity,
    DateAppConfigItem,
    DatetimeAppConfigItem,
    DnaOligo,
    DnaSequence,
    EntitySchemaAppConfigItem,
    Entry,
    FieldAppConfigItem,
    FloatAppConfigItem,
    GenericApiIdentifiedAppConfigItem,
    IntegerAppConfigItem,
    JsonAppConfigItem,
    Location,
    Mixture,
    Molecule,
    Plate,
    Request,
    RnaOligo,
    RnaSequence,
    SecureTextAppConfigItem,
    TextAppConfigItem,
    WorkflowTask,
)

_MODEL_TYPES_FROM_SCHEMA_TYPE = {
    SchemaDependencyTypes.CONTAINER_SCHEMA: Container,
    SchemaDependencyTypes.PLATE_SCHEMA: Plate,
    SchemaDependencyTypes.BOX_SCHEMA: Box,
    SchemaDependencyTypes.LOCATION_SCHEMA: Location,
    SchemaDependencyTypes.ENTRY_SCHEMA: Entry,
    SchemaDependencyTypes.REQUEST_SCHEMA: Request,
    SchemaDependencyTypes.RESULT_SCHEMA: AssayResult,
    SchemaDependencyTypes.RUN_SCHEMA: AssayRun,
    SchemaDependencyTypes.WORKFLOW_TASK_SCHEMA: WorkflowTask,
}


_SCALAR_TYPES_FROM_CONFIG = {
    ScalarConfigTypes.BOOLEAN: bool,
    ScalarConfigTypes.DATE: date,
    ScalarConfigTypes.DATETIME: datetime,
    ScalarConfigTypes.FLOAT: float,
    ScalarConfigTypes.INTEGER: int,
    ScalarConfigTypes.JSON: JsonType,
    ScalarConfigTypes.TEXT: str,
}


_FIELD_SCALAR_TYPES_FROM_CONFIG = {
    AppConfigFieldType.BOOLEAN: bool,
    AppConfigFieldType.DATE: date,
    AppConfigFieldType.DATETIME: datetime,
    AppConfigFieldType.FLOAT: float,
    AppConfigFieldType.INTEGER: int,
    AppConfigFieldType.JSON: JsonType,
    AppConfigFieldType.TEXT: str,
}


ModelType = Union[AssayResult, AssayRun, Box, Container, Entry, Location, Plate, Request]

_INSTANCE_FROM_SCHEMA_SUBTYPE = {
    SchemaDependencySubtypes.AA_SEQUENCE: AaSequence,
    SchemaDependencySubtypes.CUSTOM_ENTITY: CustomEntity,
    SchemaDependencySubtypes.DNA_SEQUENCE: DnaSequence,
    SchemaDependencySubtypes.DNA_OLIGO: DnaOligo,
    SchemaDependencySubtypes.MIXTURE: Mixture,
    SchemaDependencySubtypes.MOLECULE: Molecule,
    SchemaDependencySubtypes.RNA_OLIGO: RnaOligo,
    SchemaDependencySubtypes.RNA_SEQUENCE: RnaSequence,
}

EntitySubtype = Union[
    AaSequence, CustomEntity, DnaOligo, DnaSequence, Mixture, Molecule, RnaOligo, RnaSequence
]

AnyDependency = Union[
    BaseManifestConfig,
    DropdownDependency,
    EntitySchemaDependency,
    FieldDefinitionsManifest,
    ManifestArrayConfig,
    ManifestScalarConfig,
    ResourceDependency,
    SchemaDependency,
    WorkflowTaskSchemaDependency,
]

ArrayElementDependency = Union[
    SchemaDependency,
    EntitySchemaDependency,
    WorkflowTaskSchemaDependency,
    DropdownDependency,
    ResourceDependency,
    ManifestScalarConfig,
]


class UnsupportedSubTypeError(Exception):
    """Error when an unsupported subtype is encountered."""

    pass


def model_type_from_dependency(
    dependency: Union[EntitySchemaDependency, SchemaDependency]
) -> Optional[Type[Union[ModelType, EntitySubtype]]]:
    """Translate a schema dependency to its model class. Must have a valid subtype."""
    if isinstance(dependency, EntitySchemaDependency):
        subtype = subtype_from_entity_schema_dependency(dependency)
        if subtype:
            return _subtype_instance_from_dependency(dependency)
        return None
    return _MODEL_TYPES_FROM_SCHEMA_TYPE[dependency.type]


def scalar_type_from_config(config: ScalarConfig) -> Union[object, Type[ScalarModelType]]:
    """Translate a scalar config to its Pyton type."""
    # We union with object to satisfy JsonType.
    return _SCALAR_TYPES_FROM_CONFIG.get(config.type, str)


def scalar_type_from_field_config(config: FieldDefinitionsManifest) -> Union[object, Type[ScalarModelType]]:
    """Translate a field config to its Pyton type."""
    # type may not be specified, so handle NotPresentError
    try:
        if hasattr(config, "type"):
            # We union with object to satisfy JsonType.
            return _FIELD_SCALAR_TYPES_FROM_CONFIG.get(config.type, str)
    # We can't seem to handle this programmatically by checking isinstance() or output truthiness
    except NotPresentError:
        pass
    return str


def field_definitions_from_dependency(
    dependency: Union[
        EntitySchemaDependency,
        SchemaDependency,
        WorkflowTaskSchemaDependency,
        WorkflowTaskSchemaDependencyOutput,
    ]
) -> List[FieldDefinitionsManifest]:
    """Safely return a list of field definitions from a schema dependency or empty list."""
    try:
        if hasattr(dependency, "field_definitions"):
            return dependency.field_definitions
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return []


def element_definition_from_dependency(dependency: ManifestArrayConfig) -> List[ArrayElementDependency]:
    """Safely return an element definition as a list of dependencies from an array dependency or empty list."""
    try:
        if hasattr(dependency, "element_definition"):
            return [
                _fix_element_definition_deserialization(element) for element in dependency.element_definition
            ]
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return []


# TODO BNCH-57036 All element definitions currently deserialize to UnknownType. Hack around this temporarily
def _fix_element_definition_deserialization(
    element: Union[UnknownType, ArrayElementDependency]
) -> ArrayElementDependency:
    if isinstance(element, UnknownType):
        if "type" in element.value:
            element_type = element.value["type"]
            if element_type == WorkflowTaskSchemaDependencyType.WORKFLOW_TASK_SCHEMA:
                return WorkflowTaskSchemaDependency.from_dict(element.value)
            elif element_type == EntitySchemaDependencyType.ENTITY_SCHEMA:
                return EntitySchemaDependency.from_dict(element.value)
            elif element_type in [member.value for member in SchemaDependencyTypes]:
                return SchemaDependency.from_dict(element.value)
            elif element_type == DropdownDependencyTypes.DROPDOWN:
                return DropdownDependency.from_dict(element.value)
            elif element_type in [member.value for member in ResourceDependencyTypes]:
                return ResourceDependency.from_dict(element.value)
            elif element_type in [member.value for member in ScalarConfigTypes]:
                return ManifestScalarConfig.from_dict(element.value)
        raise NotImplementedError(f"No array deserialization fix for {element}")
    return element


def workflow_task_schema_output_from_dependency(
    dependency: WorkflowTaskSchemaDependency,
) -> Optional[WorkflowTaskSchemaDependencyOutput]:
    """Safely return a workflow task schema output from a workflow task schema or None."""
    try:
        if hasattr(dependency, "output"):
            return dependency.output
    # We can't seem to handle this programmatically by checking isinstance() or output truthiness
    except NotPresentError:
        pass
    return None


def options_from_dependency(dependency: DropdownDependency) -> List[BaseManifestConfig]:
    """Safely return a list of options from a dropdown dependency or empty list."""
    try:
        if hasattr(dependency, "options"):
            return dependency.options
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return []


def is_config_required(dependency: AnyDependency) -> bool:
    """Safely return if a config item is required."""
    try:
        if hasattr(dependency, "required_config"):
            # `type: ignore` is used here because casting would be inaccurate or fragile.
            return dependency.required_config  # type: ignore
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return False


def is_field_value_required(dependency: FieldDefinitionsManifest) -> bool:
    """
    Safely return if a field must have a value.

    A field must be specified as requiredConfig: true AND isRequired: true to require a value.
    """
    # Fields must be both linked and isRequired to always provide a value
    try:
        if hasattr(dependency, "required_config") and hasattr(dependency, "is_required"):
            # dependency.required_config is Optional so evaluate the bool value
            return dependency.required_config is True and dependency.is_required is True
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return False


# For forwards compatibility with multi-valued scalars, which could infer Unset == False
def is_config_multi_valued(dependency: FieldDefinitionsManifest) -> bool:
    """
    Safely return if a config item is multi-valued.

    Assumes False in the case that a multi-valued constraint is unspecified (Unset).
    """
    multi_valued_unset = is_config_multi_valued_or_unset(dependency)
    return multi_valued_unset if multi_valued_unset is not None else False


def is_config_multi_valued_or_unset(dependency: FieldDefinitionsManifest) -> Optional[bool]:
    """
    Safely return if a config item is multi-valued or None if it's Unset.

    Multi-valued constraint being undefined cannot be safely inferred for type coercion.

    For instance, a required text field could be typed as:
    isMulti == True: List[str]
    isMulti == False: str
    isMulti == Unset: Union[str, List[str]]
    """
    try:
        if hasattr(dependency, "is_multi") and dependency.is_multi is not None:
            return dependency.is_multi
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return None


def subtype_from_entity_schema_dependency(
    dependency: EntitySchemaDependency,
) -> Optional[SchemaDependencySubtypes]:
    """Safely return an entity schema dependency's subtype, if present."""
    try:
        if hasattr(dependency, "subtype") and dependency.subtype:
            return dependency.subtype
    # We can't seem to handle this programmatically by checking isinstance() or field truthiness
    except NotPresentError:
        pass
    return None


def app_config_type_from_dependency(dependency: AnyDependency) -> Type[ConfigurationReference]:
    """
    App Config Item Type From Item.

    Returns the type of the API model corresponding to an app config item.
    Raises UnsupportedDependencyError if encountering an unknown type.
    """
    # Generic type
    if isinstance(
        dependency,
        (
            BaseManifestConfig,
            DropdownDependency,
            SchemaDependency,
            ResourceDependency,
            WorkflowTaskSchemaDependency,
        ),
    ):
        return GenericApiIdentifiedAppConfigItem
    # Specially handled Schema types
    elif isinstance(dependency, FieldDefinitionsManifest):
        return FieldAppConfigItem
    elif isinstance(dependency, EntitySchemaDependency):
        return EntitySchemaAppConfigItem
    # Scalar types
    elif isinstance(dependency, ManifestScalarConfig):
        if dependency.type == ScalarConfigTypes.BOOLEAN:
            return BooleanAppConfigItem
        elif dependency.type == ScalarConfigTypes.DATE:
            return DateAppConfigItem
        elif dependency.type == ScalarConfigTypes.DATETIME:
            return DatetimeAppConfigItem
        elif dependency.type == ScalarConfigTypes.FLOAT:
            return FloatAppConfigItem
        elif dependency.type == ScalarConfigTypes.INTEGER:
            return IntegerAppConfigItem
        elif dependency.type == ScalarConfigTypes.JSON:
            return JsonAppConfigItem
        elif dependency.type == ScalarConfigTypes.SECURE_TEXT:
            return SecureTextAppConfigItem
        elif dependency.type == ScalarConfigTypes.TEXT:
            return TextAppConfigItem
    elif isinstance(dependency, ManifestArrayConfig):
        return ArrayElementAppConfigItem
    raise UnsupportedDependencyError(f"Unrecognized type for {dependency}]")


def _subtype_instance_from_dependency(dependency: EntitySchemaDependency) -> Type[EntitySubtype]:
    if dependency.subtype in _INSTANCE_FROM_SCHEMA_SUBTYPE:
        return _INSTANCE_FROM_SCHEMA_SUBTYPE[dependency.subtype]
    # This would mean the spec has a new subtype, the manifest installed in Benchling has declared it,
    # the user has linked it in Benchling, but the app code receiving it was never updated.
    # App developers should support it in deployed app code before republishing the manifest.
    raise UnsupportedSubTypeError(
        f"An unsupported subtype, {dependency.subtype.value} was received. "
        f"The version of the SDK may need to be upgraded to support this."
    )
