"""
Слишком много что писать
"""
class Car:
    """
    Слишком много что писать
    """
    def __init__(self):
        """
        Слишком много что писать    
        """
        self.model = None
        self.year = None
        self.manufacturer = None
        self.engine_capacity = None
        self.color = None
        self.price = None

    def input_data(self):
        """
        Слишком много что писать    
        """
        self.model = input("Введите название модели: ")
        self.year = int(input("Введите год выпуска: "))
        self.manufacturer = input("Введите производителя: ")
        self.engine_capacity = float(input("Введите объем двигателя: "))
        self.color = input("Введите цвет машины: ")
        self.price = float(input("Введите цену: "))

    def output_data(self):
        """
        Слишком много что писать    
        """
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.manufacturer)
        print("Объем двигателя:", self.engine_capacity)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)

    def get_field(self, field):
        """
        Слишком много что писать    
        """
        if field == "model":
            result = self.model
        elif field == "year":
            result = self.year
        elif field == "manufacturer":
            result = self.manufacturer
        elif field == "engine_capacity":
            result = self.engine_capacity
        elif field == "color":
            result = self.color
        elif field == "price":
            result = self.price
        else:
            result = None
        return result

if __name__ == "__main__":
    car = Car()
    car.input_data()
    print("\nДанные о стадионе:")
    car.output_data()

    print("\nДоступ к отдельным полям:")
    field_name = input("Введите поле (model, year, manufacturer, engine_capacity, price): ")
    field_value = car.get_field(field_name)
    if field_value is not None:
        print(f"Значение поля {field_name}: {field_value}")
    else:
        print("Некорректное имя поля")
        