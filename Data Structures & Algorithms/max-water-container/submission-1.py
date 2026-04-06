class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j = 0, n-1
        max_water=0
        while i<j:
            water = (j-i) * min(heights[i],heights[j])
            if  water > max_water:
                max_water = water
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water

        