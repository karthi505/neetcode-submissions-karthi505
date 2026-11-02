class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}

        for string in strs:
            index_array = [0] * 26
            
            for character in string:
                index_array[ord(character) - 97] += 1

            key = tuple(index_array)

            if key not in freq:
                freq[key] = []

            freq[key].append(string)

        result = list()
        
        for res in freq.values():
            result.append(res)

        return result
            

