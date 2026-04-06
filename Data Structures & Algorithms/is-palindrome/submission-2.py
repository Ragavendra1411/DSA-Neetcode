class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j = 0,len(s)-1
        s=s.lower()
        print(s)
        while i<=j:
            if s[i]==" " or not s[i].isalnum():
                i+=1
                continue
            if s[j]==" " or not s[j].isalnum():
                j-=1 
                continue
            print("I and J for comp are",s[j],s[i])
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        