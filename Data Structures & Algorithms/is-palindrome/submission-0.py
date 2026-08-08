class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ''.join(char for char in s if char.isalnum())
        print(s_new)
        left = 0
        right = len(s_new) -1 

        while left <= right:
            if s_new[left] != s_new[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True
        