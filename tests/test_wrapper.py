import unittest

from google.cloud.firestore_v1beta1 import DocumentSnapshot

from core.db_setup import FirebaseAppWrapper


class TestFirebaseAppWrapper(unittest.TestCase):
    def setUp(self):
        self.app = FirebaseAppWrapper(def_collection_name='tests')
        self.data_fst = {'test': 'some_text'}
        self.data_sec = {'data': 'some_data'}
        self.data = {'test': 'some_text', 'data': 'some_data'}

    def test_is_active(self):
        assert self.app.is_active()

    def test_read_list(self):
        documents = self.app.collection.get()
        try:
            document = next(documents)
            assert isinstance(document, DocumentSnapshot)
        except StopIteration:
            pass

    def test_crud(self):
        time_tamp, doc_created = self.app.collection.add(self.data_fst)
        assert doc_created.id
        document = self.app.collection.document(doc_created.id)
        assert document.get().to_dict() == self.data_fst
        document.update(self.data_sec)
        assert document.get().to_dict() == self.data
        assert document.delete()
