from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

finviz_url = 'https://finviz.com/quote.ashx?t='
tickers = ['AMZN', 'GOOG', 'FB']

news_tables =  {}
for ticker in tickers:
    url = finviz_url + ticker

    req = Request(url=url, headers={'user-agent': 'my-app'})
    response = urlopen(req)
    
    html = BeautifulSoup(response, 'html')
    news_table = html.find(id='news-table')
    news_tables[ticker] = news_table

    break

amzn_data = news_tables['AMZN']
amzn_rows = amzn_data.findAll('tr')

for index, row in enumerate(amzn_rows):
    title = row.a.text
    timestamp = row.td.text
    print(timestamp + " " + title)