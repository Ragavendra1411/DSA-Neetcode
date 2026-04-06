class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res = []
        n=len(nums)
        nums = sorted(nums)
        while i < n-2:

            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j = i+1
            k = n-1


            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif sum > 0:
                    k-=1
                else: 
                    j+=1
            i+=1
        return res
        