class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        hash_map = {}
        l = 0
        res = 0
        zeros = 0
        for r in range(len(nums)):
            hash_map[nums[r]] = 1 + hash_map.get(nums[r], 0)
            window = r-l+1
            if hash_map.get(0, 0) <= k:
                res = max(res, window)
            else:
                hash_map[nums[l]] -= 1
                l += 1

        return res
