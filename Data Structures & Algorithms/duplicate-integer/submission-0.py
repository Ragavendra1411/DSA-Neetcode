class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for i in range(len(nums)):
            unique_set.add(nums[i])
        return False if len(unique_set)==len(nums) else True
        
        