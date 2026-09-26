class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result_list = list()
        for num in range(len(nums)):

            if target - nums[num] in dic:
                
                result_list.append(dic[target- nums[num]])
                result_list.append(num)

            dic[nums[num]] = num

        return result_list
        