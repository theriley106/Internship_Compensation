import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import bs4

companies = [x.lower().split(",")[0] for x in open("companies.txt").read().split("\n")]
#raw_input(companies)
def grabSite(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	return requests.get(url, headers=headers)

def extract_url(stringVal):
	return stringVal.partition('href="')[2].partition('"')[0]

if __name__ == '__main__':
	url = "https://old.reddit.com/r/cscareerquestions/search?q=%5BOFFICIAL%5D+Salary+Sharing&restrict_sr=on&include_over_18=on&sort=relevance&t=all"
	url = "https://old.reddit.com/r/cscareerquestions/comments/9cjd6n/official_salary_sharing_thread_for_interns/?limit=500"
	res = grabSite(url)
	page = bs4.BeautifulSoup(res.text, 'lxml')
	for val in page.select(".md-container"):
		for x in str(val.getText()).lower().split("\n\n\n"):
			if 'salary' in x and ':' in x:
				value = val.getText().replace("\n\n", "\n")
				print val.getText().replace("\n\n", "\n")
				companyName = ""
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
				print("Predicted company: {}".format(companyName))

				print("______________")
