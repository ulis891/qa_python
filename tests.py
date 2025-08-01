import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_one_book(self, collector):
        """
        Тест проверяет, что метод add_new_book добавляет книгу и у добавленной книги нет жанра
        """
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        assert name in collector.books_genre and collector.books_genre[name] == ''

    @pytest.mark.parametrize("name", [
        '',
        'Название книги длинной больше 40 символов'])
    def test_add_new_book_wrong_len_book_name(self, collector, name):
        """
        Тест проверяет, что метод add_new_book не добавляет книгу с названием, которое не соответствует требованиям
        :param collector: созданный экземпляр класса BooksCollector
        :param name: Название книги
        """
        collector.add_new_book(name)
        assert name not in collector.books_genre

    @pytest.mark.parametrize("name", [
        '1',
        'Нормальное название',
        'Название книги из сорока символов ровно!'])
    def test_add_new_book_right_len_book_name(self, collector, name):
        """
        Тест проверяет, что метод add_new_book добавляет книгу с названием, которое соответствует требованиям
        :param collector: созданный экземпляр класса BooksCollector
        :param name: Название книги
        """
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize("name, genre, expected_genre", [
        ('Гарри Поттер', 'Фантастика', 'Фантастика'),
        ('Шерлок Холмс', 'Детективы', 'Детективы'),
        ('Винни Пух', 'Мультфильмы', 'Мультфильмы'),
        ('Что делать, если ваш кот хочет вас убить', 'Ужасы', 'Ужасы'),
        ('Гордость и предубеждение и зомби', 'Торт', '')])
    def test_set_book_genre_right_genre(self, collector, name, genre, expected_genre):
        """
        Тест проверяет, что метод set_book_genre устанавливает жанр для книги если жанр существует.
        :param collector: созданный экземпляр класса BooksCollector
        :param name: название книги
        :param genre: жанр
        :param expected_genre: ожидаемый жанр
        """
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == expected_genre

    def test_get_book_genre(self, collector):
        """
        Тест проверяет, что метод get_books_genre возвращает жанр книги.
        :param collector: созданный экземпляр класса BooksCollector
        """
        name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Комедии')
        assert collector.get_book_genre(name) == 'Комедии'

    @pytest.mark.parametrize("name, genre", [
        ('Гарри Поттер', 'Фантастика'),
        ('Шерлок Холмс', 'Детективы'),
        ('Винни Пух', 'Мультфильмы'),
        ('Что делать, ваш кот хочет вас убить', 'Ужасы'),
        ('Гордость и предубеждение и зомби', 'Комедии')])
    def test_get_books_with_specific_genre_in_dictionary(self, collector_with_books_and_genre, name, genre):
        """
        Тест проверяет, что метод get_books_with_specific_genre возвращает список книг с указанным жанром,
        если жанр есть в словаре.
        :param collector_with_books_and_genre: созданный экземпляр класса BooksCollector с книгами и жанрами
        """
        assert collector_with_books_and_genre.get_books_with_specific_genre(genre) == [name]

    @pytest.mark.parametrize("genre", ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_missing_from_dictionary(self, collector_with_books, genre):
        """
        Тест проверяет, что метод get_books_with_specific_genre возвращает пустой список,
        если книги с указанным жанром нет в коллекции.
        :param collector_with_books - экземпляр класса BooksCollector с книгами
        """
        assert collector_with_books.get_books_with_specific_genre(genre) == []

    def test_get_books_with_specific_genre_books_wrong_genre(self, collector_with_books_and_genre):
        """
        Тест проверяет, что метод get_books_with_specific_genre возвращает пустой список,
        если жанр не существует в списке жанров.
        :param collector_with_books_and_genre - экземпляр класса BooksCollector с книгами и жанрами
        """
        assert collector_with_books_and_genre.get_books_with_specific_genre('иидемоК') == []

    def test_get_books_genre_empty_dict(self, collector):
        """
        Тест проверяет, что метод get_books_genre возвращает пустой словарь, если нет книг в коллекции.
        :param collector:
        """
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize("name, genre", [
        ('Гарри Поттер', 'Фантастика'),
        ('Шерлок Холмс', 'Детективы'),
        ('Винни Пух', 'Мультфильмы'),
        ('Что делать, ваш кот хочет вас убить', 'Ужасы'),
        ('Гордость и предубеждение и зомби', 'Комедии')])
    def test_get_books_genre_not_empty_dict(self, collector_with_books_and_genre, name, genre):
        """
        Тест проверяет, что метод get_books_genre возвращает словарь, если есть книги в коллекции.
         и словарь соответствует добавленным книгам.
        :param collector_with_books_and_genre - экземпляр класса BooksCollector с книгами и жанрами
        """
        assert collector_with_books_and_genre.get_books_genre()[name] == genre

    def test_get_books_for_children_adult_books(self, collector):
        """
        Тест проверяет, что метод get_books_for_children возвращает пустой список книг для детей,
        если в коллекции только взрослые книги.
        :param collector:
        """
        collector.add_new_book('Гадость и предрассудки и зомби')
        collector.set_book_genre('Гадость и предрассудки и зомби', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_for_children() == []

    def test_get_books_for_children_books_for_children(self, collector):
        """
        Тест проверяет, что метод get_books_for_children возвращает список книг для детей,
        если в коллекции есть детские книги.
        :param collector:
        """
        collector.add_new_book('Винни Пух')
        collector.set_book_genre('Винни Пух', 'Мультфильмы')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_books_for_children() == ['Винни Пух', 'Гарри Поттер']

    def test_get_books_for_children_books_mix_books(self, collector_with_books_and_genre):
        """
        Тест проверяет, что метод get_books_for_children возвращает список книг где нет книг для взрослых,
        если в коллекции есть детские и взрослые книги.
        :param collector_with_books_and_genre - экземпляр класса BooksCollector с книгами и жанрами
        """
        adult_books = ['Шерлок Холмс', 'Что делать, ваш кот хочет вас убить']
        for book in adult_books:
            assert book not in collector_with_books_and_genre.get_books_for_children()

    def test_add_book_in_favorites_book_in_dict(self, collector):
        """
        Тест проверяет, что метод add_book_in_favorites добавляет книгу в избранное,
        если книга есть в коллекции.
        :param collector:
        """
        name = 'Гарри Поттер'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    def test_add_book_in_favorites_book_not_in_dict(self, collector):
        """
        Тест проверяет, что метод add_book_in_favorites не добавляет книгу в избранное,
        если книги нет в коллекции.
        :param collector:
        """
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.favorites == []

    def test_add_book_in_favorites_book_in_favorites_two_identical_books(self, collector_with_books):
        """
        Тест проверяет, что метод add_book_in_favorites не добавляет книгу в избранное,
        если она уже есть в избранном.
        :param collector_with_books - экземпляр класса BooksCollector с книгами
        """
        name = 'Гарри Поттер'
        collector_with_books.add_book_in_favorites(name)
        collector_with_books.add_book_in_favorites(name)
        assert name in collector_with_books.favorites and len(collector_with_books.favorites) == 1

    def test_delete_book_from_favorites(self, collector_with_books):
        """
        Тест проверяет, что метод delete_book_from_favorites удаляет книгу из избранного.
        :param collector:
        """
        collector_with_books.add_book_in_favorites('Гарри Поттер')
        collector_with_books.add_book_in_favorites('Шерлок Холмс')
        collector_with_books.delete_book_from_favorites('Гарри Поттер')
        assert collector_with_books.get_list_of_favorites_books() == ['Шерлок Холмс']
