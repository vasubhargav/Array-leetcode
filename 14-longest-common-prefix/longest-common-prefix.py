class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        d = ""
        first_word = strs[0]
        
        # Loop through each character index k of the first word
        for k in range(len(first_word)):
            char = first_word[k]
            
            # Check if this character matches at index k across all other words
            for other_word in strs[1:]:
                if k >= len(other_word) or other_word[k] != char:
                    return d  # Stop as soon as there is a mismatch or end of word
            
            # If all words matched at index k, add it to our prefix
            d = d + char
            
        return d