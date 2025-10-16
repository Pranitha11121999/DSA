class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_num = 0
        for i in range(len(nums)):
            sum_num = sum_num + nums[i]
            if sum_num > max_sum:
                max_sum = sum_num
            if sum_num <0:
                sum_num = 0
        return max_sum