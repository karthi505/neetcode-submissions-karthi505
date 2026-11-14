
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = list()

        for num in tokens:

            if num not in ['+', '-', '*', '/']:
                st.append(int(num))

            else:
                if(len(st) > 1):
                    dig2 = int(st.pop())
                    dig1 = int(st.pop())

                    if(num == '+'):

                        result = dig1 + dig2
                        st.append(result)
                    elif(num == '-'):

                        result = dig1 - dig2
                        st.append(result)
                    elif(num == '*'):

                        result = dig1 * dig2
                        st.append(result)
                    elif(num == '/'):

                        if(dig2 == 0):
                            return -1
                        else:
                            result = int(dig1 / dig2)
                            st.append(result)

        return(st[0])
