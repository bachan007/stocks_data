# This  is a test regarding yahoo finance data reader
import yfinance as yf
from datetime import datetime as dt
from dateutil import parser
import datetime

def date_format(date_val):
    date_val = parser.parse(date_val,dayfirst=True)
    formatted_date = date_val.strftime("%Y-%m-%d")
    if formatted_date:
        return formatted_date
    else:
        print("Enter a valid Date")

start_date = date_format(input('Enter the Start date : \n'))
end_date = input('Enter the End date : \n')

if not end_date:
    end_date = dt.now().strftime('%Y-%m-%d')
    print(end_date)
else:
    end_date = date_format(end_date)

ticker = input("Enter the Stock Symbol : \n")

data = yf.download(ticker,start_date,end_date)
data.sort_index(ascending=False, inplace=True)
print(f"Here are the latest 5 records : \n {data.head()}")