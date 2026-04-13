class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Iterate through each character in the string
        for i in s:
            if i not in [')', ']', '}']:  # If it's an opening bracket
                stack.append(i)
            else:  # If it's a closing bracket
                if len(stack) == 0:  # Check for unmatched closing bracket
                    return False
                
                check = stack.pop()  # Pop the last opening bracket from the stack
                
                # Check if the closing bracket matches the last opening bracket
                if i == '}':
                    if check != '{':
                        return False
                elif i == ']':
                    if check != '[':
                        return False
                elif i == ')':
                    if check != '(':
                        return False

        # At the end, the stack should be empty if all brackets are matched
        return len(stack) == 0
