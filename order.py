from product import Product


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
