class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        index = 0
        answer_list = list()
        for num in nums:
            freq_dict[num] += 1
        
        sorted_items = sorted(freq_dict.items(),key = lambda x : x[1],reverse = True)
        for key,value in sorted_items[:k]:
            answer_list.append(key)

        return answer_list

        




        


