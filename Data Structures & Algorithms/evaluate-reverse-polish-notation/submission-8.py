import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandstack=[]
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        for i in range(0,len(tokens)):
            if tokens[i] in ops:
                b = operandstack.pop()
                a = operandstack.pop()
                result = ops[tokens[i]](a, b)
                operandstack.append(result)
            else:
                operandstack.append(int(tokens[i]))
        return operandstack[0]