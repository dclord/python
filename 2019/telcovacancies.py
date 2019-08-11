from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver

"""
Sites: 
DONE - Elite Telecom - https://elitegroup.com/careers/current-opportunities/ 
DONE - Gamma Telecom -  https://gamma.co.uk/about-us/careers/
DONE - UKFast - https://ukfast.co.uk/careers.html
DONE - Chess - https://chessict.co.uk/culture/join-us/
Daisy - https://careers.smartrecruiters.com/DaisyGroup1
DONE - TalkTalk - https://careers.talktalk.co.uk/why-talktalk/latest-job-at-talktalk
DONE - Vodafone - https://careers.vodafone.co.uk/jobs?q=&options=,701&page=1 / https://careers.vodafone.co.uk/jobs?q=&options=,701&page=2
DONE - Claranet -https://www.claranet.co.uk/about-us/careers/jobs/all 
"""

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
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')

        try:
            driver = webdriver.Chrome(options=options)
            driver.get(url)
            length = len(driver.page_source)
            if length > 0:
                response = driver.page_source
                return response
        except TimeoutError as e:
            log_error('Error during request to {0} : {1}'.format(url, str(e)))
            return None

def elite():
    print("-------------------------- Elite Jobs --------------------------")

    urls = ["https://applythis.net/elitegroup/search/results/all/1"]
    # Iterate url list and call above function to download HTML
    for url in urls:
        response = get_url(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('tr', {'class': 'mpatsresultsrow'})

        for job in jobs:
            t = job.find('h2', {'class':'rule'})
            s = job.find('p', {'class': 'mpatsoverviewsalary'})

            if t and s:
                t = t.text.strip()
                s = s.text.strip()
                s = s.split("Salary")

                for s in s:
                    s = s.split(" per")
                    del s[-1]
                    s = [s.split(" £") for s in s]
                    for s in s:
                            print(t + " - " + str(s[1]))

def gamma():
    print("-------------------------- Gamma Jobs --------------------------")

    url = "https://www.gamma.co.uk/about-us/careers/"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('div', {'class' : 'job-entry'})

        for job in jobs:
            for apply in job.findAll('div', {'class' : 'alt-info'}):
                apply.decompose()
            else:
                job = job.text.strip()
                print(job)
                
def ukfast():
    print("-------------------------- UkFast Jobs --------------------------")

    url = "https://www.ukfast.co.uk/careers.html"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('td', {'class': 'title'})

        for job in jobs:
            print(job.text)

def chess():
    print("-------------------------- Chess Jobs --------------------------")

    url = "https://chessict.co.uk/culture/careers/"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('li', {'class': 'filterValue'})

        for job in jobs:
            if job.text == "":
                break
            else:
                print(job.text)

def daisy():
    print("-------------------------- Daisy Jobs --------------------------")

    url = "https://careers.smartrecruiters.com/DaisyGroup1"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        print(html.prettify())

        for x in html.findAll('section', {'class': 'openings-section'}):
            # print(x)
            if "Manchester" in x:
                print(x)
                job = x.find('li', {'class': 'opening-job job column wide-7of16 medium-1of2'})
                for job in job:
                    print(job.text)

def talktalk():
    print("-------------------------- TalkTalk Jobs --------------------------")

    url = "https://careers.talktalk.co.uk/why-talktalk/latest-job-at-talktalk"

    response = get_url(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = html.findAll('h4', {'class': 'job-feed__title'})

        # for job in jobs:
        # loc = html.findAll('span', {'class': 'job-feed__location'})
        # if loc:
        #     for loc in loc:
        #         loc = loc.text.split("\t")
        #         for loc in loc:
        #             loc = loc.rstrip(" \n")
        #         # job = job.text.strip()
        for job in jobs:
            print(str(job.text.strip()))

def vodafone():
    print("-------------------------- Vodafone Jobs --------------------------")

    url = ["https://careers.vodafone.co.uk/jobs?q=&options=,701&page=1", "https://careers.vodafone.co.uk/jobs?q=&options=,701&page=2", "https://careers.vodafone.co.uk/jobs?q=&options=,701&page=3"]

    for url in url:
        response = get_url(url)
        if response is not None:
            html = BeautifulSoup(response, 'html.parser')
            jobs = html.findAll('span', {'class': 'inner-title'})

            for job in jobs:
                print(job.text)

def claranet():
    print("-------------------------- Claranet Jobs --------------------------")
    url = "https://www.claranet.co.uk/about-us/careers/jobs/all"
    response = selenium(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        jobs = html.findAll('div', {'class': 'job_title'})

        for job in jobs:
            print(job.text)

if __name__ == "__main__":
    companies = [elite, gamma, ukfast, chess, talktalk, vodafone, claranet]

    for c in companies:
        c()
        print("\n")
