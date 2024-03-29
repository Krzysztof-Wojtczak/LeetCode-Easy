"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6."""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        tail = 0
        for e in nums:
            tail += e
            maxsum = max(tail, maxsum)
            if tail <= 0:
                tail = 0
                
        return maxsum
