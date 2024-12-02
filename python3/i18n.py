from typing import Literal



TRANSLATABLE_TEXTS = Literal['Pop Question', 'Science Question', 'Sports Question']

TRANSLATIONS = {
    'de': {
        'Pop Question': 'Pop Frage',
        'Science Question': 'Science Frage',
        'Sports Question': 'Sport Frage',

    },
    'hu': {
        'Pop Question': 'Pop kérdés',
        'Science Question': 'Tudomány kérdés',
        'Sports Question': 'Sport kérdés',
    },
    'ch': {
        'Pop Question': 'Pop 问题',
        'Science Question': '科学问题',
        'Sports Question': '体育问题',
    }
}
LANGUAGES = Literal['en', 'de', 'hu' ]

class I18n:
    def __init__(self, lang:LANGUAGES='en'):
        self.lang = lang

    def t(self, text:TRANSLATABLE_TEXTS):
        if self.lang == 'en':
            return text
        return TRANSLATIONS[self.lang][text] 