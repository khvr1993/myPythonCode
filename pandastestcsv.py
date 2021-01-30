import pandas

dataStream = pandas.read_csv('/home/harshavardhanreddyk/Downloads/testcsvFile.csv',index_col='id')

print(dataStream)

for indx in dataStream.index:
  print(dataStream['name'][indx])