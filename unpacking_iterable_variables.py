def sum_of_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def dictionary_output(**kwargs):
    print("Name:", kwargs['name'])
    print("Lastname:", kwargs['lastname'])
    print("Age:", kwargs['age'])
    print("Address:", kwargs['address'])
    print("City:", kwargs['city'])


if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    a, b, c, d, e = l1
    print(a, b, c, d, e)

    l2 = [1, 2, 3, 4, 5, 6]
    a, b, *c = l2
    print(a, b, c)

    a, *b, c = l2
    print(a, b, c)

    a, *b, c, d = l2
    print(a, b, c, d)

    a, b, c, d, e, f = l2
    print(a, b, c, d, e, f)

    # ValueError: not enough values to unpack (expected at least 7, got 6)
    # a, b, c, d, e, f, g = l2
    # print(a, b, c, d, e, f, g)

    l3 = [1, 2, 3, 'python']
    a, b, c, d = l3
    print(a, b, c, d)

    a, b, *c = l3
    print(a, b, c)

    a, *b, c = l3
    print(a, b, c)

    l4 = (1, 2, 3, 4, 5)
    a, b, c, d, e = l4
    print(a, b, c, d, e)

    l5 = (1, 2, 3, 4, 5, 6)
    a, b, *c = l5
    print(a, b, c)

    a, *b, c = l5
    print(a, b, c)

    l6 = {1, 2, 3, 4, 5}
    a, b, c, d, e = l6
    print(a, b, c, d, e)

    l7 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    a, b, c, d, e = l7
    print(a, b, c, d, e)

    a, b, c, d, e = l7.values()
    print(a, b, c, d, e)

    a, b, c, d, e = l7.items()
    print(a, b, c, d, e)

    print("Iterating over dictionary")
    for item in l7.items():
        print(f"key: {item[0]}, value: {item[1]}")

    print("Iterating over dictionary using unpacking")
    for (key, value) in l7.items():
        print(f"key: {key}, value: {value}")

    print("Iterating over dictionary using unpacking")
    for key, value in l7.items():
        print(f"key: {key}, value: {value}")

    l8 = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
    l9 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    d = {**l8, **l9}
    print(d)
    d = {**l9, **l8}
    print(d)

    print(sum_of_numbers(1, 2, 3, 4, 5))
    print(sum_of_numbers(1, 2, 3))
    dictionary_output(name="Chanan", lastname="Berler", age=49, address="Hanotea 25", city="Tel Mond")