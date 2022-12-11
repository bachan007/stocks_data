import pandas as pd
import numpy as np
from nsetools import Nse
import yfinance as yf
import datetime as dt
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

nse = Nse()

## Getting the list of stock tickers with their name
stock_codes = pd.Series(nse.get_stock_codes())
top_looser = nse.get_top_losers()[0]
company = nse.get_quote(top_looser['symbol'])['companyName']
print(f"NSE Top looser on last traded day : {company}, with decline in price by {top_looser['netPrice']}%")

end_date = dt.datetime.now()
start_date = (end_date-relativedelta(years=5)).strftime('%Y-%m-%d') # past five years performance
end_date = end_date.strftime('%Y-%m-%d')

# Daywise data of the company
df = yf.download(f"{top_looser['symbol']}.NS",start_date,end_date)

# 100 days Moving Average --> average of last 100 days adj close price
df['100dma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

# 221 days Moving Average --> average of last 100 days adj close price
df['221dma'] = df['Adj Close'].rolling(window=221, min_periods=0).mean()

plt.figure(figsize=(12,8))
ax1 = plt.subplot2grid((7,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((7,1),(5,0),rowspan=2,colspan=1, sharex=ax1)
ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100dma'])
ax1.plot(df.index,df['221dma'])
ax2.bar(df.index,df['Volume'])
plt.show()