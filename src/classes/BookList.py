import numpy as np
import pandas as pd


class BookList:

    def __init__(self):
        self.list = []

    def to_df(self, partition_size):
        data = {'text': [], 'genre': []}

        for book in self.list:
            tmp = []
            count = 0
            for i in book.tokens:
                if count <= partition_size:
                    tmp.append(i)
                    count += 1
                else:
                    data['text'].append(np.array(tmp))
                    data['genre'].append(book.genre)
                    tmp = [i]
                    count = 0
            if tmp:
                data['text'].append(np.array(tmp))
                data['genre'].append(book.genre)

        return pd.DataFrame(data)

    def __str__(self):
        return '\n'.join(self.list)

    def show_text(self):
        for book in self.list:
            print(book)
            print(book.show_text())
            print()

    def show_tokens(self):
        for book in self.list:
            print(book.show_tokens())
            print()
