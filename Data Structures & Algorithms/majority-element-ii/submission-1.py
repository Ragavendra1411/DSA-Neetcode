class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # boyre moore voting algo
        count = defaultdict(int)
        output=[]
        for num in nums:
            count[num]+=1

            # if length of dict is less than2, its fine
            if len(count)<=2:
                continue

            # if more than 2, decrement all count by 1 and 
            # remove elements with 0 count
            newcount=defaultdict(int)
            for k,v in count.items():
                v-=1
                if v!=0:
                    # count.pop(k) == cannot directly pop since dict cannot be changed during iteration
                    newcount[k]=v
            count=newcount
        print(count)
        for num in count.keys():
            if nums.count(num)>len(nums)//3:
                output.append(num)
        return output


        
        