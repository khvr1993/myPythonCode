class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

          An input string is valid if:

          Open brackets must be closed by the same type of brackets.
          Open brackets must be closed in the correct order.

        Solution :
        1. Can be done using stack approach
        2. Initialize dictionary with key as opening bracket and val as closing bracket
        3. when key is encountered push
        4. when val is encountered pop
        5. compare the dict[key] and val
        6. if any mismatch then return false
        7. if stack is not empty return false
        8. if stack is empty before the characters complete return false

        """

        dict = {"]": "[", ")": "(", "}": "{"}
        stack = []
        for chars in s:
            # print(f"Working on the character {chars}")
            if chars in dict.values():
                # print("Pushing onto stack")
                stack.append(chars)
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                # print(f"Popped Value {val}")

                if dict[chars] != val:
                    return False

        if len(stack) > 0:
            return False
        else:
          return True


pbm = Solution()
# s = "()[]{}"
# s= "(]"
s = "[()"
print(pbm.isValid(s))
