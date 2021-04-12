class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        https://leetcode.com/problems/length-of-last-word/
        Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

        A word is a maximal substring consisting of non-space characters only.

        In python we have split function to split the string
        If we dont want to use it in we need to iterate through the string. Check if atleast one space
        has occurred. Whenever space has occurred then move your pointer to the position since we need to get the last word
        """

        word = s.split()
        if word == []:
            return 0
        else :
            return len(word[-1])

pbm = Solution()
s = "Hello World"
op = pbm.lengthOfLastWord(s)
print(op)



