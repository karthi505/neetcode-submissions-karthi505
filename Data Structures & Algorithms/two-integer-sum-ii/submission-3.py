class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length_num = len(numbers)
        answer_list = []
        for i in range(length_num):
            for j in range(i + 1,length_num):
                if numbers[i] + numbers[j] == target:
                    answer_list.append(i + 1)
                    answer_list.append(j + 1)
            
        return answer_list