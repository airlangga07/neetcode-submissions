class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_array = []

        for i in nums:
            if (i == val):
                new_array.append(i)

        for i in range(len(nums) - len(new_array)):
            new_array.append(None)

        nums = new_array
        
        return len(new_array)