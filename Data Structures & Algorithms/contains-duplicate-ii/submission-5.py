class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hashmp={}
        for index,val in enumerate(nums):
            if val in hashmp and index - hashmp.get(val) <=k:
                return True
            hashmp[val]=index
        return False


