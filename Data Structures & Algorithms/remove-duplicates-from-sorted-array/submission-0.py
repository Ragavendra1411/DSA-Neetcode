class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
        i,j=0,1
        while j <= n-1:
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[i+1]=nums[j]
                i+=1
                j+=1
        while i < n-1:
            nums.pop()
            i+=1
        return len(nums)

        