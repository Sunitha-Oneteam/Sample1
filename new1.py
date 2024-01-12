# Rename key city to location in the following dictionary

sampleDict = {
  "name": "Abc",
  "age":25,
  "salary": 8000,
  "city": "New York"  }

sampleDict['age']=23
sampleDict['salary']=12000
sampleDict['location']=sampleDict.pop('city')
sampleDict["gender"]="Male"
print(sampleDict)