#url_main = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_float_m%3Afrom%5D=50"
url_main = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/warszawa/?search%5Bfilter_float_price%3Ato%5D=2000&search%5Bfilter_float_m%3Afrom%5D=50&search%5Bfilter_enum_rooms%5D%5B0%5D=three"


oto_url_pattern = "^https?:\/\/www.otodom.pl\/" 


olx_url_pattern = "^https?:\/\/www.olx.pl\/"


#patterns_title = [".*dla rodziny.*", ".*bez po.srednik.*", ".*||.*", ".*tel ||.*", ".*na biuro.*", ".*bezpo.*", ".*bez prowizji.*", ".*wilan.w.*", ".*lux.*", ".*ekskluzywn.*", ".*luksus.*", ".*tarchomin.*", ".*bia.o.*", ".*weso.*", ".*rembert.*", ".*prag.*", ".*pradz.*", ".*targ.w.*", ".*kochanowski.*", ".*sask.*", ".*kabat.*"]
patterns_title = [".*dla rodziny.*", ".*bez po.srednik.*", ".*||.*", ".*tel ||.*", ".*na biuro.*", ".*bezpo.*", ".*bez prowizji.*"]


patterns_desc = [".*bezpo.redni.*", ".*bez prowizji.*", ".*luksusow.*", ".*bez agencji.*", ".*niniejsze og.oszenie jest wy..cznie informacj. handlow.*", ".*po.rednikom dzi.kuj.*", ".*agencjom dzi.kuj.*", ".*nie wsp..pracuj. z agencj.*", ".*nie wsp..pracuj. z po.rednik.*"]


db_ads = "/home/agigryms/Notebooks/Flat_Ads/Flat_Ads/ads.db"


db_create_ads = """
    CREATE TABLE IF NOT EXISTS ads (
    TITLE text, 
    LOCATION text, 
    URL text,
    PRICE text,
    OFERTA_OD text,
    CZYNSZ_DODATKOWO text,
    POWIERZCHNIA text,
    LICZBA_POKOI text,
    TIMES_SEEN text,
    DATES_PUBLISHED_ON text,
    DATES_DB_SAVED_ON text,
    RODZAJ_ZABUDOWY text,
    DESCRIPTION text,
    META_DESCRIPTION text,
    DATES_AVAILABLE_FROM text,
    DATES_UPDATED_ON text,
    POZIOM text,
    UMEBLOWANE text,
    CONTACT text,
    ID text)
    """


db_insert_into_ads = """INSERT INTO ads (
    TITLE, 
    LOCATION, 
    URL,
    PRICE,
    OFERTA_OD,
    CZYNSZ_DODATKOWO,
    POWIERZCHNIA,
    LICZBA_POKOI,
    TIMES_SEEN,
    DATES_PUBLISHED_ON,
    DATES_DB_SAVED_ON,
    RODZAJ_ZABUDOWY,
    DESCRIPTION,
    META_DESCRIPTION,
    DATES_AVAILABLE_FROM,
    DATES_UPDATED_ON,
    POZIOM,
    UMEBLOWANE,
    CONTACT,
    ID) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

db_ids = "SELECT ID FROM ads"
