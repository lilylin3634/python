#import pandas as pd
#df = pd.read_csv("./stocks/2330.csv")
#df = df['Close']
# df = df['Date']
# print(df.tail(5))
# #
import pandas as pd
import yfinance as yf
from tqdm import tqdm
import web_crawler as wc

# date = '2013-01-01'
# stock_no = wc.get_stocks_0050()
# print(stock_no)
#
# all_dataframe = pd.DataFrame()
# for stock_id in tqdm(stock_no):
#     stock = yf.Ticker(str(stock_id) + ".TW")
#     #轉成string才能加上TW
#     stock_data = stock.history(start=date)
#     stock_data = stock_data.rename(columns={'Close': str(stock_id)})
#     stock_data = stock_data[str(stock_id)]#取出收盤價，因改名要用改名後的取!
#
#
#     all_dataframe = pd.concat([all_dataframe, stock_data], axis=1)
#     all_dataframe.to_csv(f'./0050.csv')

#print(all_dataframe)
