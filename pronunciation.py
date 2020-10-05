#!/usr/bin/env python3

import sys
import  requests
import json
import wget

app_id = 'put your own app_id here'
app_key = 'put your own app_key here'
language = 'en-us'
word_id = str(sys.argv[1])
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.strip().lower()

print(url)
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})

result = r.json()

try:
  word_url = result['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][1]['audioFile']
except:
  print('{} does not have a pronounciation file.'.format(word_id))
else:
    print(word_url)
    filename = wget.download(word_url, '/home/bahman/Desktop/Miscellaneous University words/' + word_url.split('/')[-1])
    print("\nThe name of downloaded file is ",filename, '\n', )
