import os
import datetime
import json
import jwt
import requests

from .encrypt_manager import EncryptManager


class EncryptedRequest:
    """ The class contains encrypted request(get, post, delete). """
    def __init__(self):
        self._encrypt = EncryptManager()
        self.__SALT = "TestForQuICT"

    def get(self, url: str, user_info: tuple):
        """ Send a GET Request.

        Args:
            url (str): URL for request.
            user_info (tuple): the login user's information.
        """
        aes_key = os.urandom(16)
        header = self._generate_header(aes_key, user_info)

        # Get response.
        response = requests.get(
            url=url,
            headers=header
        )

        # decrepted response
        return self._decrepted_response(response, user_info)

    def post(
        self,
        url: str,
        json_dict: dict = None,
        user_info: tuple = None,
        is_login: bool = False
    ):
        """ Send a POST Request.

        Args:
            url (str): URL for request.
            json_dict (dict, optional): The send data. Defaults to None.
            user_info (tuple, optional): The login user's information. Defaults to None.
            is_login (bool, optional): whether is login post or not. Defaults to False.
        """
        aes_key = os.urandom(16)
        header = self._generate_header(aes_key, user_info, is_login)
        if json_dict is not None:
            json_dict = json.dumps(json_dict)

        response = requests.post(
            url=url,
            headers=header,
            data=self._encrypt.encryptedmsg(json_dict, aes_key) if json_dict is not None else None
        )

        # decrepted response
        return self._decrepted_response(response, user_info, is_login)

    def delete(self, url: str, json_dict: dict = None, user_info: tuple = None):
        """ Send a DELETE Request.

        Args:
            url (str): URL for request.
            json_dict (dict, optional): The send data. Defaults to None.
            user_info (tuple, optional): The login user's information. Defaults to None.
        """
        aes_key = os.urandom(16)
        header = self._generate_header(aes_key, user_info)
        if json_dict is not None:
            json_dict = json.dumps(json_dict)

        response = requests.delete(
            url=url,
            headers=header,
            data=self._encrypt.encryptedmsg(json_dict, aes_key) if json_dict is not None else None
        )

        # decrepted response
        return self._decrepted_response(response, user_info)

    def _generate_header(self, aes_key: bytes, user_info: tuple, is_login: bool = False):
        """ Generate Header for Request. Using AES and HRS to encrypte.

        Args:
            aes_key (bytes): The encrypted key for AES Mode.
            user_info (tuple): The login user's information
            is_login (bool, optional): whether is login post or not. Defaults to False.

        Returns:
            dict: The JWT token.
        """
        username = user_info[1]
        password = user_info[2][:16] if not is_login else self.__SALT

        payload = {
            'username': username,
            'aes_key': self._encrypt.encryptedmsg(aes_key, password).decode('ascii'),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        }

        jwt_token = jwt.encode(
            payload=payload,
            key=self.__SALT,
            algorithm="HS256"
        )

        return {"Authorization": f"Bearer {jwt_token}"}

    def _decrepted_response(self, response: requests.Response, user_info: tuple, is_login: bool = False):
        jwt_token = response.headers.get('Authorization')
        if jwt_token and jwt_token.startswith('Bearer '):
            payload = jwt.decode(jwt_token[7:], self.__SALT, ["HS256"])
        else:
            payload = None

        username = user_info[1]
        password = user_info[2][:16] if not is_login else self.__SALT
        assert username == payload.get("username", None)
        encrypted_aes_key = payload.get('aes_key')

        content = response.content
        if not content:
            return None

        aes_key = self._encrypt.decryptedmsg(encrypted_aes_key, password, True)
        decrypted_data = json.loads(self._encrypt.decryptedmsg(content, aes_key))

        if isinstance(decrypted_data, dict) and 'error' in decrypted_data.keys():
            raise KeyError(f"{decrypted_data['error']}")

        return decrypted_data
