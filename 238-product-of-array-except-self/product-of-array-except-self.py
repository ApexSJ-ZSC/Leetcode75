class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [1] * len(nums) #[1,1,2,6]

        for i in range(len(nums)):
            res[i] *= pre # pre = 12
            pre *= nums[i] #res = [1,1,2,6]

        for j in range(len(nums)-1, -1, -1):
            res[j] *= post # [24,12,8,6]
            post *= nums[j]

        return res