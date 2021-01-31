import requests
from bs4 import BeautifulSoup
import re


#sua url goc
def fix_url(url):
    if url[-1] == '/':
        url = url[0: -1]
        return url
    else:
        return url

#tim cac url lien quan
def search_url(url, url_main):
    url_results = set() #url tìm được
    link = requests.get(url)
    link_soup = BeautifulSoup(link.text, 'html.parser')
    results = link_soup('a', attrs={'href': True})
    #tach link ra khoi the
    for i in results:
        a = i['href']
        title_main = f'^{url_main}[^?#]*$'
        title_sub = '^/[^?#]*$'
        if re.match(title_main, a):
            url_results.add(a)
        else:
            if re.match(title_sub, a):
                url_new = f'{url_main}{a}' #url sau khi them phan mo dau
                url_results.add(url_new)
    return url_results

#them va duyet hang cho
def add_link(queue, url_main, page_max):
    history = queue
    while (len(queue) > 0) and (len(history) < page_max):
        url_results = search_url(queue.pop(), url_main)
        queue = queue | (url_results - history)
        history = history | url_results
    return history