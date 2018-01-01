import sqlite3, time
import general_olx_oto as General
import constants as Constants
import utils as Utils
import set_env_vars as MailgunCredentials
import os


# set 3 Mailgun env variables (they are only valid for duration of this instance)
MailgunCredentials.set_mailgun_credentials()


url_main = Constants.url_main 

t0 = time.time()
ads_list = General.olx_url_main(url_main)
t9 = time.time()

if ads_list:
    all_ads = Utils.list_dicts_to_string(ads_list)    
    Utils.send_email(all_adds)
    print('Email sent with {} new ads.'.format(len(ads_list)))
else:
    print('No new updates and no new email.')


print('Started @ {}\nFinished @ {}\nTook {} sec'
      .format(Utils.from_epoch(t0), Utils.from_epoch(t9), int(t9 - t0)))


print(os.environ['MAILGUN_API_BASE_URL'])
print(os.environ['MAILGUN_API_KEY'])
print(os.environ['MAILGUN_FROM'])
print(os.environ['ALERT_RECIPIENT'])
