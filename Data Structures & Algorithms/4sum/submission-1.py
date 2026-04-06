class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(0,len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                c=j+1
                d=len(nums)-1
                while c<d:
                    if nums[i]+nums[j]+nums[c]+nums[d] > target:
                        d-=1
                    elif nums[i]+nums[j]+nums[c]+nums[d] < target:
                        c+=1
                    else:
                        res.append([nums[i],nums[j],nums[c],nums[d]])
                        c+=1
                        while c<d and nums[c]==nums[c-1]:
                            c+=1
        return res



        


            
        
        