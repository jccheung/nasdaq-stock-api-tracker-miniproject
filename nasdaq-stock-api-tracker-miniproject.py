import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
#Call the Nasdaq API and pull out a small sample of the data (only one day) to get a glimpse into the JSON structure that will be returned

API_KEY = os.getenv('NASDAQ_API_KEY')
# NASDAQ data set will focus on the Frankfurt Stock Exchange (FES) and analyze the stock prices of a company named Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

#You can find the detailed Nasdaq Data API instructions here: https://docs.data.nasdaq.com/docs/in-depth-usage

base_url="https://data.nasdaq.com/api/v3/"
ticker_url="datasets/FSE/AFX_X.json"
params={'api_key':API_KEY,'start_date':'2017-01-01','end_date':'2017-01-02'}

r = requests.get(base_url+ticker_url, params=params)

r.status_code

r.json()

# Convert to dictionary

data_json = json.loads(r.text)
my_dict = data_json

AFX_dict=r.json()

data_dict=AFX_dict['dataset']['data']
print(data_dict)

# Define lists for the following questions
#1. What are the highest and lowest opening prices of this stock within the period?
#2. Convert the returned JSON object into a Python dictionary.
#3. Calculate what the highest and lowest opening prices were for the stock in this period.
#4. What was the largest change in any one day (based on High and Low price)?
#5. What was the largest change between any two days (based on Closing Price)?
open_list=[]
change_list=[]
twoday_list=[]
Ave_daily_trading_vol_year=[]

for i in range(len(data_dict)):
    if data_dict[i][1] is not None:
        open_list.append(data_dict[i][1])
    change_list.append(abs(data_dict[i][2]-data_dict[i][3]))
    if i>1:
        twoday_list.append(abs(data_dict[i][4]-data_dict[i-1][4]))
    Ave_daily_trading_vol_year.append(data_dict[i][6])

# highest opening and lowest opening
print(max(open_list))
print(min(open_list))

# largest and smallest daily change
print(max(change_list))
print(min(change_list))

# largest 2 day change
print(max(twoday_list))

#What was the average daily trading volume during this year?
print(sum(Ave_daily_trading_vol_year)/len(Ave_daily_trading_vol_year))

#What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.
def median_list(trading_list):
    trading_list.sort()
    len_list=len(trading_list)
    #print(trading_list)
    #print(len_list)
    #if remainder exists, meaning odd number
    if len_list%2:
        med_index=(len_list//2)+1
        #print("divisble by two",med_index)
        return trading_list[med_index]
    else:
        med_index=(len_list-1)//2
        #print(med_index)
        return (trading_list[med_index]+trading_list[med_index+1])/2

median_list(Ave_daily_trading_vol_year)