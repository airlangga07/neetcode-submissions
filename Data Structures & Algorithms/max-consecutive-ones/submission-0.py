class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentMax = 0
        temp = 0
        for num in nums:
            if (num == 1):
                temp += num

                if (temp > currentMax):
                    currentMax = temp
            else:
                temp = 0