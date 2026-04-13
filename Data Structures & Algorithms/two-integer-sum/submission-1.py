class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_arr = []
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(nums[x]+nums[y] == target):
                    index_arr.append(x)
                    index_arr.append(y)

                    return index_arr