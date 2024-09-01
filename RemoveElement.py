nums = [3,2,2,3]
val = 3

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        print("before: ", nums)
        while val in nums:
            nums.remove(val)
        print("removed: ", nums)