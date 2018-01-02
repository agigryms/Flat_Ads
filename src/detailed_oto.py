import utils as Utils
import re, datetime
from bs4 import BeautifulSoup


def oto_detailed(url):
    soup = Utils.request(url)
    params = soup.find("ul", "params-list")

    details = {}
    
    today = datetime.datetime.now().strftime("%d.%m.%Y")
    
    div = soup.find("div", "text-details")
    dates = div.find("div", "right").find_all("p")
    added = dates[0].text
    updated = dates[1].text
    details['DATES_UPDATED_ON'] = Utils.rex(":[ 0-9.]+", updated)[2:]
    details['DATES_PUBLISHED_ON'] = ("{}. Today is {}").format(Utils.rex(":[ a-z0-9.]+", added)[2:], today)


    left = div.find("div", "left")
    # details['ID'] is filled in by main script
    # id = left.find("p").text.strip()
    # details['ID'] = Utils.rex("Otodom:[ 0-9]+", id).split(': ')[1]
    seen = left.find_all("p")
    
    for p in seen:
        if Utils.rex("Liczba wy.wietle. strony", p.text.strip()):
            details['TIMES_SEEN'] = Utils.rex("[0-9]+", p.text.strip())


    if params.find("li", "param_m"):     
        details['POWIERZCHNIA'] = params.find("li", "param_m").find("span").text    
    else:
        details['POWIERZCHNIA'] = None
    
    if params.find("li", "param_m").find_next_sibling("li"):    
    	details['LICZBA_POKOI'] = params.find("li", "param_m").find_next_sibling("li").find("strong").text
    else:
        details['LICZBA_POKOI'] = None

    if params.find("li", "param_floor_no"):
        details['POZIOM'] = params.find("li", "param_floor_no").find("span").text
    else:
        details['POZIOM'] = None


    # properties below may or may not exist    
    details['CZYNSZ_DODATKOWO'] = None
    details['RODZAJ_ZABUDOWY'] = None
    details['UMEBLOWANE'] = None
    details['DATES_AVAILABLE_FROM'] = None
    details['OFERTA_OD'] = None

    if params.find("ul", "sub-list"):
        sub = params.find("ul", "sub-list")
        lis = sub.find_all("li")
        for li in lis: 

            if li.find("strong").text == "Czynsz - dodatkowo:":
                details['CZYNSZ_DODATKOWO'] = Utils.rex(":[0-9 ]+ z.", li.text.strip())[2:]

            if li.find("strong").text == "Rodzaj zabudowy:":
                details['RODZAJ_ZABUDOWY'] = Utils.rex(":[a-z ]+", li.text)[2:]

            if re.search("Stan wyko.czenia:", li.find("strong").text):
                details['UMEBLOWANE'] = Utils.rex(":[a-z ]+", li.text)[2:]

            if re.search("Dost.pne od:", li.find("strong").text):
                details['DATES_AVAILABLE_FROM'] = Utils.rex("[0-9]+[ a-zA-Z0-9]+", li.text)


    contact = soup.find("div", "box-contact-info")
    if contact.find("h6"):
        details['OFERTA_OD'] = contact.find("h6").text

    details['CONTACT'] = soup.find("span", "phone-number").text.strip()

    #details['DESCRIPTION'] = soup.find("div", "text-contents").find("div", {"itemprop":"description"}).text.strip()
    details['META_DESCRIPTION'] = soup.find("meta", {"name":"description"})["content"]
    
    return details
