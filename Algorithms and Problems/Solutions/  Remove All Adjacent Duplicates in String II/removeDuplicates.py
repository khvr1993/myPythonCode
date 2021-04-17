class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them causing the left and the right side of the deleted substring to concatenate together.

        We repeatedly make k duplicate removals on s until we no longer can.

        Return the final string after all such duplicate removals have been made.

        It is guaranteed that the answer is unique.
        Solution :
        1. Initialize stack and keep inserting each letter in
        2. keep track of the count of elements being inserted.
        3. If count reaches k then pop the values and make the count of chars to 0
        4. repeat the process until dups are not found

        Refer https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/ for more optimized way
        """
        print(f"Provided String {s} with k => {k}")
        def initialize_dict():
            chars = {   "a" : 0,
                    "b":  0,
                    "c" : 0,
                    "d":  0,
                    "e" : 0,
                    "f":  0,
                    "g" : 0,
                    "h":  0,
                    "i" : 0,
                    "j":  0,
                    "k" : 0,
                    "l":  0,
                    "m" : 0,
                    "n":  0,
                    "o" : 0,
                    "p":  0,
                    "q" : 0,
                    "r":  0,
                    "s" : 0,
                    "t":  0,
                    "u" : 0,
                    "v":  0,
                    "w" : 0,
                    "x":  0,
                    "y":  0,
                    "z" : 0
                    }
            return chars

        duplicate_found = True
        stack = []
        while duplicate_found:
            chars = initialize_dict()
            duplicate_found = False
            stack = [s[0]]
            chars[s[0]] += 1
            for i in range(1,len(s)):
                stack.append(s[i])
                chars[s[i]] += 1
                if s[i] != s[i-1]:
                    chars[s[i-1]] = 0
                print(f"No of occurrings for {s[i]} => {chars[s[i]]} STACK => {stack}")
                if chars[s[i]] == k:
                    print(f"Popping the elements")
                    temp = k
                    for _ in range(k):
                        stack.pop()
                    chars[s[i]] -= k
                    duplicate_found = True
                print(f"No of occurrings after popping for {s[i]} => {chars[s[i]]} STACK => {stack}")
            # create the new string to iterate over again to remove k duplicates
            s = "".join(stack)
            print(f"s => {s}")
        return s

pbm = Solution()
s = "abcd"
k = 2
op = pbm.removeDuplicates(s,k)
print(op)