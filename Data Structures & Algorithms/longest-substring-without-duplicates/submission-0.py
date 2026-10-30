class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlength = 0

        if len(s) == 0:
            return 0

        seen = set()
        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                length = r - l + 1
                if length > maxlength:
                    maxlength = length
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])

        return maxlength
