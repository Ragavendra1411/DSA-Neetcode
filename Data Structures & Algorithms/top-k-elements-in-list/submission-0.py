class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={} # dictionary to store the frequency table
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        
        heap=[]
        for val,freq in count.items():
            heapq.heappush(heap,(freq,val))
            if(len(heap)>k):
                heapq.heappop(heap)
        output=[]   
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output



        