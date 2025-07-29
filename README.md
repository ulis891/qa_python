# qa_python
## Описание фикстур:
- collector: создаёт экземпляр класса BooksCollector
- collector_with_books: создаёт экземпляр класса BooksCollector с книгами
- collector_with_books_and_genre: создаёт экземпляр класса BooksCollector с книгами и жанрамии 
## Описание тестов
- **test_add_new_book_one_book**: проверяет добавление новой книги.
- **test_add_new_book_wrong_len_book_name**: проверяет, что метод add_new_book не добавляет книгу с названием, которое не соответствует требованию по длинне названия
- **test_add_new_book_right_len_book_name**: проверяет, что метод add_new_book добавляет книгу с названием, которое соответствует требованию по длинне названия.
- **test_set_book_genre_right_genre**: проверяет, что метод set_book_genre устанавливает жанр для книги если жанр существует.
- **test_get_book_genre**: проверяет, что метод get_books_genre возвращает жанр книги.
- **test_get_books_with_specific_genre_in_dictionary**: проверяет, что метод get_books_with_specific_genre возвращает список книг с указанным жанром
- **test_get_books_with_specific_genre_missing_from_dictionary**: проверяет, что метод get_books_with_specific_genre возвращает пустой список, если книги с указанным жанром нет в коллекции
- **test_get_books_with_specific_genre_books_wrong_genre**: проверяет, что метод get_books_with_specific_genre возвращает пустой список, если жанр не существует в списке жанров
- **test_get_books_genre_empty_dict**: проверяет, что метод get_books_genre возвращает пустой словарь, если нет книг в коллекции
- **test_get_books_genre_not_empty_dict**: проверяет, что метод get_books_genre возвращает словарь, если есть книги в коллекции.
- **test_get_books_for_children_adult_books**: проверяет, что метод get_books_for_children возвращает пустой список книг для детей, если в коллекции только взрослые книги.
- **test_get_books_for_children_books_for_children**: проверяет, что метод get_books_for_children возвращает список книг для детей, если в коллекции есть детские книги.
- **test_get_books_for_children_books_mix_books**: проверяет, что метод get_books_for_children возвращает список книг где нет книг для взрослых, если в коллекции есть детские и взрослые книги.
- **test_add_book_in_favorites_book_in_dict**: проверяет, что метод add_book_in_favorites добавляет книгу в избранное, если книга есть в коллекции.
- **test_add_book_in_favorites_book_not_in_dict**:  проверяет, что метод add_book_in_favorites не добавляет книгу в избранное, если книги нет в коллекции.
- **test_add_book_in_favorites_book_in_favorites_two_identical_books**: Тест проверяет, что метод add_book_in_favorites не добавляет книгу в избранное, если она уже есть в избранном.
- **test_delete_book_from_favorites**: проверяет, что метод delete_book_from_favorites удаляет книгу из избранного.

## Тестовое покрытие
```
Name      Stmts   Miss  Cover
-----------------------------
main.py      38      0   100%
-----------------------------
TOTAL        38      0   100%

```