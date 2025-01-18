class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

class SortedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current = self.head
            previous = None
            while current and current.value < value:
                previous = current
                current = current.next
            if previous is None:
                new_node.next = self.head
                self.head = new_node
            else:
                new_node.next = current
                previous.next = new_node

    def __str__(self):
        return_value = ""
        current = self.head
        while current:
            return_value = return_value + f"{current.value} -> "
            current = current.next
        return return_value

def check_two_sum(nums, target):
    d = {}

    for i, num in enumerate(nums):
        print(f"i: {i}, num: {num}")
        for j in range(i+1, len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    print(f"{nums[i]} + {nums[j]} == {target}")


def missing_number(nums):
    n = len(nums)
    return (n + 1) * (n + 2) // 2 - sum(nums)


def contains_duplicate(nums):
    return len(nums) != len(set(nums))


def max_sub_array(nums):
    max_sum = 0
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            print([d[target - num], i])
        d[num] = i


def pascal(n):
    if n == 0:
        return [1]
    else:
        N = pascal(n-1)
        return [1] + [N[i] + N[i+1] for i in range(n-1)] + [1]


if __name__ == '__main__':
    # arr = [7,8,1,9,6,4,5,3]
    # print(missing_number(arr))


    # # myLinkedList = SortedLinkedList()
    # # myLinkedList.add(1)
    # # myLinkedList.add(4)
    # # myLinkedList.add(5)
    # # myLinkedList.add(2)
    # # print(myLinkedList)
    #
    # # check_two_sum([2, 3, 7, 1, 4, 11, 15,1,4], 5)
    # print(missing_number([0,1,2,4,5,6,7,8,9,10]))
    # # print(contains_duplicate([1,2,3,2,5,6,7,8,9,10]))
    # # print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    # # two_sum([2, 7, 11, 15], 18)
    # # print(pascal(5))
