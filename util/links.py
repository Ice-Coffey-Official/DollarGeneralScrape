import requests
from bs4 import BeautifulSoup
from util.config import retryBackoff, reqSleep
import time

def extractLinks(url):
    time.sleep(reqSleep)
    newLinks = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        page = requests.get(url, headers=headers)
    except:
        try:
            time.sleep(retryBackoff)
            page = requests.get(url, headers=headers)
        except:
            return []

    soup = BeautifulSoup(page.text, 'lxml')
    mylinks = soup.findAll("p", { "class" : "location-list-item" })
    for i in range(len(mylinks)):
        link = mylinks[i]
        newLink = link.find('a')['href']
        ending = newLink.split('/')[-1].split('.')[0]
        newLinks.append(url + '/' + ending)
    
    return newLinks

def extractStoreLinks(url):
    time.sleep(reqSleep)
    newLinks = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        page = requests.get(url, headers=headers)
    except:
        try:
            time.sleep(retryBackoff)
            page = requests.get(url, headers=headers)
        except:
            return []
    soup = BeautifulSoup(page.text, 'lxml')
    mylinks = soup.findAll("a", { "class" : "view-details" })
    for i in range(len(mylinks)):
        link = mylinks[i]
        newLink = link['href']
        ending = newLink.split('/')[-1].split('.')[0]
        newLinks.append(url + '/' + ending)
    
    return newLinks

def extractStoreInfo(url):
    time.sleep(reqSleep)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try:
        page = requests.get(url, headers=headers)
    except:
        try:
            time.sleep(retryBackoff)
            page = requests.get(url, headers=headers)
        except:
            return []
    soup = BeautifulSoup(page.text, 'lxml')
    storeNum = url.split('/')[-1]
    city = url.split('/')[-2]
    state = url.split('/')[-3]
    try:
        name = soup.find("title").text.strip()
    except:
        name = ''

    try:
        phoneNumber = soup.findAll("div", { "class" : "store-details__main-phone" })[-1]['data-phone'].strip('\\')
    except:
        phoneNumber = ''

    try:
        address = soup.find("meta", { "name" : "description" })['content'].split('| ')[-1]
    except:
        address = ''

    try:
        latitude = soup.findAll("div", { "class" : "store-details__main-travel" })[-1]['data-latitude']
    except:
        latitude = ''

    try:
        longitude = soup.findAll("div", { "class" : "store-details__main-travel" })[-1]['data-longitude']
    except:
        longitude = ''

    return [name, storeNum, phoneNumber, address, url, longitude, latitude, city, state]