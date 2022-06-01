import pathlib
from pathlib import Path

from src.classes.Book import Book
from src.classes.BookList import BookList


class BookReader:
    def __init__(self, path):
        self.path = Path(Path.cwd(), path)

    GENRES = {'detective': 0,
              'fantasy': 1,
              'sci-fi': 2
              }

    def read(self):
        books = BookList()
        for x in self.path.rglob('*.txt'):
            with open(x, 'r', encoding='utf-8') as r:
                data = str(r.read())
            genre = x.parts[-2]
            title = x.parts[-1]
            if genre in self.GENRES:
                value = self.GENRES[genre]

            books.list.append(Book(title=title, genre=value, text=data))

        return books
