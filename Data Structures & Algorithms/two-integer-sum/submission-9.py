class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a1 = 0
        a2 = 0
        for num in nums:
            a1 = nums.index(num)
            rem = target - num
            new = nums[a1 + 1:]
            print(new)
            if rem in new:
                    print(a1)
                    a2 = new.index(rem) + a1 + 1
                    return [a1, a2]
        return [a1, a2]
            