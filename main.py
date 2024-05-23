from util.config import baseURL, directoryRelUrl, saveAs, saveName
from util.links import extractLinks, extractStoreLinks, extractStoreInfo
import pandas as pd
from tqdm import tqdm

cityLinks = []
storeLinks = []
pandasList = [['Store Name', 'Store Number', 'Phone Number', 'Address', 'Url', 'Longitude', 'Latitude', 'City', 'State']]

print('Extracting State Links...')
stateLinks = extractLinks(baseURL + directoryRelUrl)

print('Extracting City Links...')
for i in tqdm(range(len(stateLinks))):
    link = stateLinks[i]
    cityLinks += extractLinks(link)

print('Extracting Store Links...')
for j in tqdm(range(len(cityLinks))):
    link = cityLinks[j]
    storeLinks += extractStoreLinks(link)

print('Extracting Store Information...')
for k in tqdm(range(len(storeLinks))):
    link = storeLinks[k]
    pandasList.append(extractStoreInfo(link))

print('Saving...')
df = pd.DataFrame(pandasList[1:],columns=pandasList[0])

if('csv' in saveAs):
    df.to_csv('{data}.csv'.format(data = saveName), index=False)
if('excel' in saveAs):
    df.to_excel("{data}.xlsx".format(data = saveName), index=False)