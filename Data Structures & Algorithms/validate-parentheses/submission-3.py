class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        condition = False
        for i in s:
            if i not in [')',']','}']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    check = stack.pop()
                    if i == '}':
                        if check == '{':
                            condition = True
                        else:
                            return False
                    elif i == ']':
                        if check == '[':
                            condition = True
                        else:
                            return False
                    else:
                        if check == '(':
                            condition = True
                        else:
                            return False
        return len(stack) == 0



