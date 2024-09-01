import numpy as np

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

    def removeElement(self, nums: list[int], val: int) -> int:
        print("before: ", nums)
        while val in nums:
            nums.remove(val)
        print("removed: ", nums)

    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        i = 0
        while i < l:
            c = nums.count(nums[i])
            if c > 1:
                for _ in range(0, c - 1):
                    nums.remove(nums[i])
                l = l - c + 1
            i += 1

    def removeDuplicatesII(self, nums: list[int]) -> int:
        l = len(nums)
        i = 0
        while i < l:
            c = nums.count(nums[i])
            if c > 2:
                for _ in range(0, c - 2):
                    nums.remove(nums[i])
                l = l - c + 2
            i += 1
            
    def majorityElement(self, nums: list[int]) -> int:
        candicate = 0
        count = 0
        for i in nums:
            if count == 0:
                candicate = i
            if candicate == i:
                count += 1
            else:
                count -= 1
        return candicate

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        step = k if k < length else k % length
        if step == 0:
            return nums
        nums1 = nums[length - step:]
        nums2 = nums[:length - step]
        tar = nums1 + nums2
        nums.clear()
        for i in tar:
            nums.append(i)         

    def maxProfit(self, prices: list[int]) -> int:
        buy = prices[0]
        profit = 0
        if len(prices) == 1:
            return profit
        for sell in prices:
            if sell > buy and sell - buy > profit:
                profit = sell - buy
            elif sell < buy:
                buy = sell
        return profit
    
    def canJump(self, nums: list[int]) -> bool:
        length = len(nums)
        if nums[0] == 0 and length == 1:
            return True
        
        cur = 0
        maxStep = nums[cur]
        if maxStep >= length - 1:
            return True
        success = True

        while success and maxStep > 0:
            
            #if maxStep == 0:
            #    success = False
            #    break
            if nums[cur + maxStep] == 0:
                maxStep -= 1
            else:
                cur = cur + maxStep
                maxStep = nums[cur]
            if maxStep + cur >= length - 1:
                success = False
        return not success