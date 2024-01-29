class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.__name = name
        self.__author = author
        self.pages_setter(pages)


    def pages_setter(self, pages: int):
        if not isinstance(pages, int):
            ValueError("Incorrect type")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Страницы {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.__name = name
        self.__author = author
        self.duration_set(duration)

    def duration_set(self, duration: float):
        if not isinstance(duration, float):
            ValueError("Incorrect type")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}. Длительность {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"