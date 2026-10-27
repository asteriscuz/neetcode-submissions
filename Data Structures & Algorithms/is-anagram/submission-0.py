class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        counts1 = Counter(s)
        counts2 = Counter(t)
        if counts1 == counts2:
            return True
        else:
            return False