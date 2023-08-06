import os
import logging
from typing import List
from flask import request, make_response, jsonify
from pymongo import MongoClient
from alephvault.http_storage.flask_app import StorageApp
from alephvault.http_storage.types.method_handlers import MethodHandler, ItemMethodHandler


logging.basicConfig()


class GetUserByLogin(MethodHandler):
    """
    The user's password is not validated here.
    """

    def __call__(self, client: MongoClient, resource: str, method: str, db: str, collection: str, filter: dict):
        login = request.args.get("login")
        if not login:
            return make_response(jsonify({"code": "missing-lookup"}), 400)
        filter = {**filter, "login": login}
        document = client[db][collection].find_one(filter)
        if document:
            return make_response(jsonify(document), 200)
        else:
            return make_response(jsonify({"code": "not-found"}), 404)


ACCOUNTS = {
    "login": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "password": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "display_name": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "position": {
        "type": "dict",
        "required": True,
        "schema": {
            "scope": {
                # It must be a valid scope, but "" can be
                # understood as Limbo (if a player must
                # belong to such state).
                "type": "string",
                "required": True
            },
            "map": {
                # It must be a valid map. An index being
                # >= 0 is expected. Typically, the index
                # must be valid and, if the scope is "",
                # then it is ignored (suggested: 0).
                "type": "integer",
                "required": True,
                "min": 0
            },
            "x": {
                # The position must be valid inside the
                # map it belongs to. It may be ignored
                # if the scope is "".
                "type": "integer",
                "required": True,
                "min": 0,
                "max": 32767
            },
            "y": {
                # The position must be valid inside the
                # map it belongs to. It may be ignored
                # if the scope is "".
                "type": "integer",
                "required": True,
                "min": 0,
                "max": 32767
            },
        }
    }
}


SCOPES = {
    "key": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "template_key": {
        "type": "string",
        "required": True,
        "empty": False
    },
    "dynamic": {
        "type": "boolean",
        "required": True
    },
}


MAPS = {
    "scope_id": {
        "type": "objectid",
        "required": True
    },
    "index": {
        "type": "integer",
        "required": True,
        "min": 0
    },
    "drop": {
        # The layout is: map.drop[y * width + x] == stack([head, ...]).
        "type": "list",
        "schema": {
            "type": "list",
            "schema": {
                "type": "integer"
            }
        }
    }
}


class Application(StorageApp):
    """
    The main application. It comes out of the box with:

    - universe.accounts: the player accounts (and characters).
    - universe.scopes: the scopes.
    - universe.maps: the scopes' maps (and drops).
    """

    SETTINGS = {
        "debug": True,
        "auth": {
            "db": "auth-db",
            "collection": "api-keys"
        },
        "connection": {
            "host": os.environ['DB_HOST'],
            "port": int(os.environ['DB_PORT']),
            "user": os.environ['DB_USER'],
            "password": os.environ['DB_PASS']
        },
        "resources": {
            "accounts": {
                "type": "list",
                "db": "universe",
                "collection": "accounts",
                "soft_delete": True,
                "schema": ACCOUNTS,
                "list_projection": ["login", "password", "display_name", "position"],
                "verbs": "*",
                "indexes": {
                    "unique-login": {
                        "unique": True,
                        "fields": "login"
                    },
                    "unique-nickname": {
                        "unique": True,
                        "fields": "display_name"
                    }
                },
                "methods": {
                    "by-login": {
                        "type": "view",
                        "handler": GetUserByLogin()
                    }
                }
            },
            "scopes": {
                "type": "list",
                "db": "universe",
                "collection": "scopes",
                "soft_delete": True,
                "schema": SCOPES,
                "list_projection": ["key", "template_key", "dynamic"],
                "verbs": "*",
                "indexes": {
                    "key": {
                        "unique": True,
                        "fields": "login"
                    }
                }
            },
            "maps": {
                "type": "list",
                "db": "universe",
                "collection": "maps",
                "soft_delete": True,
                "schema": MAPS,
                "list_projection": ["scope_id", "index", "drop"],
                "verbs": "*",
                "indexes": {
                    "key": {
                        "unique": True,
                        "fields": ["scope_id", "index"]
                    }
                }
            }
        }
    }

    def _init_default_key(self, key: str):
        """
        A convenience utility to initialize an API key.
        :param key: The key to initialize.
        """

        self._client["auth-db"]["api-keys"].insert_one({"api-key": key})

    def _init_static_scopes(self, scopes: List[str]):
        """
        A convenience utility to initialize some static maps.
        :param scopes: The scopes keys to initialize.
        """

        self._client["universe"]["scopes"].insert_many([
            {"key": scope, "template_key": scope, "dynamic": False}
            for scope in set(scopes)
        ])

    def __init__(self, import_name: str = __name__):
        super().__init__(self.SETTINGS, import_name=import_name)
        try:
            setup = self._client["lifecycle"]["setup"]
            result = setup.find_one()
            if not result:
                setup.insert_one({"done": True})
                self._init_default_key(os.environ['SERVER_API_KEY'])
                # self._init_static_scopes([])
        except:
            pass


app = Application()


if __name__ == "__main__":
    app.run("0.0.0.0", 6666)
