class Solution:
    def trap(self, height: List[int]) -> int:
        # Handle exceptions
        if not height or len(height)==1: return 0
        
        # declaration
        l,r = 0, len(height)-1
        lmax,rmax = 0,0
        area=0

        # loop with two pointers
        while l<r:
            if height[l] < height[r]:
                if lmax<height[l]:
                    lmax = height[l]
                else:
                    area += lmax-height[l]
                l+=1

            else:
                if rmax > height[r]:
                    area+= rmax-height[r]
                else:
                    rmax = height[r]
                r-=1
        return area



        
        
        


        