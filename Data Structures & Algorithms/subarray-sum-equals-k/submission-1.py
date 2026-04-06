class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=defaultdict(int) #prefix sum
        result=0
        ps[0] = 1
        current_sum=0
        for num in nums:
            current_sum+=num #sum till the current element
            # current_sum = k + some other prefix sum.
            # check if the diff exists in the prefix sum dict. if yes - update the count to result
            if current_sum - k in ps:
                result += ps[current_sum - k] 
            ps[current_sum] += 1
        return result
        





       


        


        