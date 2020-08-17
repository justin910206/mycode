#!/usr/bin/env python3

import requests

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=DEMO_KEY' ## replace this with our API key

    if custom_end == 'q':
        neourl = neourl + startdate + mykey
    else:
        neourl = neourl + startdate + enddate mykey






    neojson = (requests.get(neourl)).json()

    print(neojson)

## call main
main()
print(main)
