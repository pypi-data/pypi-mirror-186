import base64
from datetime import datetime, timedelta, timezone
from typing import cast, List

from benchling_api_client.v2.benchling_client import BenchlingApiClient
import httpx
from jwcrypto import jwk
from typing_extensions import Protocol

from benchling_sdk.errors import raise_for_status
from benchling_sdk.helpers.logging_helpers import log_stability_warning, StabilityLevel
from benchling_sdk.helpers.package_helpers import _required_packages_context, ExtrasPackage
from benchling_sdk.services.v2.stable.api_service import build_json_response

log_stability_warning(StabilityLevel.ALPHA)


class WebhookVerificationError(Exception):
    """
    Webhook Verification Error.

    Indicates a webhook from Benchling could not be verified.

    Some reasons this could happen include:
    - An app developer misconfiguration (e.g., wrong app)
    - A webhook was received too late
    - The webhook did not originate from Benchling (possible attack vector)
    """

    pass


class GetJwksFunction(Protocol):
    """Function for custom resolution of JWKs for an app."""

    def __call__(self, app_id: str) -> jwk.JWKSet:
        """Retrieve JWKs for an app."""
        pass


class JwkUrlProvider(Protocol):
    """
    Function for custom URL for resolving JWKs by app.

    Should generally never be used except in the event of specialized testing with internal Benchling.
    """

    def __call__(self, app_id: str) -> str:
        """Return a fully qualified URL for retrieving JWKs from an app."""
        pass


def _default_httpx_webhook_client() -> httpx.Client:
    """
    Create a default httpx client for webhook verification.

    Since webhook verification does not require authentication and typically takes place before
    Benchling initialization, we don't have access to the internal httpx in Benchling.
    """
    transport = httpx.HTTPTransport(retries=3)
    # noinspection PyProtectedMember
    user_agent_header = BenchlingApiClient._get_user_agent("Benchling SDK", "benchling-sdk")
    return httpx.Client(transport=transport, headers={"User-Agent": user_agent_header})


def _production_webhook_jwks(app_id) -> str:
    """Return the URL for retrieving production JWKs for an app."""
    return f"https://benchling.com/apps/jwks/{app_id}"


def jwks_by_app(
    app_id: str,
    httpx_client: httpx.Client = None,
    jwk_url_provider: JwkUrlProvider = None,
) -> jwk.JWKSet:
    """
    Get JWKs by App.

    Retrieves a set of JWKs assigned to an app used to verify webhooks.

    JWKs generally should not be resolved on their own. We recommend using webhook verification
    functions such as verify().

    This method is provided for specialized cases such as customizing the httpx client.
    """
    if httpx_client is None:
        httpx_client = _default_httpx_webhook_client()
    if jwk_url_provider is None:
        jwk_url_provider = _production_webhook_jwks
    jwk_url = jwk_url_provider(app_id)
    httpx_response = httpx_client.get(jwk_url)
    response = build_json_response(httpx_response)
    raise_for_status(response)
    return jwk.JWKSet.from_json(response.content)


def verify(app_id: str, data: str, headers: dict, jwk_function: GetJwksFunction = None) -> None:
    """
    Verify a webhook.

    Verifies that a webhook was a valid webhook from Benchling.
    Raises WebhookVerificationError if the webhook could not be verified.
    Resolves JWKs from Benchling with default settings. Pass jwk_function for customization.
    """
    _verify_headers_present(headers)
    _verify_timestamp(headers["webhook-timestamp"])
    to_verify = f'{headers["webhook-id"]}.{headers["webhook-timestamp"]}.{data}'
    signatures = headers["webhook-signature"].split(" ")
    der_signatures = _der_signatures_from_versioned_signatures(signatures)
    base64_der_signatures = [base64.b64decode(der_signature) for der_signature in der_signatures]
    if jwk_function is None:

        def _get_default_jwks(_app_id):
            return jwks_by_app(_app_id)

        jwk_function = _get_default_jwks
    jwks = jwk_function(app_id)
    if not _has_valid_signature(to_verify, jwks, base64_der_signatures):
        raise WebhookVerificationError("No matching signature found")


@_required_packages_context(ExtrasPackage.CRYPTOGRAPHY)
def _has_valid_signature(to_verify: str, jwks: jwk.JWKSet, encoded_signatures: List[bytes]) -> bool:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import ec
    from cryptography.hazmat.primitives.serialization import load_pem_public_key

    for jk in jwks:
        pubkey = cast(ec.EllipticCurvePublicKey, load_pem_public_key(jk.export_to_pem()))
        for der_signature in encoded_signatures:
            try:
                pubkey.verify(der_signature, bytes(to_verify, "utf-8"), ec.ECDSA(hashes.SHA256()))
            except InvalidSignature:
                continue
            return True
    return False


def _der_signatures_from_versioned_signatures(versioned_signatures: str) -> List[str]:
    """
    Parse and return a list of ders signatures from a single string.

    Signature format is f"v{version_number}der,{signature}"
    """
    der_signatures = []
    for versioned_sig in versioned_signatures:
        _version, sig = versioned_sig.split(",")
        if "der" in _version:
            der_signatures.append(sig)
    if len(der_signatures) == 0:
        raise WebhookVerificationError("Expected to find a der encoded signature")
    return der_signatures


def _verify_headers_present(headers: dict) -> None:
    """
    Verify Headers Present.

    Check that webhook headers contain all the expected keys. Raises WebhookVerificationError if
    headers are missing, which is more friendly than KeyError.

    Does not validate the contents of headers.
    """
    if "webhook-id" not in headers:
        raise WebhookVerificationError("Missing webhook-id header")
    if "webhook-timestamp" not in headers:
        raise WebhookVerificationError("Missing webhook-timestamp header")
    if "webhook-signature" not in headers:
        raise WebhookVerificationError("Missing webhook-signature header")


def _verify_timestamp(timestamp_header: str) -> None:
    """
    Verify Timestamp.

    Checks that a timestamp in the webhook header is recent enough to not suspect a replay attack.
    """
    webhook_tolerance = timedelta(minutes=5)
    now = datetime.now(tz=timezone.utc)
    try:
        timestamp = datetime.fromtimestamp(float(timestamp_header), tz=timezone.utc)
    except Exception:
        raise WebhookVerificationError("Invalid Signature Headers")
    if timestamp < (now - webhook_tolerance):
        raise WebhookVerificationError("Message timestamp too old")
    if timestamp > (now + webhook_tolerance):
        raise WebhookVerificationError("Message timestamp too new")
