import requests
import logging
import logging.handlers
import os

page = requests.get('https://www.screener.in/company/WIPRO/consolidated/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content,'html.parser')
def dummy(page):
  soup = BeautifulSoup(page.content,'html.parser')
  c = soup.find('h1',{'class':'margin-0'})
  name = c.string
  d = soup.find('div',{'class':'company-ratios'})
  e = d.findAll('span')
  price = e[5].string
  mcap = e[2].string
  hprice_52week = e[8].string
  lprice_52week = e[9].string
  pe = e[12].string
  bookvalue =e[15].string
  div_yield =e[18].string
  ROCE =e[21].string
  ROE = e[24].string
  facevalue = e[27].string
  return (name,price,mcap,hprice_52week,lprice_52week,pe,bookvalue,div_yield,ROCE,ROE,facevalue)

#print(dummy(page))

import pandas as pd

df = pd.read_csv("https://www1.nseindia.com/content/indices/ind_nifty50list.csv")
df.head()

top50 = []
for i in df.loc[:,'Symbol']:
    url = f"https://www.screener.in/company/{i}/consolidated/"
    top50.append(url)

top_stocks = []
for i in top50:
  top_stocks.append(requests.get(i))

nifty_50 = []
for i in top_stocks:
  try:
    nifty_50.append(dummy(i))
  except:
    pass

label = ['Name','Price','MCap','High_52week','Low_52week','PE','Bookvalue','Div_yield%','ROCE%','ROE%','Facevalue']
#print(pd.DataFrame(nifty_50, columns = label))


#try:
#    SOME_SECRET = os.environ["SOME_SECRET"]
#except KeyError:
#    SOME_SECRET = "Token not available!"
#    #logger.info("Token not available!")
#    #raise


if __name__ == "__main__":
   print(pd.DataFrame(nifty_50, columns = label))
    #logger.info(f"Token value: {SOME_SECRET}")

