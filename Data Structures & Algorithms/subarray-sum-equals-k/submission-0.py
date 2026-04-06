class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=defaultdict(int) #prefix sum
        result=0
        ps[0] = 1
        current_sum=0
        for num in nums:
            current_sum+=num #sum till the current element
            # current_sum = k + some other prefix sum.
            result+= ps.get(current_sum - k,0)
            ps[current_sum]+=1
        return result
        





       


        


        