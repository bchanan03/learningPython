from functools import reduce


def simple_math(x, y, operator = "+"):
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    return operators[operator](x, y)

def simple_addition_array(lst):
    return reduce(lambda x,y: x*y, lst)

def filter_array(lst):
    return  list(filter(lambda n: n % 2 == 0, lst))

if __name__ == "__main__":
    print(simple_math(5, 3, "*"))
    print(simple_addition_array([1, 2, 3, 4, 5]))

    print(filter_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

