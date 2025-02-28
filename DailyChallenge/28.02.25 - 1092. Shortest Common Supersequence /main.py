"""
1092. Shortest Common Supersequence 

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 in str2:
            return str2
        if str2 in str1:
            return str1

        if len(str1) < len(str2):
            temp = str1
            str1 = str2
            str2 = temp

        shortest_str = str1 + str2

        for i in range(len(str2)):
            if str2[:i] == str1[-i:]:
                if len(shortest_str) > len(str1 + str2[i:]):
                    shortest_str = str1 + str2[i:]
            elif str2[-i:] == str1[:i]:
                if len(shortest_str) > len(str2 + str1[i:]):
                    shortest_str = str2 + str1[i:]

        return shortest_str


sol = Solution()

print(sol.shortestCommonSupersequence("abac", "cab") == "cabac")
print(sol.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa") == "aaaaaaaa")
print(sol.shortestCommonSupersequence("bbbaaaba", "bbababbb") == "bbbaaababbb")
