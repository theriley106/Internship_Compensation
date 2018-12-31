import requests
import bs4
import re

API_ENDPOINT = "https://www.bestplaces.net/cost-of-living/{0}-{1}/{2}-{3}/{4}"
'''
0 - Destination City
1 - Destination State
2 - Comparison City
3 - Comparison State
4 - Salary Amount
'''

COMPARISON_CITY = "jacksonville"
COMPARISON_STATE = "fl"
# This is the city we will adjust the salary to

def grab_site(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def extract_num(stringVal):
	return int(''.join(re.findall("\d+", stringVal)))

def adjust_salary(originCity, originState, salary):
	url = API_ENDPOINT.format(originCity, originState, COMPARISON_CITY, COMPARISON_STATE, salary)
	res = grab_site(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	numVals = page.select("strong")
	if len(numVals) == 2:
		return extract_num(numVals[-1].getText())


if __name__ == '__main__':
	print adjust_salary("san-francisco", "ca", 100000)


