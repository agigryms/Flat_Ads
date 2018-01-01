import detailed_olx as Olx
import detailed_oto as Oto
import utils as Utils
import constants as Constants
import sqlite3, re, time


def olx_url_main(url):

    # create cursor for sqlite
    conn = sqlite3.connect(Constants.db_ads)
    conn.row_factory = sqlite3.Row
    conn.isolation_level = None
    c = conn.cursor()

    c.execute(Constants.db_create_ads)

    insert_sql = Constants.db_insert_into_ads

    # get list of ad id's in db
    # ads that already exist in db will be skipped
    db_ids = c.execute(Constants.db_ids).fetchall()
    ids = []
    for id in db_ids:
        ids.append(id['ID'])

    # get keywords for filters
    patterns = Constants.patterns
    
    # start scraping
    soup = Utils.request(url)
    ads = soup.find("table", {'id':"offers_table"})

    singles = ads.find_all("tr",  "wrap")
    results = []

    # single is one ad from main url's list of ads 
    for single in singles:
        title = single.find('h3').text.strip()
        filtered_out = False

        # gen is information scraped for single from main url
        # details is information from single's detailed url
        gen = {}
        details = {}
        
        for pattern in patterns:
            if re.search(pattern, title.lower()):
                filtered_out = True
                break
                
        if not filtered_out:

            url_detailed = single.find('a')['href']
            soup_detailed = Utils.request(url_detailed)

            # extract detailed info for otodom.pl ad   
            match_oto = re.search(Constants.oto_url_pattern, url_detailed)
            if match_oto:
                div = soup_detailed.find("div", "text-details")
                left = div.find("div", "left")
                soup_id = left.find("p").text.strip()
                id = Utils.rex("Otodom:[ 0-9]+", soup_id).split(': ')[1]

                # check if ad's id is not in db
                if id not in ids:
                    div = soup_detailed.find("div", "text-details")
                    dates = div.find("div", "right").find_all("p")
                    added = dates[0].text
                    
                    # check if ad is not older than 14 days; if so, it will be skipped
                    if Utils.rex(":[ a-z0-9.]+", added)[2:] != "ponad 14 dni temu":
                        gen = Utils.general_ad_info(url_detailed, title, single)
                        details = Oto.oto_detailed(gen['URL'])
                        details['ID'] = id

                        
            # extract detailed info for olx.pl ad
            match_olx = re.search(Constants.olx_url_pattern, url_detailed)
            if match_olx:     
                em = soup_detailed.find("em")
                id = Utils.rex("[0-9]+", em.find("small").text)
                
                # check if ad's id is not in db
                if id not in ids:
                    gen = Utils.general_ad_info(url_detailed, title, single)
                    details = Olx.olx_detailed(gen['URL'])
                    details['ID'] = id
                    
            time.sleep(1)
            ad = {**gen, **details}
            if ad: 
                c.execute(Constants.db_insert_into_ads, (ad['TITLE'], \
                       ad['LOCATION'], \
                       ad['URL'], \
                       ad['PRICE'], \
                       ad['OFERTA_OD'], \
                       ad['CZYNSZ_DODATKOWO'], \
                       ad['POWIERZCHNIA'], \
                       ad['LICZBA_POKOI'], \
                       ad['TIMES_SEEN'], \
                       ad['DATES_PUBLISHED_ON'], \
                       ad['DATES_DB_SAVED_ON'], \
                       ad['RODZAJ_ZABUDOWY'], \
                       ad['DESCRIPTION'], \
                       ad['META_DESCRIPTION'], \
                       ad['DATES_AVAILABLE_FROM'], \
                       ad['DATES_UPDATED_ON'], \
                       ad['POZIOM'], \
                       ad['UMEBLOWANE'], \
                       ad['CONTACT'], \
                       ad['ID'], \
                      ))                
                results.append(ad)
        
        else:
            pass
    
    return results
                         
