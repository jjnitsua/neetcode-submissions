class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c=='(' or c=='{' or c=='[' :
                stack.append(c)
            elif stack!=[]:
                check=stack.pop()
                if c==')' and check!='(':
                    return False
                if c=='}' and check!='{':
                    return False
                if c==']' and check!='[':
                    return False
            else:
                return False
        if stack==[]:
            return True
        else:
            return False