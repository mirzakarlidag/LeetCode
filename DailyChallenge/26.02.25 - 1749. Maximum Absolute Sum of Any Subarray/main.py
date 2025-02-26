"""
1749. Maximum Absolute Sum of Any Subarray

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
 

Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def maxAbsoluteSum(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Track both max and min sums
        max_sum = min_sum = current_max = current_min = 0

        for num in nums:
            # Update max subarray sum
            current_max = max(current_max + num, num)
            max_sum = max(max_sum, current_max)

            # Update min subarray sum
            current_min = min(current_min + num, num)
            min_sum = min(min_sum, current_min)

        # The maximum absolute sum is either the max sum or the absolute value of min sum
        return max(max_sum, abs(min_sum))


sol = Solution()


print(sol.maxAbsoluteSum([1, -3, 2, 3, -4]) == 5)
print(sol.maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8)
