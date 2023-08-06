import json
import jwt
import os
import functools
from flask import request, Response

from .encrypt_manager import EncryptManager
from .sql_controller import SQLManger


__SALT = "TestForQuICT"


def format_job_dict(job_dict: dict):
    for key, value in job_dict.items():
        if not isinstance(value, (str, int, float, bytes)):
            job_dict[key] = json.dumps(value)

    return job_dict


def request_validation(login: bool = False, register: bool = False):
    """Check JWT validity and do data decryption before getting into the actual logistic.
    Args:
        func:
    Returns:
        None.
    """

    def decorator(func):
        @functools.wraps(func)
        def with_valid(*args, **kwargs):
            sql_conn = SQLManger()
            # Get jwt_token and its payload
            encrypt = EncryptManager()
            jwt_token = request.headers.get('Authorization')
            if jwt_token and jwt_token.startswith('Bearer '):
                payload = jwt.decode(jwt_token[7:], __SALT, ["HS256"])
            else:
                payload = None

            username = payload.get("username", None)
            if register and sql_conn.validate_user(username):
                return create_response(username, __SALT, {'error': "Existed users!"})

            if not register and not sql_conn.validate_user(username):
                return create_response(username, __SALT, {'error': "unauthorized user"})

            kwargs['username'] = username
            aes_key = payload.get('aes_key')
            encrypted_passwd = sql_conn.get_password(username)[:16] if not login and not register else \
                __SALT

            data = request.data
            if data != b'':
                decrypted_aeskey = encrypt.decryptedmsg(aes_key, encrypted_passwd, True)
                decrypted_data = encrypt.decryptedmsg(data, decrypted_aeskey)
                kwargs['json_dict'] = format_job_dict(json.loads(decrypted_data))

            try:
                return_data = func(*args, **kwargs)
            except Exception as e:
                return_data = {'error': repr(e)}
            finally:
                # create header for response
                return create_response(username, encrypted_passwd, return_data)

        return with_valid

    return decorator


def create_response(username: str, password: str, json_dict: dict):
    encrypt = EncryptManager()
    aes_key = os.urandom(16)

    payload = {
        'username': username,
        'aes_key': encrypt.encryptedmsg(aes_key, password).decode('ascii')
    }

    jwt_token = jwt.encode(
        payload=payload,
        key=__SALT,
        algorithm="HS256"
    )

    if json_dict is not None:
        json_dict = encrypt.encryptedmsg(json.dumps(json_dict), aes_key)

    response = Response(response=json_dict)
    response.headers = {"Authorization": f"Bearer {jwt_token}"}

    return response
