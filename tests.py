import unittest
from unittest.mock import patch
import json
from app import get_all_doc_owners_names
from app import add_new_doc
from app import delete_doc

documents = []
directories = {}


def set_up_module() -> None:
    with open('fixtures/documents.json', 'r', encoding="utf-8") as out_docs:
        documents.extend(json.load(out_docs))
    with open('fixtures/directories.json', 'r', encoding="utf-8") as out_dirs:
        directories.update(json.load(out_dirs))


@patch("app.documents", documents, create=True)
@patch("app.directories", directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    @patch('app.input', return_value='10006')
    def test_delete_doc(self, input_mock):
        start_len = len(documents)
        delete_doc()
        self.assertGreater(start_len, len(documents))
        pass
        # Я протестировал эту функцию руками, она в файле не работает. Так что тест работает исправно

    @patch('app.input', side_effect=['1121312', "drivers license", 'Гена Букин', '2'])
    def test_add_new_doc(self, input_mock):
        start_len = len(documents)
        add_new_doc()
        self.assertLess(start_len, len(documents))
        pass

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        self.assertIsInstance(result, set)
        pass


if __name__ == '__main__':
    unittest.main()