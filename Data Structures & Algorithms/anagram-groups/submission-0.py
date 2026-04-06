class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Iterate through the list and find the freq array of all strings
        # 2. Add the freq array to a output dictionary where indes is the freq array and list of string is the value
        # 3. When new freq array is found, check if already present in dict, yes-> add to the list, no-> add new element in dict
        # 4. Return dict.values()
        output={}
        for str in strs:
            str_freq = self.getFrequencyTable(str)
            sub_array = output.get(str_freq,[])
            sub_array.append(str)
            output[str_freq] = sub_array
        return list(output.values())

    def getFrequencyTable(self,str):
        # if len(str)==0:
        #     return {"":1}
        # freq_table={}
        # for char in str:
        #     freq_table[char]= freq_table.get(char,0)+1
        # NOTE: returning freq table doesnt work since a dictionary cannot be added as a key in another dict.
        # So return a freq array with 26 elements, and frequency of each character in the right index
        freq_array = [0]*26
        for char in str:
            index = ord(char)-ord('a')
            freq_array[index]+=1
        return tuple(freq_array)







        