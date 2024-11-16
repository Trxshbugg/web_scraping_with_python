from bs4 import BeautifulSoup
import requests
import re
import time

print('put some skill that you are not familiar with:')
unfamiliar_skill= input('>').split()
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'html.parser')
    jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'Posted 1 day ago' in published_date or 'Posted 2 days ago' in published_date or 'Posted 3 days ago' in published_date:
            
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            skills = job.find('div', class_='srp-skills').text.strip()
            skills = re.sub(r'\s+', ' ', skills)  # Removes all whitespace characters
            more_info = job.header.h2.a['href']


            if not any(skill.lower() in skills.lower() for skill in unfamiliar_skill):

                print(f'''company name : {company_name}''')
                print(f'''skills: {skills}''')
                print(f'''More Info: {more_info}''')
                print('')

if __name__== '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} Minutes..')
        time.sleep(time_wait *60)



 

















'''# Open and process the file inside the 'with open' block
with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all <h5> tags
    
    tags = soup.find_all('h5')

    if tags:
        # Print the text of all <h5> tags
        for tag in tags:
            print(tags)
    else:
        print("No <h5> tag found.")

    course_cards = soup.find_all('div', class_ = "card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')  '''
