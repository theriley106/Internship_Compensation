# Fix comments all
import json

a = json.load(open("data2.json"))

g = json.load(open("dataBackup.json"))

new = dict(a)

for k, v in a.iteritems():
	for index, commentInfo in enumerate(v):
		for _, b in g.iteritems():
			for i, val in enumerate(b):
				#print val
				#print commentInfo
				if val['comment'].strip().split("\n")[0] == commentInfo['comment'].strip().split("\n")[0]:
					print("FIXED")
					new[k][index]['comment'] = val['comment']
					break

with open('fixed2.json', 'w') as fp:
	json.dump(new, fp, indent=4)
