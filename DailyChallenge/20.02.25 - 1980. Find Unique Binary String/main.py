class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        all_binary_nums = []

        def backtrack(current):
            if len(current) == len(nums):
                all_binary_nums.append(current)
                return

            for char in "01":
                backtrack(current + char)

        backtrack("")

        for num in all_binary_nums:
            if num not in nums:
                return num


sol = Solution()
print(sol.findDifferentBinaryString(["01", "10"]) in ["00", "11"])
print(sol.findDifferentBinaryString(["00", "01"]) in ["11", "10"])
print(
    sol.findDifferentBinaryString(["111", "011", "001"])
    in ["101", "000", "010", "100", "110"]
)
