class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return false if both have different lengths
        if len(s)!=len(t):
            return False 

        # populate the frequency dict
        s_freq, t_freq = {},{}
        for i,j in zip(s,t):
            if i in s_freq:
                s_freq[i]= s_freq[i]+1
            else:
                s_freq[i]=1
            if j in t_freq:
                t_freq[j]= t_freq[j]+1
            else:
                t_freq[j]=1

        # compare the frequency dicts
        # for char,freq in s_freq.items():
        #     if s_freq[char]!= t_freq.get(char,0):
        #         return False 
        # return True
        return s_freq==t_freq
        