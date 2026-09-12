class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=0
        stack=[]
        comparison_stack=[]
        counter=0

        pairs = list(zip(position, speed))
        pairs.sort()  # sorts by first element (a)

        position, speed = zip(*pairs)

        position = list(position)
        speed = list(speed)

        for i,d in enumerate(position): 
            dist=target-d
            time=dist/speed[i]
            stack.append(time)
        
        while stack:
            t=stack.pop()
            if comparison_stack:
                if t>comparison_stack[-1]:
                    comparison_stack.append(t)
                    counter+=1
            else:
                comparison_stack.append(t)
                counter+=1

        return counter      


