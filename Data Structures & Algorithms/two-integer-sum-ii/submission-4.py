# Two Pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length_num = len(numbers)
        answer_list = []
        low = 0
        high = length_num - 1
        while low < high:
            summ = numbers[low] + numbers[high]
            if summ > target:
                high -= 1
            elif summ < target:
                low += 1
            elif summ == target:
                answer_list.append(low + 1)
                answer_list.append(high + 1)
                low += 1
                high -= 1

            

        return answer_list
