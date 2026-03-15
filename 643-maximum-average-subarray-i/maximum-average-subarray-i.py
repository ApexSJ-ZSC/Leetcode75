class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0
        for i in range(0, k):
            summ += nums[i]
        
        max_sum = summ

        for j in range(k, len(nums)):
            summ += nums[j] - nums[j-k]
            max_sum = max(max_sum, summ)

        return max_sum / k