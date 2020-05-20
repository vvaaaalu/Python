#Web Scrapper
import requests

indeed_result = requests.get(
"https://www.indeed.com/jobs?q=python&limit=50"
)
