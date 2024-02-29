"""
Слишком много что писать    
"""
class Book:
    """
    Слишком много что писать    
    """
    def __init__(self):
        """
        Слишком много что писать    
        """
        self.title = None
        self.year = None
        self.publisher = None
        self.genre = None
        self.author = None
        self.price = None

    def input_data(self):
        """
        Слишком много что писать    
        """
        self.title = input("Введите название книги: ")
        self.year = int(input("Введите год выпуска: "))
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = float(input("Введите цену: "))

    def output_data(self):
        """
        Слишком много что писать    
        """
        print("Название книги:", self.title)
        print("Год выпуска:", self.year)
        print("Издатель:", self.publisher)
        print("Жанр:", self.genre)
        print("Автор:", self.author)
        print("Цена:", self.price)

    def get_field(self, field):
        """
        Слишком много что писать    
        """
        if field == "title":
            result = self.title
        elif field == "year":
            result = self.year
        elif field == "publisher":
            result = self.publisher
        elif field == "genre":
            result = self.genre
        elif field == "author":
            result = self.author
        elif field == "price":
            result = self.price
        else:
            result = None
        return result

if __name__ == "__main__":
    book = Book()
    book.input_data()
    print("\nДанные о стадионе:")
    book.output_data()

    print("\nДоступ к отдельным полям:")
    field_name = input("Введите поле (title, year, publisher, genre, price): ")
    field_value = book.get_field(field_name)
    if field_value is not None:
        print(f"Значение поля {field_name}: {field_value}")
    else:
        print("Некорректное имя поля")
        