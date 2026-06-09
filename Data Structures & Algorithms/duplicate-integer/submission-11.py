class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            s.add(num)
            print(len(s))
            print(len(nums))
        return len(s) != len(nums)