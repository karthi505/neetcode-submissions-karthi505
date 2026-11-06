class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic = {}
        
        for numbers in nums:
            if numbers in freq_dic:
                freq_dic[numbers] += 1
            else:
                freq_dic[numbers] = 1
            
        arr = []
        for (key,value) in freq_dic.items():
            arr.append([key,value])

        arr.sort(key=lambda x : x[1])
        
        result = []
        while(len(result) < k):
            result.append(arr.pop()[0])

        return result
        
        #for keys in freq_dic:
         #   if freq_dic[keys] >= k:
          #      answer_list.append(keys)






        