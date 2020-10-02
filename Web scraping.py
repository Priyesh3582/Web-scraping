# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 04:25:58 2020

@author: PRIYESH
"""

#WEB SCRAPPING
import requests
r = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')
print(r.text[0:500])

from bs4 import BeautifulSoup
#making it usable
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('span', attrs={'class':'short-desc'})
len(results)

results[0:3]
results[-1]
first_result = results[0]
#date
first_result
first_result.find('strong')
first_result.find('strong').text
first_result.find('strong').text[0:-1]
first_result.find('strong').text[0:-1] + ', 2017'
#lie
first_result
first_result.contents
first_result.contents[1]
first_result.contents[1][1:-2]
#explanation
first_result
first_result.contents  #converts in list
first_result.contents[2]
first_result.find('a').text[1:-1]

#url
first_result.find('a').text[0:1]

first_result.find('a')['href']
records=[]
for result in results:
    date=result.find('strong').text[0:-1] + ', 2017'
    lie=result.contents[1][1:-2]
    explanation=result.find('a').text[1:-1]
    url=result.find('a')['href']
    records.append((date,lie,explanation,url))

records[0:3]
import pandas as pd
a=pd.DataFrame(records, columns=['date','lie','explanation','url'])








