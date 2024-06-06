class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Input : longest common prefix flower , flow , flight 

        #output : fl  


        if not strs:
            return ""

        common = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j < len(common) and j < len(strs[i]) and common[j] == strs[i][j]:
                j += 1
            common = common[:j]
            if not common:
                return ""

        return common