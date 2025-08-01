import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """
    Создает экземпляр класса BooksCollector
    :return: BooksCollector() - экземпляр класса
    """
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    books = ['Гарри Поттер',
             'Шерлок Холмс',
             'Винни Пух',
             'Что делать, ваш кот хочет вас убить',
             'Гордость и предубеждение и зомби'
             ]
    for book in books:
        collector.add_new_book(book)
    return collector


@pytest.fixture
def collector_with_books_and_genre(collector_with_books):
    books = {'Гарри Поттер': 'Фантастика',
             'Шерлок Холмс': 'Детективы',
             'Винни Пух': 'Мультфильмы',
             'Что делать, ваш кот хочет вас убить': 'Ужасы',
             'Гордость и предубеждение и зомби': 'Комедии'
             }
    for book, genre in books.items():
        collector_with_books.set_book_genre(book, genre)
    return collector_with_books
