class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(0,len(temperatures)):
            while stack and temperatures[i]>stack[-1][1]:
                removed=stack.pop()
                res[removed[0]]=i-removed[0]
            stack.append((i,temperatures[i]))
        return res


