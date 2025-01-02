class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = {}
        ans = 0
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] in m:
                left = max(left , m[s[i]] + 1)
            right += 1
            m[s[i]] = i
            ans = max(right-left , ans)
        return ans