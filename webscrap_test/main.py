from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Java+%2C+Python&txtLocation=')
soup = BeautifulSoup(html_text.text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
   
    job_name = job.find('h3', class_='joblist-comp-name').text.strip()
    skills = job.find('span', class_='srp-skills').text.strip()
    publish_date = job.find('span', class_='sim-posted').span.text.strip()
   
    print(f"""
    Company Name: {job_name}
    Required Skills: {skills}
    Published: {publish_date}
    """)
   



