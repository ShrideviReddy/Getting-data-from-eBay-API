# Getting Data from eBay API
This repository contains code for scraping data from eBay API and write data to csv. I wanted to scrape listing and price data for my new project. Hence I have used finding APIfor this purpose. 
Refer eBay API documentation for more on different API and their usage. 
## Getting Started:
To use eBay API, you need to register for eBay developer program. Click [here](https://developer.ebay.com/) and Register. If you have already registered then sign-in to get application keys.  Get both Sandbox and Production. You need following info while scraping data:
* App ID
* Dev
* Cert ID
* User Token

For finding API , you just need App ID. But for some other APIS you need all of them.
## Setting EbaySDK
Install ebaysdk using pip.Then clone this [repo](https://github.com/timotheus/ebaysdk-python.git).
## After cloning:
After cloning repo, it will be download as ebaysdk-python. In ebaysdk-python folder check for ebaysdk.
This folder has code for different API. 
