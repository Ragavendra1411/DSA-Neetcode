class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        # Bubble sort
        for i in range(1,len(nums)):
            for j in range(1,len(nums)):
                if nums[j]<nums[j-1]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1]=temp
        
        return nums


        