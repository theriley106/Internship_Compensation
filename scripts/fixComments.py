# Fix comments all
import json

a = json.load(open("data2.json"))

b = json.load(open("dataBackup.json"))

new = dict(b)

for k, v in a.iteritems():
	for commentInfo in v:
		for i, val in enumerate(b[k]):
			#print val
			#print commentInfo
			if val['comment'].split("\n")[0] == commentInfo['comment'].split("\n")[0]:
				print("FIXED")
				new[k][i]['comment'] = val['comment']

with open('fixed.json', 'w') as fp:
	json.dump(new, fp, indent=4)
