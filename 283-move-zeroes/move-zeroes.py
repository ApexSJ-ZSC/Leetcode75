class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        if nums and 0 not in nums:
            return nums
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1