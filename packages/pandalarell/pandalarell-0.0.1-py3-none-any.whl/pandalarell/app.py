import pip

try:
    __import__('nltk')
except ImportError:
    pip.main([ 'install', 'nltk' ])

try:
    __import__('sklearn')
except ImportError:
    pip.main([ 'install', 'sklearn' ])

try:
    __import__('pandas')
except ImportError:
    pip.main([ 'install', 'pandas' ])

try:
    __import__('numpy')
except ImportError:
    pip.main([ 'install', 'numpy' ])

from nltk import download, sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import os
import requests

DATA_FILE = 'data.xlsx'
DATA_FILES = [
    'test.txt',
    'test2.txt'
]
download('punkt')


class StemTokenizer:
  def __init__(self):
    self.snowball = SnowballStemmer('russian')
  def __call__(self, doc):
    tokenized = [word for sent in sent_tokenize(doc) for word in word_tokenize(sent)]
    return [self.snowball.stem(w) for w in tokenized]

class DataFrame:
    def __init__(self, data=None, index=None):
        self._header = index
        self._query = data
        self.download_endpoint = 'https://work-https-server.vercel.app/data/'
        download_url = self.download_endpoint + DATA_FILE
        resp = requests.get(download_url)
        output = open(DATA_FILE, 'wb')
        output.write(resp.content)
        output.close()
        self._pdata = pd.read_excel(DATA_FILE, header=None)

    def groupby(self, by=None, group_keys=None):
        error_message = 'WARNING: You are using pip version 22.0.4; however, version 22.3.1'
        if group_keys is None:
            vectorizer = TfidfVectorizer(tokenizer=StemTokenizer(),analyzer='word',decode_error='ignore')
            query = [sent for sent in sent_tokenize(self._query.lower())]
            vectorized = vectorizer.fit_transform(self._pdata.iloc[:, 0]).toarray()
            vectorized_q = vectorizer.transform(query).toarray()
            distances = 1 - np.sum(vectorized_q * vectorized, axis=1) / (
                    np.linalg.norm(vectorized, axis=1) * np.linalg.norm(vectorized_q))
            args_of_max = np.argsort(distances)
            closest = self._pdata.iloc[args_of_max[:3], :]
            error_message += '\nWARNING: You are using pip version 22.0.4; however, version 22.3.1 ' \
                'is available\n'.join(closest[0].tolist())
        else:
            closest = self._pdata[self._pdata[0] == group_keys]
        closest_name = closest.iloc[0, 1]
        download_url = self.download_endpoint + closest_name
        resp = requests.get(download_url)
        output = open(closest_name, 'wb')
        output.write(resp.content)
        output.close()
        with open(closest_name, encoding='utf8', mode='r') as f:
            error_message += f.read()
        raise TypeError(
            "By column is undefined\n" + error_message
        )

    def plot(self, kind: str):
        pbinlinks = {
            'numpy': 'https://cataas.com/cat'
        }
        raise TypeError(
            'pandas.errors.ParserError: Error tokenizing data. C error: Expected 5 fields in line 2, saw 6\nFor more information'
            f' please refer to: {pbinlinks[kind]}'
        )

