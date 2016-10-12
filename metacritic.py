#!/usr/bin/env python3
#
# Code Assessment for Gaikai
#
# Chris Moser May 9 2016

import os
from lxml import html
import json
import pprint
import unittest

MC_URL = "http://metacritic.com/game/playstation-3"

def topps3games():
    #requests.get or urllib.open would be the preferred methods but return "forbidden 403"
    #This may vioate the TOS: "Engage in unauthorized spidering, "scraping," ...
    
    #I used wget to grab the page and them work from the local file instead
    #Only need to download the first run
    if not os.path.isfile('page.html'):
        os.system('wget ' + MC_URL + ' -O page.html')

    tree = html.parse('page.html')	

    title = tree.xpath('//div[@class="basic_stat product_title"]/h3/a/text()')
    score = tree.xpath('//a[@class="basic_stat product_score"]/span/text()')
    
    gamesarray = []

    for i in range(len(title)):
        gamesarray.append(json.dumps({'title' : title[i], 'score' : score[i]}))

    return(gamesarray)

def printgames():
    pprint.pprint(topps3games(), indent=4)

printgames()
