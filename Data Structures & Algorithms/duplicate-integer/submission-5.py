class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        
        freq_list = freq_dict.values()

        if max(freq_list) > 1:
            return True
        else:
            return False
        

       