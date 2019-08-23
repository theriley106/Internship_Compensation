import json
import os

data = json.load(open("fixed2.json"))
os.system('cp fixed2.json newDataBackup.json')
newData = json.load(open('fixed3.json'))
if len(newData.get('unknown', [])) == 0:
	newData["unknown"] = data['unknown']

if len(newData.get('all', [])) == 0:
	newData["all"] = []

for k, value in data.iteritems():
	for v in value:
		if v not in newData['all'] and "INTERN" in v["thread"].upper():
			print(v["comment"])
			print("\nPredicted company: {}\n".format(k))
			print("______________")
			temp = raw_input("Unknown? ")
			r = len(temp)
			if r == 1:
				print("marked as unknown")
				newData['unknown'].append(v)
			elif r > 1:
				for char in temp.split(","):
					print("saved company as: {}".format(char))
					if char not in newData:
						newData[char] = []
					newData[char].append(v)
			else:
				print("saved company as {}".format(k))
				if k not in newData:
					newData[k] = []
				newData[k].append(v)
			print("______________")
			newData["all"].append(v)
		with open('fixed3.json', 'w') as fp:
			json.dump(newData, fp, indent=4)

