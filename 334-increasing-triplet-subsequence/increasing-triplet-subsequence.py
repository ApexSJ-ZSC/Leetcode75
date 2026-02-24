class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = float('inf')
        r = float('inf')
        for num in nums:
            if num <= l: 
                l = num 
            elif num <= r: 
                r = num 

            else:
                return True
        return False