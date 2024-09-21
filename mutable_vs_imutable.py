
if __name__ == "__main__":
    # a and b are lists therefore mutable
    a = [1, 2]
    b = [3, 4]
    c = [7, 8]

    # tuple of references for a and b
    t = (a, b)
    print(f"t = ")
    print(t)

    # a and b are mutable, so we can change them
    a.append(3)
    b.append(5)

    # t is a tuple of references to a and b, so it will reflect the changes
    print(t)

    # c is a list, so we can add it to t
    # t is a tuple of references to a and b, so it will reflect the changes
    # t is immutable, so we can't change it therefore we have to create a new tuple
    t = t + (c,)
    print(t)
