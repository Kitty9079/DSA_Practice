class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    if i == "+":
                        stack.append(num1+num2)
                    elif i == "-":
                        stack.append(num2-num1)
                    elif i == "*":
                        stack.append(num2*num1)
                    else:
                        res = num2/num1
                        if res < 0 :
                            res = math.ceil(res)
                        else:
                            res = math.floor(res)
                        stack.append(res)
        return stack[0]