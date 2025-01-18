class MyData:
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other

class DynamicArrays:
    def __init__(self, data, inc_size=10):
        self.inc_size = inc_size
        self.max_size = inc_size
        self.head = [MyData()] * self.inc_size
        self.head[0] = MyData(data)
        self.last_index = 1

    def add(self, data):
         self.head[self.last_index] = MyData(data)
         self.last_index = self.last_index + 1

         # extend array dynamically
         if self.last_index == self.max_size:
             extended = [MyData()] * self.inc_size
             self.max_size = self.max_size + self.inc_size

             self.head = self.head + extended


    def __str__(self):
        result = ""
        for item in self.head:
            if item == None:
                break
            result = result + f"{item}, "

        return result


if __name__ == "__main__":
    myDynamicArray = DynamicArrays(10)
    myDynamicArray.add(20)
    myDynamicArray.add(30)
    myDynamicArray.add(40)
    myDynamicArray.add(50)
    myDynamicArray.add(60)
    myDynamicArray.add(70)
    myDynamicArray.add(80)
    myDynamicArray.add(90)
    myDynamicArray.add(100)

    print(myDynamicArray)

