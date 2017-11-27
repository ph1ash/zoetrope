import time
import giphy_client
import random
import numpy as np
from urllib import request
from giphy_client.rest import ApiException
from pprint import pprint
from subprocess import call

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'xbG4NZKIK3I35KErPcQ3UAyAtXg4q7Xi' # str | Giphy API Key.
q = 'cats' # str | Search query term or prhase.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Search Endpoint
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    #pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

# Retrieve the gif
idx = int(np.random.uniform(0,24))
pprint(idx)
request.urlretrieve(api_response.data[idx].images.fixed_height.url, "./status.gif")

call(['animate', './status.gif'])
