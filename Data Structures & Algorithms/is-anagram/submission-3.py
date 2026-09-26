class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       string1 = {}
       string2 = {}

       for iter1 in s:
        if iter1 in string1:
            string1[iter1] = string1[iter1] +  1
        else:
            string1[iter1] = 1


       for iter2 in t:
        if iter2 in string2:
            string2[iter2] += 1

        else:
            string2[iter2] = 1

        
    
       if string1 == string2:
        return True

       else:
        return False


            

         