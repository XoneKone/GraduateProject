import re
from string import punctuation

from nltk import word_tokenize
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer


class Preprocessing:
    PUNCTUATION = list(punctuation) + ['–', '—']
    STOPWORDS = stopwords.words('russian')
    MORPH = MorphAnalyzer()

    @classmethod
    def remove_punctuation(cls, text):
        return "".join([ch if ch not in cls.PUNCTUATION and ch.isalpha() else ' ' for ch in text])

    @classmethod
    def remove_numbers(cls, text):
        return "".join([i if not i.isdigit() else ' ' for i in text])

    @classmethod
    def remove_multiple_spaces(cls, text):
        return re.sub(r'\s+', ' ', text, flags=re.I)

    @classmethod
    def preprocessing(cls, text: str):
        return text.replace('\xa0', '').replace('\t', '').replace('\n', '')

    @classmethod
    def tokenize(cls, text: str):
        tokens = []
        for token in list(map(str.lower, word_tokenize(text))):
            if (token not in cls.PUNCTUATION) and (token not in cls.STOPWORDS):
                tokens.append(token.replace('\n', ''))
        return tokens

    @classmethod
    def lemmatize(cls, tokens: list[str]):
        lemmatized_tokens = []
        for token in tokens:
            var = cls.MORPH.parse(token)[0]
            if var.normal_form not in cls.STOPWORDS:
                lemmatized_tokens.append(var.normal_form)
        return lemmatized_tokens

    @classmethod
    def to_tokens(cls, text: str):
        return cls.lemmatize(cls.tokenize(text))
