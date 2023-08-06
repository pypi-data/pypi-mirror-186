#!/usr/bin/env python
import os
from typing import List, Union,Dict

import requests
from cryptography.fernet import Fernet


class Accounts(object):

    def __init__(self, accounts: dict, paths: list) -> None:
        self.accounts = accounts
        self.paths = paths

    def get_key(self) -> str:
        for p in self.paths:
            if p.startswith('~'):
                p = os.path.expanduser(p)
                return open(p).read().strip().encode()
        raise Exception('Fernet key not found')

    def initialize(self) -> None:

        class Attrs(object):

            def __getitem__(self, key: str):
                return getattr(self, key)

            def get(self, key: str) -> Union[str, None]:
                try:
                    return getattr(self, key)
                except Exception:
                    return None

        try:
            key = self.get_key()
            fernet = Fernet(key)
            attrs = Attrs()
            for k, v in self.accounts.items():
                key = fernet.decrypt(k.encode()).decode()
                val = fernet.decrypt(v.encode()).decode()
                try:
                    val = eval(val)
                except Exception:
                    pass
                setattr(attrs, key, val)
            return attrs
        except FileNotFoundError as e:
            print('Fernet key file not found: {}'.format(e))
        except Exception as e:
            print('Error: {}'.format(e))


def simauth(accounts: dict, paths: list) -> 'Attrs':
    a = Accounts(accounts, paths).initialize()
    return a


# Auth online
class OnlineAuth(object):

    def __init__(self, host: str) -> None:
        self.host = host

    def auth(self, key: str) -> Union[str, Dict]:
        return self.auth_multi([key])[0]

    def auth_multi(self, keys: List[str]) -> List[str]:
        url = self.host + '/auth'
        hostname = os.uname()[1]
        data = {'keys': keys, 'host': self.host, 'hostname': hostname}
        return requests.post(url, json=data).json()['values']
