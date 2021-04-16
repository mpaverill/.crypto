from cryptocmd import CmcScraper
import shutil
import csv

# generate list of top 200 crypto tickers by market cap
top_200_tickers = []
with open('top_200.csv', newline='') as csvfile:
     tickerreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     i = 0
     for tick in tickerreader:
         top_200_tickers.append(tick[0])
         i += 1
top_200_tickers[0] = 'BTC'

j = 0
for ticker in top_200_tickers:
    # initialise scraper without time interval
    scraper = CmcScraper(ticker)

    # get raw data as list of list
    headers, data = scraper.get_data()

    # get data in a json format
    stroj_json_data = scraper.get_data("json")

    # export the data as csv file, you can also pass optional `name` parameter
    scraper.export("csv", name=ticker)
    path_partial1 = 'C:/Users/Matthew/Documents/.crypto/'
    path_partial2 = 'C:/Users/Matthew/Documents/.crypto/DATA/'
    ext = '.csv'
    path_full1 = path_partial1 + ticker + ext
    path_full2 = path_partial2 + ticker + ext
    shutil.move(path_full1, path_full2)

    # Pandas dataFrame for the same data
    df = scraper.get_dataframe()

    # display progress
    phrase = '/200 Datasets Complete'
    num_complete = str(j + 1)
    print(num_complete + phrase)
    j += 1