class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sor_s = ''.join(sorted(s))
        sor_t = ''.join(sorted(t))
        if sor_t == sor_s:
            return True
        else:
            return False