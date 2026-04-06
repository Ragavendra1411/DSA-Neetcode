class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        output=[]
        i=j=0
        while i<n or j<m:
            if i<n:
                output.append(word1[i])
            if j<m:
                output.append(word2[j])
            i+=1
            j+=1
        return "".join(output)
        