class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if(len(s) == 1):
            return False

        hashmap = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        open_set = set(["(","[","{"])
        close_set = set([")","]","}"])

        for parameter in s:

            if parameter in open_set:

                stack.append(parameter)

            if parameter in close_set:
                if len(stack) == 0:
                    return False
                    
                value = stack.pop()

                if hashmap[parameter] != value:
                    return False

        return len(stack) == 0

                


