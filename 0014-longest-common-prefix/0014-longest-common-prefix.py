class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Loop through characters of the first word
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check if this character matches all other words
            
            for string in strs[1:]:
                if i == len(string) or string[i] != char:
                    # print("67777",strs[0][:i])
                    return strs[0][:i]
            
        return strs[0]
        