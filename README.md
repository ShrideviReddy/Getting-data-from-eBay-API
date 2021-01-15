# Getting Data from eBay API
This repository contains code for scraping data from eBay API and write data to csv. I wanted to scrape listing and price data for my new project. Hence I have used finding API for this purpose. 
Refer eBay API documentation for more on different API and their usage. 
## Getting Started:
To use eBay API, you need to register for eBay developer program. Click [here](https://developer.ebay.com/) and Register. If you have already registered then sign-in to get application keys.  Get both Sandbox and Production. You need following info while scraping data:
* App ID
* Dev
* Cert ID
* User Token

For finding API , you just need App ID. But for some other API's you need all of them.
## Setting EbaySDK:
Install ebaysdk using pip.
```
pip install ebaysdk
```
Then clone this [repo](https://github.com/timotheus/ebaysdk-python.git).
```
git clone https://github.com/timotheus/ebaysdk-python.git
```
## After cloning:
After cloning repo, it will be download as ebaysdk-python. In ebaysdk-python folder check for ebaysdk.
This folder has code for different API. Copy code and edit as per your requirement.
I have edited finding file to get data and save in CSV file. 

Following screenshot shows response you get from API:

![Response from eBay API](/img/Response_dict.PNG)

It's in dictionary format. Check dictionary format and use you dictionary subsetting skills to get data in format you want. 
