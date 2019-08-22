import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import bs4
import json

companies = [x.lower().split(",")[0] for x in open("companies.txt").read().split("\n")]
#raw_input(companies)

DB = {}

def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def extract_url(stringVal):
	return stringVal.partition('href="')[2].partition('"')[0]

if __name__ == '__main__':
	url = "https://old.reddit.com/r/cscareerquestions/search?q=%5BOFFICIAL%5D+Salary+Sharing+author%3AAutoModerator&restrict_sr=on&include_over_18=on&sort=relevance&t=all"
	
	#url = "https://old.reddit.com/r/cscareerquestions/comments/9cjd6n/official_salary_sharing_thread_for_interns/?limit=500"
	urls = []
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	options = page.select(".search-title")
	for val in options:
		#print val
		g = extract_url(str(val))
		#raw_input(g)
		urls.append(g)
	for url in urls:
		print url
		try:
			res = grabSite(url)
			page = bs4.BeautifulSoup(res.text, 'lxml')
			for val in page.select(".md-container"):
				for x in str(val.getText()).lower().split("\n\n\n"):
					if 'salary' in x and ':' in x:
						value = val.getText().replace("\n\n", "\n")
						comment = val.getText().replace("\n\n", "\n")
						companyName = "unknown"
						for c in companies:
							found = False
							g = value.lower().split()
							for part in c.split():
								#print part
								if part not in g:
									found = False
									break
								else:
									found = True
							if found == True:
								companyName = c
								break
						if companyName not in DB:
							DB[companyName] = []
						information = {"thread": page.title.string, "comment": comment}
						DB[companyName].append(information)
						#print("Predicted company: {}".format(companyName))

						#print("______________")
		except:
			print("ERROR")
	with open('data.json', 'w') as fp:
		json.dump(DB, fp, indent=4)
