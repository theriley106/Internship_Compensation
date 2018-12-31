import requests
import bs4

def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

if __name__ == '__main__':
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')


