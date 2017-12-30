import sqlite3, math, time
import general_olx_oto as General
import constants as Constants
import utils as Utils


url_main = Constants.url_main 

t0 = time.time()
ads_script = General.olx_url_main(url_main)
t9 = time.time()
print('Started @ {}\nFinished @ {}\nTook {} sec'
      .format(Utils.from_epoch(t0), Utils.from_epoch(t9), math.ceil(t9 - t0)))

