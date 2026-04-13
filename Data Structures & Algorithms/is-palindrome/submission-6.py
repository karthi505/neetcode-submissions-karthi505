class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        new_str = s.replace(" ","")
        improved_str = ""
        for i in new_str:
            if i == '?' or i == '#' or i == '@' or i == "'" or i == ',' or i == '.' or i == ":":
                continue
            else:
                improved_str = improved_str + i

        length = len(improved_str)
        ptr2 = length-1

        print("improved String: ",improved_str)

        if(improved_str == ""):
            return True

        else:
            while(improved_str[ptr1].upper() == improved_str[ptr2].upper()):
                ptr1 = ptr1 + 1
                ptr2 = ptr2 - 1
                if(ptr1 > ptr2):
                    return True

            return False
        