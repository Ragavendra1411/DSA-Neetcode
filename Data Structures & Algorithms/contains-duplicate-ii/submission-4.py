class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # handle constraints
        if k==0: return False

        index_map = {}

        for index,num in enumerate(nums):
            if num in index_map and index - index_map.get(num) <=k:
                return True
            index_map[num]=index
        return False

       

        