"""
Utilities for implementing IndieAuth clients and servers.

>   [IndieAuth](https://indieauth.spec.indieweb.org) is an identity layer on
>   top of OAuth 2.0 [RFC6749], primarily used to obtain an OAuth 2.0 Bearer
>   Token [RFC6750] for use by [Micropub] clients. End-Users and Clients are
>   all represented by URLs. IndieAuth enables Clients to verify the identity
>   of an End-User, as well as to obtain an access token that can be used to
>   access resources under the control of the End-User.

## [Authorization Flow](https://indieauth.spec.indieweb.org/#authorization)

*   The End-User enters a URL in the login form of the client and clicks
    "Sign in". The client canonicalizes the URL. `canonicalize_user(...)`
    
*   The client discovers the End-User's IndieAuth server metadata endpoint by
    fetching the provided URL and looking for the rel=indieauth-metadata value AND
    
*   The client discovers the server's authorization endpoint and token endpoint
    by fetching the metadata URL and looking for the authorization_endpoint and
    token_endpoint values `discover_user(...)`
    
*   The client builds the authorization request including its client identifier,
    requested scope, local state, and a redirect URI, and redirects the browser
    to the authorization endpoint `initiate_signin(...)`
    
*   The authorization endpoint fetches the client information from the client
    identifier URL in order to have an application name and icon to display to
    the user `discover_client(...)`
    
*   The authorization endpoint verifies the End-User, e.g. by logging in, and
    establishes whether the End-User grants or denies the client's request
    
*   The authorization endpoint generates an authorization code and redirects
    the browser back to the client, including an authorization code in the URL
    `complete_signin(...)`
    
*   The client exchanges the authorization code for an access token by making
    a POST request to the token endpoint `redeem_code(...)`. The token endpoint
    validates the authorization code, and responds with the End-User's canonical
    profile URL and an access token `validate_redemption(...)`
    
*   The client confirms the returned profile URL declares the same
    authorization server and accepts the profile URL

Note: If the client is only trying to learn who the user is and does not
need an access token, the client exchanges the authorization code for the
user profile information at the Authorization Endpoint instead.

### Token Management: Introspection, Expiration & Revocation

*   The client revokes the token when the user signs out `revoke_token(...)`

"""

import base64
import hashlib
import string
import time
import webbrowser

import txt
import webcli
from Crypto.Random import random
from webcli import URI

__all__ = [
    "AuthorizationError",
    "canonicalize_user",
    "discover_user",
    "initiate_signin",
    "discover_client",
    "complete_signin",
    "redeem_code",
    "validate_redemption",
    "revoke_token",
    "main",
]

DEVICE_CODE_CHARACTERS = string.ascii_uppercase + string.digits
STATE_CHARACTERS = DEVICE_CODE_CHARACTERS + string.ascii_lowercase
CODE_VERIFIER_CHARACTERS = (
    STATE_CHARACTERS + "-._~"
)  # https://indieauth.spec.indieweb.org/#authorization-request-p-4
ACCESS_TOKEN_CHARACTERS = (
    CODE_VERIFIER_CHARACTERS + "+/"
)  # https://www.rfc-editor.org/rfc/rfc6750#section-2.1


class AuthorizationError(Exception):
    """Raised when an error has occurred during authorization."""


main = txt.application("indieauth", __doc__)


def canonicalize_user(user_url: str) -> URI:
    """
    Return the canonicalized form of user's URL. For clients.

    """
    return webcli.uri(user_url)


def discover_user(user_url: URI, session: dict) -> URI:
    """
    Return the `authorization_endpoint` for given `user_url`. For clients.

    Update `session` to include other endpoints and supported scopes.

    """
    metadata_url = webcli.get(user_url).link("indieauth-metadata")
    auth_metadata = webcli.get(metadata_url).json
    authorization_endpoint = auth_metadata["authorization_endpoint"]
    session.update(
        authorization_endpoint=authorization_endpoint,
        token_endpoint=auth_metadata.get("token_endpoint"),
        revocation_endpoint=auth_metadata.get("revocation_endpoint"),
        introspection_endpoint=auth_metadata.get("introspection_endpoint"),
        ticket_endpoint=auth_metadata.get("ticket_endpoint"),
        scopes_supported=auth_metadata.get("scopes_supported"),
    )
    return webcli.uri(authorization_endpoint)


def initiate_signin(
    client_id: URI, redirect_uri: URI, user_url: URI, scopes: list, session: dict
) -> URI:
    """
    Return a URL to initiate sign-in at `client_id` for `user_url`. For clients.

    `redirect_uri` should be the client's return endpoint.

    Update `session` to include authorization state.

    """
    auth_url = discover_user(user_url, session)
    auth_url["me"] = user_url
    auth_url["client_id"] = session["client_id"] = client_id
    auth_url["redirect_uri"] = session["redirect_uri"] = redirect_uri
    auth_url["response_type"] = "code"
    auth_url["state"] = session["state"] = _generate_random_string(16, STATE_CHARACTERS)
    code_verifier = session["code_verifier"] = _generate_random_string(
        128, CODE_VERIFIER_CHARACTERS
    )
    auth_url["code_challenge"] = _generate_challenge(code_verifier)
    auth_url["code_challenge_method"] = "S256"
    auth_url["scope"] = " ".join(scopes)
    return auth_url


