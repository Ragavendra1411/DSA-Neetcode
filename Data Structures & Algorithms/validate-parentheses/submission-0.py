class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pair_paranthesis = {")":"(","]" : "[", "}" : "{"}
        for char in s:
            if char in pair_paranthesis:
                if stack and stack[-1]==pair_paranthesis[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return False if stack else True

        


        