#!/usr/bin/env python3
"""
Basic Authentication
"""

import base64
import binascii
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """base64
        """
        header = "Basic "
        if authorization_header is None:
            return None
        if not type(authorization_header) == str:
            return None
        if len(authorization_header) < 6:
            return None
        if authorization_header.startswith(header):
            return authorization_header[6:]
        else:
            return None

    def decode_base64_authorization_header(self,
                                           base_authorization_header: str
                                           ) -> str:
        """decode base64
        """
        if base_authorization_header is None:
            return None
        if not type(base_authorization_header) == str:
            return None
        try:
            base64_bytes = base_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except binascii.Error:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """user credentials
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not type(decoded_base64_authorization_header) == str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        result = decoded_base64_authorization_header.find(":")
        header_one = decoded_base64_authorization_header[:result]
        header_two = decoded_base64_authorization_header[result + 1:]
        return header_one, header_two

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """finds user
        """
        if user_email is None or not type(user_email) == str:
            return None
        if user_pwd is None or not type(user_pwd) == str:
            return None
        try:
            search = User.search({'email': user_email})
        except KeyError:
            return None
        if not search:
            return None
        if not search[0].is_valid_password(user_pwd):
            return None
        return search[0]

    def current_user(self, request=None) -> TypeVar('user'):
        """retrieve the user
        """
        auth_header = self.authorization_header(request)
        extract_auth = self.extract_base64_authorization_header(auth_header)
        decode_auth = self.decode_base64_authorization_header(extract_auth)
        search = self.extract_user_credentials(decode_auth)
        user = self.user_object_from_credentials(search[0], search[1])
        return user