from exception import User_Exception
# todo 1.1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
#  опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
class Product:
    def __init__(self, name: str, description: str, price: float, size: tuple):
        if type(price) != float:
            raise TypeError
        if price < 0:
            raise User_Exception("Negative price value")
        else:
            self.price = price

        self.name = name
        self.description = description
        self.size = size



    def __str__(self):
        return f"prod:{self.name}  discr:{self.description}  price:{self.price}  size:{self.size}"
