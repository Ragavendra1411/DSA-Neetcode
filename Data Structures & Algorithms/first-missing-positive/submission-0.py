class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i=0
        # place the positive numbers in their actual index by swapping
        while i<n:
            if nums[i]<=0 or nums[i]>n:
                i+=1
                continue
            actual_index = nums[i]-1
            if nums[i] != nums[actual_index]:
                nums[i],nums[actual_index]= nums[actual_index],nums[i]
            else:
                i+=1

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1


