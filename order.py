from product import Product


class OrderIterator:
    def __init__(self, wrapped, wrapped_2):
        self.wrapped = wrapped
        self.wrapped_2 = wrapped_2
        self.index = 0

    def __next__(self):
        if self.index < len(self.wrapped) or self.index < len(self.wrapped_2):
            self.index = self.index + 1
            return (self.wrapped[self.index - 1], self.wrapped_2[self.index - 1])
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Order:
    def __init__(self, customer):
        self.__customer = customer
        self.__products = []
        self.__qty = []
        self.number = 0

    def add_product(self, product: Product, quonity):
        if isinstance(product, Product):
            if product in self.__products:
                self.__qty[self.__products.index(product)] += quonity
            else:
                self.__products.append(product)
                self.__qty.append(quonity)
                self.number += 1

    def __str__(self): #  Визначте метод str() для коректного виведення інформації про це замовлення.
        __str = "Order:\n"
        __str += f"{str(self.__customer)}\n"
        for idx in range(len(self.__products)):
            __str += str(self.__products[idx]) + f" Qty - {self.__qty[idx]}\n"
        __str += f"Total bill: {self.total_bill()}"
        return __str

    def total_bill(self): #  Реалізуйте метод обчислення сумарної вартості замовлення.
        total = 0
        for idx in range(len(self.__products)):
            total += self.__products[idx].price * self.__qty[idx]
        return total

    def __iter__(self):
        return OrderIterator(self.__products, self.__qty)

    def __getitem__(self, index):
        if isinstance(index, slice):
            __start = 0 if index.start == None else index.start
            __stop = self.number - 1 if index.stop == None else index.stop
            __step = 1 if index.step == None else index.step
            if __start < 0 or __stop > self.number:
                raise IndexError
            else:
                result = []

            for i in range(__start, __stop, __step):
                result.append((self.__products[i], self.__qty[i]))
            return result
        if isinstance(index, int):
            if index < self.number:
                return (self.__products[index], self.__qty[index])
        else:
            raise IndexError
        raise TypeError()

    def __len__(self):
        return self.number
