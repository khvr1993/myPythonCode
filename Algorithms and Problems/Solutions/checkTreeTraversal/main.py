
# PreOrder : Root Left Right
# Inorder:   Left Root Right
# PostOrder:  Left Right Root
class Solution:
    def checktree(self, preorder, inorder, postorder, N):
        if N == 0:
            return True

        # Your code goes here
        if len(preorder) != len(inorder) or len(preorder) != len(postorder):
            # print("Lengths not equal")
            return False

        if N == 1 and preorder[0] == inorder[0] and preorder[0] == postorder[0]:
            return True

        rootPre = preorder[0]
        rootPostOrder = postorder[-1]

        if rootPre != rootPostOrder:
            return False

        try:
            indexOfRoot = inorder.index(rootPre)
        except:
            indexOfRoot = -1

        if indexOfRoot == -1 :
            return False

        leftSideLength = indexOfRoot
        rightSideLength = len(inorder) - 1 - leftSideLength

        leftSide = True
        rightSide = True

        if leftSideLength > 0:
            leftSide = self.checktree(
                preorder[1:leftSideLength+1], inorder[0:leftSideLength], postorder[0:leftSideLength], leftSideLength)
        if rightSideLength > 0:
            rightSide = self.checktree(preorder[rightSideLength*-1:], inorder[rightSideLength*-1:],
                                       postorder[leftSideLength:leftSideLength+rightSideLength], rightSideLength)

        return leftSide and rightSide


pbm = Solution()
preorder = [3,5]
inorder = [5,3]
postorder = [5,3]
N = 2

print(preorder.index(10))

# op_list = pbm.checktree(preorder, inorder, postorder, N)

# print(op_list)

