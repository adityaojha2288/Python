from bs4 import BeautifulSoup
import requests


print('Put some skills that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
 ).text
soup = BeautifulSoup(html_text, "lxml")
job = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for  jobs in job:
   post = jobs.find("span", class_="sim-posted").text.replace(" ", "")
   company_name = jobs.find("h3", class_="joblist-comp-name").text.replace(" ", "")
   skills = jobs.find("span", class_="srp-skills").text.replace(" ", "")
   more_info= jobs.header.h2.a['href']
   if unfamiliar_skills not in skills:
    
      print(
      f"""
      Company Name: {company_name.strip()}
      Job Posted on : {post.strip()}
      Skills Required : {skills.strip()}
      More Info: {more_info}
      """
      )

     
