import os
import configs
import firebase_admin
from firebase_admin import credentials, firestore

from .utils import Singleton


class FirebaseAppWrapper(object, metaclass=Singleton):
    def __init__(self, name=None, service_account_key='serviceAccountKey.json', def_collection_name='default'):
        self.name = name or firebase_admin._DEFAULT_APP_NAME
        self.def_collection_name = def_collection_name
        self.cred = credentials.Certificate(os.path.join(os.path.dirname(configs.__file__), service_account_key))
        self._app = self.initialize_app()

    def initialize_app(self):
        return firebase_admin.initialize_app(credential=self.cred, name=self.name)

    def is_active(self):
        return bool(self._app)

    @property
    def client(self):
        return firestore.client()

    @property
    def collection(self, name=None):
        return self.client.collection(name or self.def_collection_name)
