import utils as Utils
import re
from bs4 import BeautifulSoup


def olx_detailed(url):
    soup = Utils.request(url)
    
    details = {}
    
    # 2 DATES properties don't exist for olx.pl ads
    details['DATES_UPDATED_ON'] = None
    details['DATES_AVAILABLE_FROM'] = None
    
    # properties below may or may not exist
    details['OFERTA_OD'] = None
    details['RODZAJ_ZABUDOWY'] = None
    details['LICZBA_POKOI'] = None
    details['UMEBLOWANE'] = None
    details['POWIERZCHNIA'] = None
    details['CZYNSZ_DODATKOWO'] = None
    details['POZIOM'] = None
    details['CONTACT'] = None

    em = soup.find("em")
    # details['ID'] is filled in by main script
    # details['ID'] = Utils.rex("[0-9]+", em.find("small").text)
    details['DATES_PUBLISHED_ON'] = Utils.rex("o .*20[0-9]+", em.text)[2:]

    seen = soup.find("div", {"id":"offerbottombar"}).find_all("div")
    details['TIMES_SEEN'] = seen[len(seen) - 1].text.strip().split(':')[1]
   
 
    detailed_table = soup.find("table", "details").find_all("th")
    for th in detailed_table:
        td = th.find_next_sibling("td")
	# replace spaces with _ in property names, capitalize letters and remove ()
        details['_'.join(th.text.strip().upper()\
                         .replace('(', '').replace(')', '')\
			 .split(' '))] \
	= td.text.strip()


    content = soup.find("div", {"id":"textContent"})
    details['META_DESCRIPTION'] = soup\
			 .find("meta", {"name":"description"})["content"]
 
        
    return details
