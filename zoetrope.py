import time
import giphy_client
import random
import numpy as np
import sys
import math
from urllib import request
from giphy_client.rest import ApiException
from pprint import pprint
from subprocess import call, run 

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'xbG4NZKIK3I35KErPcQ3UAyAtXg4q7Xi' # str | Giphy API Key.
q = '' # str | Search query term or prhase.
limit = 25 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
screenWidthX = 128
screenWidthY = 64

try:
    if len(sys.argv) < 2:
        print("No search term provided! :(")
        exit(1)
    else:
        q = sys.argv[1]
        print("Searching for gifs...")
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        #pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

# Retrieve the gif
data_len = len(api_response.data)
if data_len is 0:
    print ("No results for " + sys.argv[1] + "!")
    exit(1)
else:
    print ("Resizing gif...")

# pull a uniformly generated random number
idx = int(np.random.uniform(0, data_len))
request.urlretrieve(api_response.data[idx].images.fixed_height.url, "./status.gif")

result = run(['gifsicle', '--sinfo', 'status.gif', '#0'], capture_output=True)
result = result.stdout.decode()

dims = ''

for line in result.split("\n"):
    if "logical screen" in line:
        lineSplit = line.strip().split(' ')
        dims = lineSplit[2].split('x')

xDim = int(dims[0])
yDim = int(dims[1])
divider = 1
if dims is not '':
    # is the width greater than the length?
    if xDim > yDim:
        divider = xDim/screenWidthX
    else:
        # this catch-all else case is desired since the Y is the limiting factor of the screen
        divider = yDim/screenWidthY
xDimResize = math.floor(xDim/divider)
yDimResize = math.floor(yDim/divider)
call(['gifsicle', 'status.gif', '--colors=256', '--resize', str(xDimResize)+'x'+str(yDimResize), '-o', 'status.gif'])

call(['animate', './status.gif'])

