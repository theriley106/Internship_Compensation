# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import json
xVal = json.load(open('fixed3.json'))
companies = []

for k, v in xVal.iteritems():
	for val in v:
		if "INTERNS" in val['thread'].upper():
			if k != "none" and k != "unknown" and k != "all":
				companies.append(k)
			break

companies.sort()
companyList = open("companies.txt").read().split("\n")

def get_correct_case(string):
	for val in companyList:
		if val.strip().lower() == string.strip().lower():
			return val
	return string

os.system("touch tempREADME2.md")
readme = '''

Company Table of Contents
=================

<!--ts-->
'''

for k in companies:
	readme += "+ [{}](#{})\n".format(get_correct_case(k), k.replace(" ", "-"))

readme += '''
<!--te-->

'''

with open("tempREADME2.md", "a") as myfile:
	myfile.write(readme)

a = list(json.load(open('fixed3.json')).iteritems())
a.sort(key=lambda k: k[0])

for k, v in a:
	if k.strip() != 'unknown' and k != 'all' and k in companies:
		os.system("echo '## {}\n' >> tempREADME2.md".format(get_correct_case(k)))
		for val in v:
			if "INTERNS" in val['thread'].upper():
				with open("tempREADME2.md", "a") as myfile:
					myfile.write('```' + str(val['comment']) + '\n\n{}\n```\n\n'.format(val['thread'].replace(": cscareerquestions", "").replace("[OFFICIAL] ", "")))