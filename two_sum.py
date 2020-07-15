class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        ans = [-1, -1]

        for i, num in enumerate(nums):
            try:
                res[num] = [res[num][0] + 1, i]
            except KeyError:
                res[num] = [1, i]

            for i, num in enumerate(nums):
                diff = target - num
                res[num][0] -= 1

            if diff in res and res[diff][0] > 0:
                ans = i, res[diff][1]

        return ans

