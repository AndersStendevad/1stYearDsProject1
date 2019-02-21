from InstagramAPI import InstagramAPI
import time
from extensions import logger

logger = logger.get_logger()

def locationSearch(location, hits):
    maxid = ''
    for i in range(hits):
        API.getHashtagFeed(location, maxid)
        data = API.LastJson
        try:
            for pic in data.get('items'):
                if pic.get('caption'):
                    log.write(pic.get('caption').get('text'))
            #log.write(data.get('items')[0].get('caption').get('text'))
            log.write('\n \n')
            maxid = data.get('next_max_id')
        except Exception:
            logger.info(f'error on fetch')
            logger.info(data)
            break
            pass
        time.sleep(1)

API = InstagramAPI("neil_ds_guy", "mKh80994QCuY")
API.login()

size = 100

with open('instagram_locations.txt', 'r') as loc:
    for line in loc:
        location = line.strip()
        logger.info(f'writing data to {location}')
        log = open(location+".txt", "w")
        locationSearch(location, size)
        log.close()
