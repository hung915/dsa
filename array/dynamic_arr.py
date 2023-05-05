from typing import List

# Python arrays are dynamic by default, but this is an example of resizing.
class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2 # Array of capacity = 2

    # Insert n in the last position of the array
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def resize(self):
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # Copy elements to newArr
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # Remove the last element in the array
    def popback(self):
        if self.length > 0:
            self.length -= 1

    # Get value at i-th index
    def get(self, i):
        if i < self.length:
            return self.arr[i]
        # Here we would throw an out of bounds exception

    # Insert n at i-th index
    def insert(self, i, n):
        if i < self.length:
            self.arr[i] = n
            return
        # Here we would throw an out of bounds exception

    def print(self):
        for i in range(self.length):
            print(self.arr[i])
        print()


# Leet code problems
# 1. https://leetcode.com/problems/concatenation-of-array/
def getConcatenation(nums: List[int]) -> List[int]:
        size = len(nums)
        sol = [0] * 2 * size
        for i in range(size):
            sol[i] = sol[i+size] = nums[i]
        return sol

        return nums + nums
        return nums * 2