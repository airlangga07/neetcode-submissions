class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # there are 2 ways to do this
        
        # 1st solution
        # new array only for the non targeted val
        # e.g. array [3,2,2,3] val is 3
        # iterate the arrays such that for each num that is not val
            # push to new array
        
        # result [2,2]
        
        # another loop that fills in the remaining array with None 
        # with the same length as val or remaining array length
        
        new_array = []

        for i in nums:
            if (i == val):
                new_array.append(i)
        
        print(new_array)
