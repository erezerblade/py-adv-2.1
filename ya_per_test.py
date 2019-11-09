import unittest
from unittest.mock import patch
from ya_per import translate_me


class YaPerTest(unittest.TestCase):

    def test_correct_translation(self):
        result = translate_me('Привет')
        self.assertEqual(''.join(result.get('text')), "Hi",)

    def test_ya_per_availability(self):
        result = translate_me('Привет')
        self.assertEqual(result.get('code'), 200, msg=f'Сервис отдает ошибку {result.get("code")}')

    @patch('ya_per.KEY', return_value="bublyabublya")
    def test_wrong_api_key(self, input_mock):
        result = translate_me('Привет')
        self.assertEqual(result.get('code'), 502, msg='Ключ подходит')
        pass


if __name__ == '__main__':
    unittest.main()