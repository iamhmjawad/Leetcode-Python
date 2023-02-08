from collections import Counter


class Solution:
    # solution 1
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            # folowing line tells us that if s[i] is not in countS,
            # then set countS[s[i]] to 0, otherwise, add 1 to countS[s[i]]
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

    # Solution 2    - sort and compare
    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    # Solution 3    - use Counter

    def isAnagram3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
