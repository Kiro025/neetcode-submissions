class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        tm = {}

        for c in s:
            sm[c] = sm.get(c,0) + 1 

        for c in t:
            tm[c] = tm.get(c,0) + 1

        return sm == tm
 