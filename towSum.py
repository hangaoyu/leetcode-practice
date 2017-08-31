class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i, n in enumerate(nums):
            m = target - n
            if n in buff_dict:
                return [buff_dict[n], i]
            else:
                buff_dict[m] = i


nums = [11, 2, 2, 7, 11, 15]
target = 9
#test
solution = Solution()
print (solution.twoSum(nums, target))
