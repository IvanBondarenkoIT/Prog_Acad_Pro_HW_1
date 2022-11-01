# Домашнє завдання 1, 3:
BORDER = "=" * 100

# todo 3.1. Модифікуйте Перше домашнє завдання так,
#  щоб при спробі встановити від'ємну або нульову вартість товару викликалася виняткова ситуація
#  (тип виняткової ситуації треба самостійно реалізувати).
class User_Exception(Exception):
    def __init__(self, text):
        super(User_Exception, self).__init__()
        self.message = text

    def get_exception_message(self):
            return self.message


# todo 1.1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
#  опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
class Product:
    def __init__(self, name: str, description: str, price: float, size: tuple):
        self.name = name
        self.description = description
        try:
            if price < 0:
                raise User_Exception("Negative number value")
            else:
                self.price = price
        except User_Exception as err:
            print(err.get_exception_message())
        except TypeError as err:
            print(f"Incorrect value in price: {price} for product: {name}")
        self.size = size

    def __str__(self):
        return f"prod:{self.name}  discr:{self.description}  price:{self.price}  size:{self.size}"



# todo 1.2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище,
#  ім'я, по батькові, мобільний телефон тощо.
class Customer:
    def __init__(self, full_name: tuple, phone_number: str, other_information: dict):
        self.full_name = full_name
        self.phone_number = phone_number
        self.other_information = other_information

    def __str__(self):
        fio = self.full_name[1] + ' ' + self.full_name[0] + ' ' + self.full_name[2]
        return f"{fio}, phone number:{self.phone_number}"

# todo 1.3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
#  Замовлення має містити дані про користувача, який його здійснив.
#  Реалізуйте метод обчислення сумарної вартості замовлення.
#  Визначте метод str() для коректного виведення інформації про це замовлення.
class Order:
    def __init__(self, customer):
        self.__customer = customer
        self.__products = {}

    def add_product(self, product: Product, quonity):
        if isinstance(product, Product):
            if product in self.__products:
                self.__products[product] += quonity
            else:
                self.__products[product] = quonity

    def __str__(self): #  Визначте метод str() для коректного виведення інформації про це замовлення.
        __str = "Order:\n"
        __str += f"{str(self.__customer)}\n"
        for prod in self.__products:
            __str += str(prod) + f" Qty - {self.__products[prod]}\n"
        __str += f"Total bill: {self.total_bill()}"
        return __str

    def total_bill(self): #  Реалізуйте метод обчислення сумарної вартості замовлення.
        total = 0
        for product, qty in self.__products.items():
            total += product.price * qty
        return total


products = []
prod_1 = Product(name="bread", description="To eat", price=5.00, size=(3, 3, 3))
products.append(prod_1)
prod_2 = Product(name="solt", description="To eat", price=3.00, size=(2, 2, 2))
products.append(prod_2)
prod_3 = Product(name="water", description="To drink", price=1.00, size=(1, 1, 1))
products.append(prod_3)

prod_4 = Product(name="water", description="To drink", price=-11.00, size=(1, 1, 1))
products.append(prod_3)

prod_5 = Product(name="water", description="To drink", price='bnn', size=(1, 1, 1))
products.append(prod_3)

print("All products:\n" + f"\n".join(map(str, products)))
print(BORDER)


customers = []
customer1 = Customer(full_name=("Ivan", "Ivanov", "Jovanovich"), phone_number="123456",
                     other_information={"email": "asd@asd.com",
                                        "address": "Ukraine, Kherson"})
customer2 = Customer(full_name=("Petro", "Petrov", "Petrovich"), phone_number="456789",
                     other_information={"email": "qwe@qwe.com",
                                        "address": "Georgia, Batumi",
                                        "telegram": "@progacad"})
customers.append(customer1)
customers.append(customer2)

order_1 = Order(customer=customers[1])
order_1.add_product(product=products[0], quonity=5)
order_1.add_product(product=products[1], quonity=3)
order_1.add_product(product=products[0], quonity=2)
'''order_1 = Order(customer=customers[1])
order_1.add_product(product=products[0], quonity=5)
order_1.add_product(product=products[1], quonity= 3)
'''

order_2 = Order(customer=customers[0])
order_2.add_product(product=products[0], quonity=4)
order_2.add_product(product=products[2], quonity=2)

print(order_1)
print(BORDER)
print(order_2)
print(BORDER)

