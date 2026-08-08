class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t1 = list(t)
        for l in s:
            found = False
            for i in range(len(t1)):
                if l==t1[i]:
                    t1.pop(i)
                    found = True
                    break
            if not found:
                return False
        return True