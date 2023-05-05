from typing import List

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr: list, n: int, length: int, capacity: int) -> None:
    if length < capacity:
        arr[length] = n

# Remove from the last position in the array if the array is not empty (i.e. length is non-zero).
def removeEnd(arr: list, length: int) -> None:
    if length > 0:
        # Overwrite last element with some default value.
        # We would also need the length to decreased by 1.
        arr[length - 1] = 0
        length -= 1

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
def insertMiddle(arr: list, i: int, n: int, length: int) -> None:
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n

# Remove value at index i before shifting elements to the left.
# Assuming i is a valid index.
def removeMiddle(arr: list, i: int, length: int) -> None:
    # Shift starting from i + 1 to end.
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # No need to 'remove' arr[i], since we already shifted

def printArr(arr: list, capacity: int) -> None:
    for i in range(capacity):
        print(arr[i])


# leet code problems

# 1. https://leetcode.com/problems/remove-duplicates-from-sorted-array/
def remove_duplicates(nums: List[int]) -> int:
    # Start both index (insert_index, i) from 1
    insert_index = 1
    for i in range(1, len(nums)):
        # Check if the previous element is different from the current element
        if nums[i-1] != nums[i]:
            # Found different then update insert_index in the main array
            nums[insert_index] = nums[i]
            # Incrementing insert_index count by 1
            insert_index += 1
    return insert_index

    # use sorted
    nums[:] = sorted(set(nums))
    return len(nums)

# 2. https://leetcode.com/problems/remove-element/

def removeElement(nums: List[int], val: int) -> int:
    # Solution 1: Two pointer
    # Two pointers i and j, where i is the slow-runner while j is the fast-runner.
    i = 0
    for j in range(len(nums)):
        # As long as nums[j] != val, we copy nums[j] to nums[i] and increment both indexes at the same time
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    # Repeat the process until j reaches the end of the array and the new length is i
    return i

    # Solution 2: Two pointer (When elements to remove are rare)
    i = 0
    n = len(nums)
    while i < n:
        # When we encounter nums[i]=val, we can swap the current element out with the last element and dispose the last one.
        # This essentially reduces the array's size by 1.
        if nums[i] == val:
            nums[i] = nums[n-1]
            n -= 1
        else:
            i += 1
    return i

# 3. https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums: List[int], n: int) -> List[int]:
    result = [0] * (2 * n)
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[n + i]
    return result
    # TODO Bit manipulation
