"""
Слишком много что писать    
"""
class Parent:
    """
    Слишком много что писать    
    """
    def __init__(self, text):
        """
        Слишком много что писать    
        """
        self.text = text

    def set_text(self, text=None):
        """
        Слишком много что писать    
        """
        if text:
            self.text = text
        else:
            self.text = input("Введите текст: ")

    def display_text(self):
        """
        Слишком много что писать    
        """
        print("Текст:", self.text)


class Child(Parent):
    """
    Слишком много что писать    
    """
    def __init__(self, text, number):
        """
        Слишком много что писать    
        """
        super().__init__(text)
        self.number = number

    def set_text_and_number(self, text=None, number=None):
        """
        Слишком много что писать    
        """
        self.set_text(text)
        if number is not None:
            self.number = number
        else:
            self.number = int(input("Введите число: "))

    def display_text_and_number(self):
        """
        Слишком много что писать    
        """
        super().display_text()
        print("Число:", self.number)


if __name__ == "__main__":
    text = input("Введите текст для объекта главного класса: ")
    parent_object = Parent(text)
    parent_object.set_text()
    parent_object.display_text()

    print()

    text = input("Введите текст для объекта класса-потомка: ")
    number = int(input("Введите число для объекта класса-потомка: "))
    child_object = Child(text, number)
    child_object.set_text_and_number()
    child_object.display_text_and_number()
