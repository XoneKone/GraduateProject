from src.classes.Preprocessing import Preprocessing


class Book:

    def __init__(self, title:str, genre: int, text: str):
        self.title = title
        self.genre = genre
        self.text = Preprocessing.preprocessing(text)
        self.tokens = Preprocessing.to_tokens(text)

    def __str__(self):
        return f"Автор и название: {self.title}\n" \
               f"Жанр: {self.genre}\n"

    def show_text(self):
        return self.text

    def show_tokens(self):
        return self.tokens
