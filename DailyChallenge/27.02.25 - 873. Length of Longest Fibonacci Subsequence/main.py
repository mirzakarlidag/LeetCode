"""
873. Length of Longest Fibonacci Subsequence

A sequence x1, x2, ..., xn is Fibonacci-like if:

n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

Example 1:

Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 

Constraints:

3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109
"""


class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_length = 0

        def is_fibo(arr):
            for i in range(len(arr) - 2):
                if arr[i + 2] != arr[i] + arr[i + 1]:
                    return False
            return True

        for cursor in range(len(arr) - 2):
            for end in range(cursor + 2, len(arr)):
                if is_fibo(arr[cursor : end + 1]):
                    print(arr[cursor : end + 1])
                    max_length = max(max_length, len(arr[cursor : end + 1]))
        return max_length


sol = Solution()

print(sol.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5)
print(sol.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3)
