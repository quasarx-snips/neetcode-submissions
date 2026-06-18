class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(i for i in s if i.isalnum()).lower()
        return string[::-1]==string
        