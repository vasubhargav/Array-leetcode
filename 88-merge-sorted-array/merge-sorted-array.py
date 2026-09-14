class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        lst = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                lst.append(nums1[i])
                i += 1
            else:
                lst.append(nums2[j])
                j += 1

        while i < m:
            lst.append(nums1[i])
            i += 1

        while j < n:
            lst.append(nums2[j])
            j += 1

        nums1[:] = lst