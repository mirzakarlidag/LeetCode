"""
1079. Letter Tile Possibilities

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""

from collections import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

        def backtrack(counter):
            count = 0
            for tile in counter:
                if counter[tile] > 0:
                    counter[tile] -= 1
                    count += 1 + backtrack(counter)
                    counter[tile] += 1
            return count

        counter = Counter(tiles)
        return backtrack(counter)


sol = Solution()

print(sol.numTilePossibilities("AAB") == 8)
print(sol.numTilePossibilities("AAABBC") == 188)
print(sol.numTilePossibilities("V") == 1)
