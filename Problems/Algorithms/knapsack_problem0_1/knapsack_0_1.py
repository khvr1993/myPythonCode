from typing import List

def print_table(table : List[int]):
  """Prints the table"""
  for row in table:
    print(row)
  print("------------------------")

class Solution:
  def init_dp_array(self,values : List[int], weight_to_bag: int,dp_array):
    """
      Initializes the dp array for picking 1 item
    """
    for i in range(1):
      for j in range(1,weight_to_bag+1):
        dp_array[i][j] = values[i]


  def knapsack01(self,weight : List[int],values : List[int], weight_to_bag: int ) -> int:
    """

    https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

    Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

    Solution using dp:
      1. build a 2 dimensional array with columns range from 0 - weight_of_bag(including). No of rows = weight(List)
      2. fill the column 0 with all 0's because for weight 0 the value will be 0
      3. For 1 weight the weight than can fill the bag will be itself. Fill it for i = 0
      4. For i = 1 , maximum weight that can be accommodated is equal to
        max(weight without including the current item, value of the current item + what is the value for the remaining weight after we include the current item)

      5. Formula :
        If weight[i] > j then
        T[i,j] = T[i-1,j] -> Cannot include the current weight . Take the previous value only

        T[i,j] = Max(T[i-1,j], value[i] + T[i-1,weight - current item weight])


    """


    # build the dp_array
    len_weight = len(weight)
    len_value = len(values)

    # make a zip for the given lists and sort by weight

    weight_value = list(zip(weight,values))
    sorted_weights = sorted(weight_value,key = lambda x:x[0])
    print_table(sorted_weights)

    # Build dp array

    dp_array = [[0 for _ in range(weight_to_bag+1)] for _ in range (len_weight)]
    print_table(dp_array)

    self.init_dp_array(values , weight_to_bag,dp_array)
    print_table(dp_array)

    # Start filling the array from top to bottom

    i = 1
    while i < len_weight:
      for j in range(1,weight_to_bag+1):
        if sorted_weights[i][0] > j: # weight of the curent element is not able to accommodate
          dp_array[i][j] = dp_array[i-1][j] # not including the current weight what is the value
        else:
          dp_array[i][j] = max(dp_array[i-1][j], sorted_weights[i][1] + dp_array[i-1][j - sorted_weights[i][0]])
      i += 1
    print_table(dp_array)

    return dp_array[len_weight-1][weight_to_bag]



pbm = Solution()


weight = [1,2,3]
values = [10,15,40]
weight_to_bag = 6

op = pbm.knapsack01(weight,values,weight_to_bag)

print(op)

















