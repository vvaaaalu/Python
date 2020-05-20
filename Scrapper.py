#Web Scrapper
import requests
from bs4 import BeautifulSoup
URL="https://www.indeed.com/jobs?q=python&limit=50"
#definition
def extract_indeed_pages():
indeed_result = requests.get(
"https://www.indeed.com/jobs?q=python&limit=50"
)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class":"pagination"})

links = pagination.find_all('a')
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max=pages[-1]

for n in range(max):
    print(f"start={n*50}")

def extract_indeed_jobs(last_page):
    jobs=[]
    #for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    resluts=soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
        title = result.find("div", {"class":"title"}).find("a")["title"]
    return jobs

last_indeed_page=extract_indeed_pages()
indeed_jobs=extract_indeed_jobs(last_indeed_page)
