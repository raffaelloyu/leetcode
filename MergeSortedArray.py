class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #nums1 = nums1[:m]
        #nums2 = nums2[:n]
        for i in range(len(nums1) - 1, m - 1, -1):
            nums1.pop(i)
        print('process nums1:', nums1)
        for i in range(len(nums2) - 1, n - 1, -1):
            nums2.pop(i)
        print('process nums2:', nums2)
        i = 0
        j = 0
        if m != 0 and n != 0:
            while i < m and j < n:
                if nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    j += 1
                    m += 1
                elif nums1[i] <= nums2[j]:
                    i += 1
            if i == m: # means the last one in nums1, directly add the remains of nums2 to the tail of nums1
                for j in range(j, n):
                    nums1.append(nums2[j])
        if m == 0:
            for j in range(0, n):
                nums1.insert(j, nums2[j])
        print('after merge:', nums1)
