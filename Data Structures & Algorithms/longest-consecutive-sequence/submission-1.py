class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        counter = 1
        longest = 1
        n = len(nums)

        for i in range(n):
            if nums[i] == nums[i - 1]:
                continue #if duplicate
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            else:
                 counter = 1

            longest = max(longest, counter)
        return longest

        