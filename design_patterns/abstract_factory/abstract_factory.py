class AbstractProduct:
    def operation(self):
        pass


class ConcreteProductA1(AbstractProduct):
    def operation(self):
        print("ConcreteProductA1 operation")


class ConcreteProductA2(AbstractProduct):
    def operation(self):
        print("ConcreteProductA2 operation")


class ConcreteProductB1(AbstractProduct):
    def operation(self):
        print("ConcreteProductB1 operation")


class ConcreteProductB2(AbstractProduct):
    def operation(self):
        print("ConcreteProductB2 operation")


class AbstractFactory:
    def createProductA(self):
        pass

    def createProductB(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def createProductA(self):
        return ConcreteProductA1()

    def createProductB(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def createProductA(self):
        return ConcreteProductA2()

    def createProductB(self):
        return ConcreteProductB2()


def client(factory):
    productA = factory.createProductA()
    productB = factory.createProductB()
    productA.operation()
    productB.operation()


if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    client(factory1)

    factory2 = ConcreteFactory2()
    client(factory2)

        # Output:
        # ConcreteProductA1 operation
        # ConcreteProductB1 operation
        # ConcreteProductA2 operation
        # ConcreteProductB2 operation