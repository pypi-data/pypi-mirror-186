import os
import jwt
from configparser import ConfigParser


class Auth0Exception(Exception):
    """Exception for auth0"""


class IllegalTokenExcpetion(Auth0Exception):
    """Illegal Auth0 Exception"""


class Auth0TokenVerifier():
    """Does all the token verification using PyJWT"""

    def __init__(self, permissions=None, scopes=None):
        self.permissions = permissions
        self.scopes = scopes
        self.config = {
            "DOMAIN": os.getenv("DOMAIN", "bdating-consumer-dev.au.auth0.com"),
            "API_AUDIENCE": os.getenv("API_AUDIENCE", "oa1z7FUmEYNNv2Bhi8Rk2I6ISO0AdbEN"),
            "ISSUER": os.getenv("ISSUER", "https://bdating-consumer-dev.au.auth0.com/"),
            "ALGORITHMS": os.getenv("ALGORITHMS", "RS256"),
        }

        # This gets the JWKS from a given URL and does processing so you can
        # use any of the keys available
        jwks_url = f'https://{self.config["DOMAIN"]}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    def verify(self, token):
        # This gets the 'kid' from the passed token
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token
            )
            signing_key = signing_key.key
        except jwt.exceptions.PyJWKClientError as error:
            return {"status": "error", "msg": error.__str__()}
        except jwt.exceptions.DecodeError as error:
            return {"status": "error", "msg": error.__str__()}

        try:
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=self.config["ALGORITHMS"],
                audience=self.config["API_AUDIENCE"],
                issuer=self.config["ISSUER"],
            )
        except Exception as e:
            return {"status": "error", "message": str(e)}

        if self.scopes:
            result = self._check_claims(
                payload, 'scope', str, self.scopes.split(' '))
            if result.get("error"):
                return result

        if self.permissions:
            result = self._check_claims(
                payload, 'permissions', list, self.permissions)
            if result.get("error"):
                return result

        return payload

    def _check_claims(self, payload, claim_name, claim_type, expected_value):

        instance_check = isinstance(payload[claim_name], claim_type)
        result = {"status": "success", "status_code": 200}

        payload_claim = payload[claim_name]

        if claim_name not in payload or not instance_check:
            result["status"] = "error"
            result["status_code"] = 400

            result["code"] = f"missing_{claim_name}"
            result["msg"] = f"No claim '{claim_name}' found in token."
            return result

        if claim_name == 'scope':
            payload_claim = payload[claim_name].split(' ')

        for value in expected_value:
            if value not in payload_claim:
                result["status"] = "error"
                result["status_code"] = 403

                result["code"] = f"insufficient_{claim_name}"
                result["msg"] = (f"Insufficient {claim_name} ({value}). You "
                                 "don't have access to this resource")
                return result
        return result
