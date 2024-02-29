"""
Слишком много что писать    
"""
class Stadium:
    """
    Слишком много что писать    
    """
    def __init__(self):
        """
        Слишком много что писать    
        """
        self.name = None
        self.opening_date = None
        self.country = None
        self.city = None
        self.capacity = None

    def input_data(self):
        """
        Слишком много что писать    
        """
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = int(input("Введите вместимость: "))

    def output_data(self):
        """
        Слишком много что писать    
        """
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)

    def get_field(self, field):
        """
        Слишком много что писать    
        """
        if field == "name":
            result = self.name
        elif field == "opening_date":
            result = self.opening_date
        elif field == "country":
            result = self.country
        elif field == "city":
            result = self.city
        elif field == "capacity":
            result = self.capacity
        else:
            result = None
        return result
if __name__ == "__main__":
    stadium = Stadium()
    stadium.input_data()
    print("\nДанные о стадионе:")
    stadium.output_data()

    print("\nДоступ к отдельным полям:")
    field_name = input("Введите поле (name, opening_date, country, city, capacity): ")
    field_value = stadium.get_field(field_name)
    if field_value is not None:
        print(f"Значение поля {field_name}: {field_value}")
    else:
        print("Некорректное имя поля")
