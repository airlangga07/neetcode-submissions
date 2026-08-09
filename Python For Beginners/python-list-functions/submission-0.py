from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    count = 0

    for i in nums:
        count += i

    return count

def get_min(nums: List[int]) -> int:
    new_min = nums[0]

    for i in nums:
        if i < new_min:
            new_min = i
    
    return new_min

def get_max(nums: List[int]) -> int:
    new_max = nums[0]

    for i in nums:
        if i > new_max:
            new_max = i
    
    return new_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
