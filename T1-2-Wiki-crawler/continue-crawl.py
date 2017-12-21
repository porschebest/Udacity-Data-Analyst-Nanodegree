import time
import requests
from bs4 import BeautifulSoup

def check_duplicate(search_list):
    check_list = []
    count = 0
    for item in search_list:
        if item in check_list:
            count += 1
        else:
            check_list.append(item)
    return count

def continue_crawl(search_history,target_url, max_steps=25):
    while len(search_history) < max_steps :
        #   most recent article in the search_history is the target article -> False
        if(target_url in search_history):
            print('reach Philosophy')
            return False
        #   list is more than 25 urls -> False
        elif len(search_history) > max_steps:
            print('long route error')
            return False
        #   has a cycle in it -> False
        elif check_duplicate(search_history) != 0:
            print('loop detected')
            return False
        #   Else -> Continue
        else:
            print('continue')
            return True

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)

def first_link(url):
    # return the first link as string or return None if there's no link
    #  get the HTML from the url
    response = requests.get(url)
    #  feed the HTML into BeautifulSoup
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    #  get the first link from the html
    first_link = soup.div['mw-content-text']
    print(first_link)
    #  return the first link
    if first_link != None:
        return first_link
    else:
        return None
first_link('https://en.wikipedia.org/wiki/Helsinki')
