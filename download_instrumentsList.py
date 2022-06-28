from kiteconnect import KiteConnect,exceptions as kiteExceptions
import pandas as pd
import logging
from configLogin import api_key

outputFileName = "NewInstrumentsList03062021.xlsx"

#connect to Kite API service
kite = KiteConnect(api_key=api_key)
try:
    # read access token from file which was saved manually by user (you) by login into your trading account with zerodha
    acess_token = open('access_token.txt','r').read()
    kite.set_access_token(acess_token)
    
except kiteExceptions.TokenException: 
    logging.error("Exception occurred", exc_info=True)
    print("done")
    
# hit API which gives list of instruments.    
instrumentsList=kite.instruments(exchange=kite.EXCHANGE_NFO)

#change it to dataFrame
df = pd.DataFrame(instrumentsList)

#save it in excel file format.
df.to_excel(outputFileName,index=False)
