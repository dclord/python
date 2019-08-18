from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime as dt
import mysql.connector as maria
import time

"""
Sites: 
DONE - SQL - Elite Telecom - https://elitegroup.com/careers/current-opportunities/ 
DONE - SQL - Gamma Telecom -  https://gamma.co.uk/about-us/careers/
DONE - SQL - UKFast - https://ukfast.co.uk/careers.html
DONE - SQL - Chess - https://chessict.co.uk/culture/join-us/
ONGOING - SQL - Daisy - Selenium - https://careers.smartrecruiters.com/DaisyGroup1
DONE - SQL - TalkTalk - https://careers.talktalk.co.uk/why-talktalk/latest-job-at-talktalk
DONE - SQL - Vodafone - https://careers.vodafone.co.uk/jobs?q=&options=,701&page=1 / https://careers.vodafone.co.uk/jobs?q=&options=,701&page=2
DONE - SQL - Selenium - Claranet -https://www.claranet.co.uk/about-us/careers/jobs/all 
"""
statement = []
def get_url(url):
    # Attempt to download url content
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        # attempt to call url, if fails closes connection
        with closing(get(url, headers=headers, stream=True)) as resp:
            # runs function to check response
            if goodresp(resp):
                return resp.content
            else:
                return None

    # Raise exception if request failure
    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

def goodresp(resp):
    # Checks if HTML returns
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    # Prints error
    print(e)

def selenium(url):
        # Set chrome options
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')

        # load headless chrome session
        try:
            driver = webdriver.Chrome(options=options)
            # Get URL & scroll to bottom of page
            driver.get(url)
            driver.execute_script("window.scrollTo(0, 10000);")
            # Check page source length and download if greater than 0
            length = len(driver.page_source)
            if length > 0:
                time.sleep(3)
                response = driver.page_source
                return response
        # Throw exception if timeout
        except TimeoutError as e:
            log_error('Error during request to {0} : {1}'.format(url, str(e)))
            return None
        driver.close()

def db(statement):
    maria_connection = maria.connect(user='<db username>', password='<db password>', database='telcojobs')
    cursor = maria_connection.cursor()
    # Interate through statement list of prepared strings 
    date = dt.today().strftime('%y-%m-%d')
    for state in statement:
        # Split string and assign to 4 variables 
        company, role, location, salary = state.split(";")
        # Insert statement into database - Today's date / Company / Role / Location / Salary 
        cursor.execute("INSERT INTO telcojobs.jobs (date, company, role, location, salary) VALUES (%s, %s,%s,%s,%s)", (date, company, role, location, salary))
    print("Database updated")

    # Commit changes to database
    maria_connection.commit()
    print("Commited to database")

def elite():
    company = "Elite"
    url = "https://applythis.net/elitegroup/search/results/all/1"

    response = get_url(url)
    # Check if returned value isn't None and parse with BS
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        # Find tags on page for job listings
        jobs = html.findAll('tr', {'class': 'mpatsresultsrow'})
        # Iterate through listings - Identify tags for title (t) and salary (s)
        for job in jobs:
            t = job.find('h2', {'class':'rule'})
            s = job.find('p', {'class': 'mpatsoverviewsalary'})
            # Check if t and s are not none then print title/salary
            if t and s:
                t = t.text.strip()
                s = s.text.strip()
                s = s.split("Salary")
                # Extract salary (s)
                for s in s:
                    s = s.split(" per")
                    del s[-1]
                    s = [s.split(" £") for s in s]
                    for s in s:
                            # Extract salary from list
                            s = s[1]
                            # Split Role (t) & Location (l) into seperate variables
                            t, l = t.split("-")
                            # Prepare string statement to insert into SQL - Format: Company; role; location; salary
                            prepstring = "%s; %s; %s; %s" % (company, t, l, s)
                            # Append prepstring to statement list
                            statement.append(prepstring)
        print("Completed - %s jobs" % (company))

def gamma():
    company = "Gamma"
    url = "https://www.gamma.co.uk/about-us/careers/"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('div', {'class' : 'job-entry'})
        for job in jobs:
            for apply in job.findAll('div', {'class' : 'alt-info'}):
                # Ignore alt-info div sub-class
                apply.decompose()
            else:
                job = job.text.strip()
                prepstring = "%s; %s; null; null" % (company, job)
                statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def ukfast():
    company = "UkFast"
    url = "https://www.ukfast.co.uk/careers.html"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('td', {'class': 'title'})
        for job in jobs:
            prepstring = "%s; %s; null; null" % (company, job.text)
            statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def chess():
    company = "Chess"
    url = "https://chessict.co.uk/culture/careers/"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('li', {'class': 'filterValue'})
        for job in jobs:
            if job.text == "":
                break
            else:
                prepstring = "%s; %s; null; null" % (company, job.text)
                statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def daisy():
    company = "Daisy"
    url = "https://careers.smartrecruiters.com/DaisyGroup1"

    response = selenium(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        # Further work required to grab all sites
        loc = ["Manchester", "Nelson", "UK", "UK Wide"]
        for l in loc:
            for x in html.findAll('section', {'class': 'openings-section'}):
                if l in x.text:
                    job = x.findAll('h4', {'class': 'details-title job-title link--block-target'})
                    for job in job:
                        prepstring = "%s; %s; %s; null" % (company, job.text, l)
                        statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def talktalk():
    company = "TalkTalk"
    #print("-------------------------- %s Jobs --------------------------" % (company))
    url = "https://careers.talktalk.co.uk/why-talktalk/latest-job-at-talktalk"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('h4', {'class': 'job-feed__title'})
        for job in jobs:
            # Strip whitespace from text output
            output = job.text.strip("\n")
            prepstring = "%s; %s; null; null" % (company, output)
            statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def vodafone():
    company = "Vodafone"
    url = ["https://careers.vodafone.co.uk/jobs?q=&options=,701&page=1", "https://careers.vodafone.co.uk/jobs?q=&options=,701&page=2", "https://careers.vodafone.co.uk/jobs?q=&options=,701&page=3"]

    for url in url:
        response = get_url(url)
        if response is not None:
            html = BeautifulSoup(response, 'html.parser')
            jobs = html.findAll('span', {'class': 'inner-title'})
            for job in jobs:
                prepstring = "%s; %s; null; null" % (company, job.text)
                statement.append(prepstring)
    print("Completed - %s jobs" % (company))

def claranet():
    company = "Claranet"
    url = "https://www.claranet.co.uk/about-us/careers/jobs/all"

    # Call selenium session to extract html
    response = selenium(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('div', {'class': 'job_title'})
        for job in jobs:
                prepstring = "%s; %s; null; null" % (company, job.text)
                statement.append(prepstring)
    print("Completed - %s jobs" % (company))

if __name__ == "__main__":
    companies = [elite, gamma, ukfast, chess, daisy, talktalk, vodafone, claranet]
    for c in companies:
        c()
    db(statement);
