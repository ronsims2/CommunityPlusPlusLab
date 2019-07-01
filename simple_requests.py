import requests

url = 'https://gist.githubusercontent.com/ronsims2/6097f7b1b5a4d82187c4171e1201ff01/raw/e3089c1202ca473270e390937321715824f0c523/sample-data.csv'
resp = requests.get(url)

print(resp.text)

#show common auth methods ie basic auth and api key, use census api...
