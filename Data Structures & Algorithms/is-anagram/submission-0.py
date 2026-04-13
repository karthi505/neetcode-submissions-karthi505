class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        slt = ''.join(sorted(sl))
        tlt = ''.join(sorted(tl))
        if(slt == tlt):
            return True
        else:
            return False