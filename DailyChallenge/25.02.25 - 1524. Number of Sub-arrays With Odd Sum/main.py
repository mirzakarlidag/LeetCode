"""
1524. Number of Sub-arrays With Odd Sum

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
"""


class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        num_of_odd_sub_arrs = 0
        odds = []
        evens = []

        for num in arr:
            if num % 2:
                odds.append(num)
            else:
                evens.append(num)

        if len(odds) == 0:
            return 0

        def get_sum_of_arr(arr):
            sum = 0
            for num in arr:
                sum += num
            return sum

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if get_sum_of_arr(arr[i : j + 1]) % 2:
                    num_of_odd_sub_arrs += 1

        return num_of_odd_sub_arrs


sol = Solution()
print(sol.numOfSubarrays([1, 3, 5]) == 4)
print(sol.numOfSubarrays([2, 4, 6]) == 0)
print(sol.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]) == 16)
