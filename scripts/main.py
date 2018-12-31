import requests
import bs4

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

def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

if __name__ == '__main__':
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')


