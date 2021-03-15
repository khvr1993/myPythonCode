#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

inp = str(input())

#Normal Way
# count_of_z = inp.count('z')
# count_of_o = inp.count('o')

#Using Lambda function
count_of_z = sum(map(lambda x : 1 if 'z' in x else 0, inp))
count_of_o = sum(map(lambda x : 1 if 'o' in x else 0, inp))


if 2*count_of_z == count_of_o:
  print('Yes')
else:
  print('No')