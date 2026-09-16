class Solution(object):
    def sortedSquares(self, nums):
        pos = []
        neg = []

        for x in nums:
            if x >= 0:
                pos.append(x ** 2)
            else:
                neg.append(x ** 2)

        neg.reverse()

        i = 0
        j = 0
        m = len(pos)
        n = len(neg)

        merg = []

        while i < m and j < n:
            if pos[i] >= neg[j]:
                merg.append(neg[j])
                j += 1
            else:
                merg.append(pos[i])
                i += 1

        while i < m:
            merg.append(pos[i])
            i += 1

        while j < n:
            merg.append(neg[j])
            j += 1

        return merg