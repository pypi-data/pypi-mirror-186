import json
import datetime
import hashlib

from base64 import urlsafe_b64decode, urlsafe_b64encode

from . import exceptions


def _has_valid_key(payload: str, key: str, checksum: str) -> bool:
    joined_data = str(payload + key).encode()
    hash_check = hashlib.sha1(joined_data).hexdigest()
    return hash_check == checksum


def _payload_is_expired(expire_str: str):
    expire_time = datetime.datetime.strptime(expire_str, '%Y-%m-%d %H-%M-%S')
    return datetime.datetime.now() > expire_time


def encode(payload: dict, key: str,
           expires_in: datetime.timedelta = None) -> str:
    """Creates a new UToken token.

    If you pass a `datetime.timedelta` type object
    to the `expires_in` argument, you will define the
    maximum time of the token. If the token expires
    and you try to decode it, the `ExpiredTokenError`
    exception will be thrown.

    :param payload: Data to be encoded
    :type payload: Union[dict, list]
    :param key: Key to encode
    :type key: str
    :param expires_in: Token expiration time, defaults to None
    :type expires_in: datetime.timedelta, optional
    :return: Returns the encoded token
    :rtype: str
    """

    if expires_in:
        exp: datetime.datetime = datetime.datetime.now() + expires_in
        payload['exp'] = exp.strftime('%Y-%m-%d %H-%M-%S')

    payload_json = json.dumps(payload).encode()
    payload_b64 = urlsafe_b64encode(payload_json).decode()
    payload_b64 = payload_b64.replace('=', '')

    checksum = str(payload_b64 + key).encode()
    checksum_hash = hashlib.sha1(checksum).hexdigest()
    utoken = '.'.join([payload_b64, checksum_hash])

    return utoken


def decode(utoken: str, key: str) -> dict:
    """Decode the UToken and returns its payload.

    :param utoken: Encoded UToken
    :type utoken: str
    :param key: Key used for token encoding
    :type key: str
    :raises exceptions.InvalidTokenError: Raise if token is invalid
    :raises exceptions.InvalidKeyError: Raise if key is invalid
    :raises exceptions.InvalidContentTokenError: Raise if content is invalid
    :raises exceptions.ExpiredTokenError: Raise if token has expired
    :return: Return token payload
    :rtype: dict
    """

    try:
        payload, checksum = utoken.split('.')

        if _has_valid_key(payload, key, checksum):
            payload_b64 = str(payload + '==').encode()
            decoded_payload = urlsafe_b64decode(payload_b64)
            payload_json: dict = json.loads(decoded_payload)
            expire_str = payload_json.get('exp')

            if expire_str:
                if _payload_is_expired(expire_str):
                    raise exceptions.ExpiredTokenError('The token has reached the expiration limit')

                payload_json.pop('exp')
        else:
            raise exceptions.InvalidKeyError('Invalid decode key')
    except json.JSONDecodeError:
        raise exceptions.InvalidContentTokenError('Token payload is not convertible to JSON')
    except ValueError:
        raise exceptions.InvalidTokenError('Token is invalid')

    return payload_json


def decode_without_key(utoken: str) -> dict:
    """Decodes the token without performing an
    integrity check, i.e. no secret key is needed.

    :param utoken: Token
    :type utoken: str
    :raises InvalidTokenError: Invalid Token
    :raises InvalidContentTokenError: Invalid content
    :raises ExpiredTokenError: Expired Token
    :return: Returns the content of the token
    :rtype: dict
    """

    try:
        payload, __ = utoken.split('.')

        payload_b64 = str(payload + '==').encode()
        decoded_payload = urlsafe_b64decode(payload_b64)
        payload_json: dict = json.loads(decoded_payload)
        expire_str = payload_json.get('exp')

        if expire_str:
            if _payload_is_expired(expire_str):
                raise exceptions.ExpiredTokenError('The token has reached the expiration limit')

            payload_json.pop('exp')
    except json.JSONDecodeError:
        raise exceptions.InvalidContentTokenError('Token payload is not convertible to JSON')
    except ValueError:
        raise exceptions.InvalidTokenError('Token is invalid')

    return payload_json
