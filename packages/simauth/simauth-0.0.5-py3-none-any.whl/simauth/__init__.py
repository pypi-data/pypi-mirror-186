#!/usr/bin/env python
import os

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
