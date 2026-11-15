class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()

        nums.sort()
        for i,element in enumerate(nums):
            if i > 0 and element == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = nums[i]

            while(left < right):
                summ = element + nums[left] + nums[right]
                if summ == 0:
                    result.append([nums[left],nums[right],target])
                    left = left + 1
                    while(left < right and nums[left] == nums[left - 1]):
                        left = left + 1

                elif(summ > 0):
                    right = right - 1
                elif(summ < 0):
                    left = left + 1

        return result