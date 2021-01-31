import json

try:
  jsonFileOpen = open('/home/harshavardhanreddyk/Downloads/testJson.json')
  jsonFileRead = jsonFileOpen.read()
  jsonData = json.loads(jsonFileRead)
  firstValue = jsonData[0]
  for data_item in jsonData:
    print(data_item['id'],data_item['definition_id'])
# except:
#   print('Some exception Occurred')
finally:
  jsonFileOpen.close()