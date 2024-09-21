class LongSusbtring:
    def findTheLongestSubstring(self, s: str) -> int:
        # Potential approach: sliding window     
        # a = s.count('a') % 2
        # e = s.count('e') % 2
        # i = s.count('i') % 2
        # o = s.count('o') % 2
        # u = s.count('u') % 2
        
        # if a == 0 and e == 0 and i == 0 and o == 0 and u == 0:
        #     return len(s)
        
        # return max(
        #     self.findTheLongestSubstring(s[1:]), self.findTheLongestSubstring(s[:-1])
        # )
        
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        res = 0
        map = [-1] * 32
        map[0] = 0
        mask = 0
        for i, c in enumerate(s):
            if c in vowels:
                mask ^= vowels[c]
            if map[mask] != -1:
                res = max(res, i + 1 - map[mask])
            else:
                map[mask] = i + 1
        return res
    # Explanation:
    # we can keep track of the mask of the substring using a 5-bit number
    # Mask 0: 00000 -> no vowels
    # Mask 1: 00001 -> 'a'
    # Mask 2: 00010 -> 'e'
    # Mask 4: 00100 -> 'i'
    # Mask 8: 01000 -> 'o'
    # Mask 16: 10000 -> 'u'
    # if we find a vowel, we toggle the corresponding bit in the mask
    # this works because the mask is a 5-bit number, and there are only 32 possible values for the mask
    # so we can use an array of size 32 to store the index of the first occurrence of each mask
    # if we find the same mask again, we can calculate the length of the substring by subtracting the index of the first occurrence from the current index
    # we keep track of the maximum length of the substring and return it at the end
    
        
        
if __name__ == '__main__':
    ls = LongSusbtring()
    print(ls.findTheLongestSubstring("eleetminicoworoep")) # 13
    print(ls.findTheLongestSubstring("leetcodeisgreat")) # 5