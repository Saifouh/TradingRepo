



####### NO LONGER NEED THE CODE BELOW InSTRUCTIONS ABOVE ########

# import pandas as pd 
# import requests 
# import json

# #########

# symbol = 'ETH-USD' # change this symbol to the data you'd like
# timeframe = '15m' # select a time frame - 1m, 5m, 15m, 30m, 1h, 6h, 1d
# start_time = '2018-1-02T00:00' #format is {year(4 digit)}-{month}-{day}T{hour}:{minute}

# ########


# # below is the api endpoint and doesnt really need to be changed unless you want to customize things



# ######

# candles_data = {
#     'symbol': symbol, 
#     'timeframe': timeframe, 
#     'start_date': start_time
# }

# r = requests.post('https://cryptofacts.dev/api/get_candle_data',data=candles_data).text #returns a string of a dict containing the pandas data for candles
# candles_df = pd.DataFrame.from_dict(json.loads(r)).set_index('datetime') #converts the string dict back to a pandas dataframe
# print(candles_df)

# #output data to a csv 
# # candles_df.to_csv(f'sample-data.csv')
# candles_df.to_csv(f'{symbol}-{timeframe}-{start_time}.csv')
