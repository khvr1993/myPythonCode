def pop(stack):
    op = stack.pop(0)
    return op

def isEmpty(stack):
    return True if len(stack) == 0 else False

def push(stack,val):
    stack = stack.insert(0, val)
    # print("contents of Stack After Pushing val ",val,stack)

def Top(stack):
  return int(stack[0])

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    def sorted(self, s):
      print(s)
      newStack = []
      tempStack= []
      while not isEmpty(s):
        val = pop(s)
        if isEmpty(newStack):
          push(newStack,val)
        else:
          while not isEmpty(newStack) and Top(newStack) < val:
            newVal = pop(newStack)
            push(tempStack,newVal)
          push(newStack,val)
          while not isEmpty(tempStack):
            tempVal = pop(tempStack)
            push(newStack,tempVal)

      # print("final new Stack",newStack)
      while not isEmpty(newStack):
        push(s,pop(newStack))
      # print(s)
      return s
        # Code here


#{
#  Driver Code Starts
if __name__=='__main__':

      arr = [11,2,4,5,32]
      ob = Solution()
      ob.sorted(arr)

# } Driver Code Ends