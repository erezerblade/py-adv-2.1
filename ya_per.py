import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20191109T220758Z.190bcef0580cb5d7.1b928515b58c63f7823ae41be3cfdacea7b9ff70"


def getparams(expand_params):
    default_params = {
        "key": KEY,
        "lang": 'ru-en'
    }
    default_params.update(expand_params)
    return default_params


def translate_me(text):
    params = getparams({'text': str(text)})
    response = requests.get(URL, params=params).json()
    return response


if __name__ == '__main__':
    print(translate_me("Привет мой друг"))