def discover_client(client_id: URI) -> dict:
    """
    Return details of client found at `client_id`. For servers.

    """
    client = {
        "url": webcli.uri(client_id).normalized,
        "name": None,
        "developer": None,
    }
    client_homepage = webcli.get(client["url"])
    if client["url"].startswith("https://addons.mozilla.org"):
        try:
            heading = client_homepage.dom.select("h1.AddonTitle")[0]
        except IndexError:
            pass
        else:
            client["name"] = heading.text.partition(" by ")[0]
            developer_link = heading.select("a")[0]
            developer_id = developer_link.href.rstrip("/").rpartition("/")[2]
            client["developer"] = {
                "name": developer_link.text,
                "url": f"https://addons.mozilla.org/user/{developer_id}",
            }
    else:
        for item in client_homepage.mf2json["items"]:
            if "h-app" in item["type"]:
                properties = item["properties"]
                client["name"] = properties["name"][0]
                break
            client["developer"] = {"name": "NAME", "url": "URL"}  # TODO
    return client


def complete_signin(redirect_uri: URI, state, code, iss) -> URI:
    """
    Return `redirect_uri` with `state` and `code` parameters added. For servers.

    """
    redirect_uri = webcli.uri(redirect_uri)
    redirect_uri["state"] = state
    redirect_uri["code"] = code
    redirect_uri["iss"] = iss
    return redirect_uri


def redeem_code(state: str, code: str, session: dict, flow: str = "profile") -> dict:
    """
    Return auth response after redeeming code at endpoint. For clients.

    `flow` can be either 'profile' or 'token'.

    Update `session` to include profile information.

    """
    if state != session["state"]:
        raise AuthorizationError("bad state")
    if flow == "profile":
        endpoint = session["authorization_endpoint"]
    elif flow == "token":
        endpoint = session["token_endpoint"]
    else:
        raise AuthorizationError("only `profile` and `token` flows supported")
    response = webcli.post(
        endpoint,
        headers={"Accept": "application/json"},
        data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": session["client_id"],
            "redirect_uri": session["redirect_uri"],
            "code_verifier": session["code_verifier"],
        },
    ).json
    # TODO pop unnecessary authorization details from session
    session["uid"] = [response["me"]]
    session["name"] = [response["profile"].get("name", "Anonymous")]
    return response


def validate_redemption(
    request: dict, authorization: dict, owner: dict, flow: str = "profile"
) -> dict:
    """
    Return auth response after validating code redemption. For servers.

    `flow` can be either 'profile' or 'token'.

    """
    if request["grant_type"] not in ("authorization_code", "refresh_token"):
        raise AuthorizationError(f"`grant_type` {request['grant_type']} not supported")
    if request["client_id"] != authorization["client_id"]:
        raise AuthorizationError("`client_id` does not match original request")
    if request["redirect_uri"] != authorization["redirect_uri"]:
        raise AuthorizationError("`redirect_uri` does not match original request")
    if request["code_verifier"]:
        if not authorization["code_challenge"]:
            raise AuthorizationError("`code_verifier` without a `code_challenge`")
        if authorization["code_challenge"] != _generate_challenge(
            request["code_verifier"]
        ):
            raise AuthorizationError("code mismatch")
    elif request["code_challenge"]:
        raise AuthorizationError("`code_challenge` without `code_verifier`")

    response = authorization["response"]
    if flow == "token":
        response = _generate_token(response)
    response["me"] = owner["url"]
    if "profile" in response["scope"]:
        response["profile"] = owner
        if "email" not in response["scope"]:
            response["profile"].pop("email", None)
    response["scope"] = " ".join(response["scope"])
    return response


def _generate_token(response):
    if not response["scope"]:
        raise AuthorizationError("Access Token request requires a scope")
    access_token = _generate_random_string(128, ACCESS_TOKEN_CHARACTERS)
    response.update(
        token_type="Bearer",
        access_token=f"secret-token:{access_token}",
    )
    return response


def revoke_token():
    ...


def request_device_token(device_endpoint, client_id):
    """"""
    response = webcli.post(device_endpoint, data={"client_id": client_id}).json
    device_verification_url = webcli.uri(response["verification_uri"])
    device_verification_url["user_code"] = response["user_code"]
    webbrowser.open_new_tab(str(device_verification_url))
    return response


def poll_device_token(token_endpoint, device_response):
    """"""
    while device_response["expires_in"]:
        token_response = webcli.post(
            token_endpoint,
            data={
                "grant_type": "device_code",
                "device_code": device_response["device_code"],
            },
        )
        if token_response.status == 200:
            break
        device_response["expires_in"] -= device_response["interval"]
        time.sleep(device_response["interval"])
    else:
        raise Exception("fail")
    return token_response


def _generate_random_string(length: int, charset: str) -> str:
    """Return a random string of given `length`."""
    return "".join([str(random.choice(charset)) for _ in range(length)])


def _generate_challenge(verifier):
    """Return a `challenge` computed from given `verifier`."""
    raw_hash = hashlib.sha256(verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(raw_hash).decode().rstrip("=")


@main.register()
class AcquireToken:
    """Initiate a device flow authorization via the command line."""

    def setup(self, add_arg):
        add_arg("user_url", help="user's URL")

    def run(self, stdin, log):
        return 0
