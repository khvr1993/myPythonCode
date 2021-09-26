#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        dict = {}
        maxLen = 0
        prefixSumArray = [None]*n
        prefixSumArray[0] = arr[0]
        dict[prefixSumArray[0]] = 0

        if arr[0] == 0 :
            maxLen = 1

        for i in range(1,n):
            prefixSumArray[i] = prefixSumArray[i-1] + arr[i]

            # If the sum till the current element is 0 then the complete array
            # till that point is the subarray
            if prefixSumArray[i] == 0 :
                maxLen = i + 1

            if prefixSumArray[i] in dict:
                length = i - dict[prefixSumArray[i]]
                if length > maxLen:
                    maxLen = length
            else:
                dict[prefixSumArray[i]] = i

        return maxLen
#{
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends