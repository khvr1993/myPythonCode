class Solution:
    def removeDuplicates(self, S: str) -> str:
        """
        https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

        Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

        We repeatedly make duplicate removals on S until we no longer can.

        Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
        """
        stack = []
        stack.append([S[0],1])
        for i in range(1,len(S)):
            current_char = S[i]

            try:
                top_of_the_stack = stack.pop()
            except:
                top_of_the_stack = None
            print(f"After Pop {top_of_the_stack} and current_char {current_char}")

            if top_of_the_stack and top_of_the_stack[0] == current_char:
                top_of_the_stack[1] += 1
                # stack.append(top_of_the_stack)
            else:
                if top_of_the_stack:
                     stack.append(top_of_the_stack)
                stack.append([S[i],1])
                top_of_the_stack = stack[len(stack) - 1]
            print(stack)

            # if top_of_the_stack[1] == 2:
            #     stack.pop()
        op = ''.join(map(lambda x : x[0],stack))
        # for i in range(len(stack)):
        #     op += stack[i][0]

        return op

pbm = Solution()
S = "abbaca"
op = pbm.removeDuplicates(S)
print(op)