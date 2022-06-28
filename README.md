# Stock-Data-Collector
# Goal
Collect data for list of companies given in InstrumentsList file for given time period from API and save them into individual file.
# instruction
This program is worked for Indian Stock market only.
You have to create api_key and api_secret from https://kite.trade/.
To download historical data you have to purchase their plan.

# How to run
paste your api_key and api_secret into configLogin.py
run generateAccessToken.py to generate access_token and save it to access_token.txt
run download_instrumentsList.py to get available stock name and their related info and save it to excel file.
edit downloaded excel file as per requirement.(delete rows with respect to its stock name whose data you don't wants to download.
open main.py in editer and change input condition as per your need and then run that file.
