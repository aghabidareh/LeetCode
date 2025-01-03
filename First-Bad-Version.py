class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n+1
        while left < right:
            mid = (left+right)//2
            if(isBadVersion(mid)):
                if mid == 1 or (mid-1 > 0 and not isBadVersion(mid-1)):
                    return mid
                else:
                    right = mid
            else:
                left = mid+1
        return left