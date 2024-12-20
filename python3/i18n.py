from typing import Dict, Literal
import json

TRANSLATABLE_TEXTS = Literal["Pop Question", "Science Question", "Sports Question"]
LANGUAGES = Literal["en", "de", "hu", "zh"]

TRANSLATIONS: Dict[LANGUAGES, Dict[TRANSLATABLE_TEXTS, str]] = {
    "de": {
        "Pop Question": "Pop Frage",
        "Science Question": "Science Frage",
        "Sports Question": "Sport Frage",
    },
    "hu": {
        "Pop Question": "Pop kérdés",
        "Science Question": "Tudomány kérdés",
        "Sports Question": "Sport kérdés",
    },
    "zh": {
        "Pop Question": "Pop 问题",
        "Science Question": "科学问题",
        "Sports Question": "体育问题",
    },
}


class I18n:
    def __init__(self, lang: LANGUAGES = "en"):
        self.lang = lang

    def t(self, text: TRANSLATABLE_TEXTS):
        if self.lang == "en":
            return text
        return TRANSLATIONS[self.lang][text]

    def to_json(self):
        return json.dumps({"lang": self.lang})

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(lang=data["lang"])


class I18nEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, I18n):
            return {"lang": obj.lang}
        return super().default(obj)
