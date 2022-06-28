from kiteconnect import KiteConnect,exceptions as kiteExceptions
import pandas as pd
from configLogin import api_key
from datetime import datetime
import logging
import requests

# to give sound feedback when error occurred or process is completed
import winsound
duration = 1000  # milliseconds
freq = 4400  # Hz

#require imput
from_date="2021-05-28"
to_date=datetime.today().strftime('%Y-%m-%d') # should be in yyyy-mm-dd hh:mm:ss
forNaming=datetime.today().strftime('%Y%m%d') # should be in yyyy-mm-dd hh:mm:ss
relativePath = "./data/20210729/"
timeInterval = "minute" # options =[minute,day,3minute,5minute,10minute,15minute,30minute,60minute]

# connecting to kite api
kite = KiteConnect(api_key=api_key)
try:
    acess_token = open('access_token.txt','r').read()
    kite.set_access_token(acess_token)
    
except kiteExceptions.TokenException: 
    logging.error("Exception occurred", exc_info=True)
    print("done")
# stock name is taken from file given in below. run download_instrumentsList.py 
# to create below file and remove stock records whose data you don't want to download.
df=pd.read_excel("instrumentList.xlsx")
df.size
completed=[]

#df['name'].unique() gives ['BANKNIFTY','PVR','VOLTAS',] 
try:
    for x in df['name'].unique():
        print(x)
        maindf=pd.DataFrame()
        for y in df.loc[df['name']==x]['instrument_token']:
            temprecords = kite.historical_data(y,from_date=from_date,to_date=to_date,interval=timeInterval,oi=True)
            tempdf = pd.DataFrame(temprecords)
            tempdf['instrument_token']=y

            maindf=maindf.append(tempdf, ignore_index=True)
        maindf.to_csv("{0}1M{1}{2}.csv".format(relativePath,x,forNaming),index=False)
        completed.append(x)
        df.drop(df.loc[df['name']==x].index,inplace=True)
    winsound.Beep(freq, duration)
    print('done')
except requests.exceptions.Timeout:
    winsound.Beep(freq, duration)
    print("RTE")

except Exception as error:
    winsound.Beep(freq, duration)
    print(error)
