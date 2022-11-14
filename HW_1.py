from customer import Customer
from order import Order
from product import Product

# Домашнє завдання 1, 3, 4(refactor to different modules), 6(add ):
BORDER = "=" * 100

# 6.2) Модифицируете класс Заказ (задание Лекции 1) добавив реализацию
# протокола последовательностей и итерационного протокола.
#  3.1. Модифікуйте Перше домашнє завдання так,
#  щоб при спробі встановити від'ємну або нульову вартість товару викликалася виняткова ситуація
#  (тип виняткової ситуації треба самостійно реалізувати).
# 1.1. Створіть клас для опису товару. У якості атрибутів товару можете використовувати значення ціни товару,
#   опису товару, габарити товару. Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# 1.2. Створіть клас "Покупець". У якості атрибутів можна використовувати прізвище,
#  ім'я, по батькові, мобільний телефон тощо.
# 1.3. Створіть клас "Замовлення". Замовлення може містити декілька товарів певної кількості.
#  Замовлення має містити дані про користувача, який його здійснив.
#  Реалізуйте метод обчислення сумарної вартості замовлення.
#  Визначте метод str() для коректного виведення інформації про це замовлення.


if __name__ == "__main__":
    products = []
    prod_1 = Product(name="bread", description="To eat", price=5.00, size=(3, 3, 3))
    products.append(prod_1)
    prod_2 = Product(name="solt", description="To eat", price=3.00, size=(2, 2, 2))
    products.append(prod_2)
    prod_3 = Product(name="water", description="To drink", price=1.00, size=(1, 1, 1))
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
    order_2.add_product(product=products[1], quonity=2)

    print(order_1)
    print(BORDER)
    print(order_2)
    print(BORDER)
    # HW_6
    for item in order_1:
        print(f"prod - {item[0].name}. iter {item}")
    for item in order_2:
        print(f"prod - {item[0].name}. iter {item}")

    print(order_1[0])
    print(order_2[:3:])

