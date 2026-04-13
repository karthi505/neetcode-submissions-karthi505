class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = list()
        ordered_list = list()
        used = [False] * len(strs)
        for i in strs:
            sort_i = ''.join(sorted(i))
            ordered_list.append(sort_i)

        for i in range(len(ordered_list)):
            #if the element has already been checked, it just continues thus skipping a turn cuh
            if used[i]:
                continue
            temp_list = list()
            temp_list.append(strs[i])
            for j in range(i + 1,len(ordered_list)):
                if ordered_list[i] == ordered_list[j]:
                    temp_list.append(strs[j])
                    used[j] = True

            output_list.append(temp_list)
        return output_list