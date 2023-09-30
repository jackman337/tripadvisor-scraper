#%pip install selenium==3.14.1

def get_driver():

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.page_load_strategy = 'normal'

    driver = webdriver.Remote('http://192.168.86.35:4444/wd/hub', options=options)

    return driver

schema = {'reviews': ('div', 'eSDnY'),
          'review': ('div', '_c'),
          'text': ('span', 'JguWG')}

def list_reviews(html):

    from bs4 import BeautifulSoup

    reviews_list = []

    soup = BeautifulSoup(html, 'html.parser')
    reviews_container = soup.find(schema['reviews'][0], {'class': schema['reviews'][1]})

    if reviews_container:

        reviews = reviews_container.find_all(schema['review'][0], {'class': schema['review'][1]})
        
        for review in reviews:
            review_text = review.find(schema['text'][0], {'class': schema['text'][1]}).text
            reviews_list.append(review_text)

    return reviews_list

from datetime import datetime
import time

t0 = datetime.now()

page = 0
reviews = []

while True:

    driver = get_driver()
    #url = f'https://www.tripadvisor.com/Attraction_Review-g34678-d108453-Reviews-or{page*10}-The_Florida_Aquarium-Tampa_Florida.html'
    url = f'https://www.tripadvisor.com/Attraction_Review-g60878-d123109-Reviews-or{page*10}-Space_Needle-Seattle_Washington.html'
    driver.get(url)

    html = driver.page_source
    reviews_list = list_reviews(html)

    driver.quit()

    if reviews_list:
        reviews += reviews_list
    else:
        break

    page += 1
    print (f'Page: {page:,}')

    time.sleep(2)

t1 = datetime.now()
t2 = (t1-t0).seconds

print (f'Processed {page:,} pages in {t2//60}:{t2%60}')
