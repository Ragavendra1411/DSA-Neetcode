class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        output=0
        for num in nums:
            length=1
            if num-1 in nums_set:
                continue
            while num+1 in nums_set:
                length+=1
                num+=1
            output = max(output,length)
        return output
            

        