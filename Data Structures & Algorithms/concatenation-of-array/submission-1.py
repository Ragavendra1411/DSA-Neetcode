class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        l=len(nums)
        for index,num in enumerate(nums):
            ans[index]=num
            ans[l+index]=num
        return ans
        