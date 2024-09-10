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
    
    def jump(self, nums: list[int]) -> int:
        curposition = 0
        nextposition = 0
        jumptime = 0
        
        for i in range(len(nums) - 1):
            nextposition = max(nextposition, i + nums[i])
            if nextposition >= len(nums) - 1:
                jumptime += 1
                break
            if i == curposition:
                jumptime += 1
                curposition = nextposition

        return jumptime

    def hIndex(self, citations: list[int]) -> int:
        h = len(citations)
        citations.sort()
        for c in citations:
            if c >= h:
                return h
            else:
                h -= 1
        return h 
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        prev = [1] * n
        next = [1] * n
        
        for i in range(1, n):
            prev[i] = prev[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            next[i] = next[i + 1] * nums[i + 1]
        
        answer = [prev[i] * next[i] for i in range(n)]
        
        return answer

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas):
            return -1 
        curGas = 0
        start = 0
        for i in range(len(gas)):
            curGas = curGas + gas[i] - cost[i]
            if curGas < 0:
                curGas = 0
                start = i + 1
        return start
    
    def candy(self, ratings: list[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            elif ratings[i] == ratings[i - 1]:
                candies[i] = candies[i - 1]
            else:
                candies[i] = 1

        for i in range(length, 0):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
            elif ratings[i - 1] == ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i])
            else:
                candies[i] = max(1, candies[i])

        return sum(candies) 

    def romanToInt(self, s: str) -> int:
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        length = len(s)
        #i = 0
        for i in range(0, length):
            if i < length - 1 and table[s[i]] < table[s[i + 1]]:
                ans -= table[s[i]]
            else:
                ans += table[s[i]]
        return ans
    
    def intToRoman(self, num: int) -> str:
        digits =[(1000, "M"),
        (900,"CM"),(500,"D"),(400,"CD"), (100, "C"),  
        (90, "XC"),(50, "L"),(40, "XL"),(10, "X"),
        (9, "IX"),(5, "V"),(4, "IV"),(1, "I")]

        roman_digits = []
        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value) #divmod 函数会返回 num 除以 value 的商和余数，count 是商，num 是余数。count 表示当前数字可以由几个 value 组成
            roman_digits.append(symbol*count)
        return "".join(roman_digits)
    
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(' ')
        return len(s[- 1])
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ''
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        minLen = len(min(strs, key=len))
        for i in range(minLen):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans
    
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [c for c in s if c != '']
        ans = []
        for i in range(len(s) - 1, -1, -1):
            ans.append(s[i])
        return ' '.join(ans)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        ans = [[] for _ in range(numRows)]
        res = []
        indx = 0
        step = 1
        for i in s:
            ans[indx].append(i)
            
            indx += step
            if indx == numRows - 1 or indx == 0:
                step = -step
        for a in ans:
            res.append(a)
        res = [j for i in ans for j in i]
        return ''.join(res)
    
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        hlen = len(haystack)
        ans = -1
        if nlen > hlen:
            return ans
        for i in range(hlen):
            if haystack[i] == needle[0]:
                j = 0
                while j < nlen and i + j < hlen:
                    if haystack[i + j] == needle[j]:
                        j += 1
                    else:
                        break
                if j == nlen:
                    return i
        return ans

