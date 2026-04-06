class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # nlogn sorted solution
        people.sort()
        i,j = 0, len(people)-1
        res=0
        while i<j:
            weight = people[i]+people[j]
            if weight<=limit:
                res+=1
                i+=1
                j-=1
            else:
                res+=1
                j-=1
        if i==j:
            res+=1
        return res



        