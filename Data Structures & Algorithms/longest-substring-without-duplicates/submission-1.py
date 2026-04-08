class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # declaration
        hashmap = {}
        l=0
        res=0

        # loop through string s
        for r in range(len(s)):
            if s[r] in hashmap:
                l= max( hashmap.get(s[r])+1,l)
            hashmap[s[r]]=r
            res = max(res,r-l+1)
        return res


        