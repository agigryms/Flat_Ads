import time, requests, re
from bs4 import BeautifulSoup


def from_epoch(t0):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t0))


def request(url): 
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup


def rex(pattern, base):
    if re.search(pattern, base):
        return re.search(pattern, base).group()
    else:
        return None

    
def if_equals_else_none(condition_left, condition_right, if_successful):
    if condition_left == condition_right:
        return if_successful
    else:
        return None

    
def if_exists_else_none(condition, if_successful):
    if condition:
        return if_successful
    else:
        return None


def general_ad_info(url_detailed, ad_title, single_soup):
    gen = {}
    
    gen['URL'] = url_detailed
    gen['TITLE'] = ad_title
    p = single_soup.find_all('p')
    gen['PRICE'] = p[1].text.strip()
    gen['LOCATION'] = p[2].text.strip()
    gen['DATES_DB_SAVED_ON'] = from_epoch(time.time())
    
    return gen	
