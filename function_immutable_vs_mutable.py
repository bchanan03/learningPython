import sys

def check_mutability(obj):
    print(f"Inside function: obj reference count: {sys.getrefcount(obj)}")
    if type(obj) == int:
        print(f"Before change: value = {obj}, address {hex(id(obj))}")
        obj = obj + 1
        print(f"After change: value = {obj}, address {hex(id(obj))}")

    if type(obj) == list:
        print(f"Inside function: Before change: value = {obj}, address {hex(id(obj))}")
        obj.append(100)
        print(f"Inside function: After change: value = {obj}, address {hex(id(obj))}")

    if type(obj) == tuple:
        print(f"Inside function: Before change: value = {obj}, address {hex(id(obj))}")
        obj = obj + (100,)
        print(f"Inside function: After change: value = {obj}, address {hex(id(obj))}")

if __name__ == "__main__":
    integerNum = 10
    arrList = [1, 2, 3, 4, 5]
    tuppleNum = (1, 2, 3, 4, 5)

    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(integerNum)}")
    print(f"Outside function: value = {integerNum}, address {hex(id(integerNum))}")
    check_mutability(integerNum)
    print(f"Outside function: value = {integerNum}, address {hex(id(integerNum))}")
    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(integerNum)}")

    print("=============================")
    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(arrList)}")
    print(f"Outside function: value = {arrList}, address {hex(id(arrList))}")
    check_mutability(arrList)
    print(f"Outside function: value = {arrList}, address {hex(id(arrList))}")
    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(arrList)}")

    print("=============================")
    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(tuppleNum)}")
    print(f"Outside function: value = {tuppleNum}, address {hex(id(tuppleNum))}")
    check_mutability(arrList)
    print(f"Outside function: value = {tuppleNum}, address {hex(id(tuppleNum))}")
    print(f"OUTSIDE function: obj reference count: {sys.getrefcount(tuppleNum)}")

