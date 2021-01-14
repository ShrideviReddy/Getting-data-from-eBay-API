import ebaysdk
from ebaysdk.finding import Connection
import csv


#API connection and response. For more info refer eBay API documentation
def find_item_advanced(page_num):
    api = Connection(siteid='EBAY-US', appid= 'SHRIDEVI-MobileUp-PRD-4d4a886f5-dda79a36', config_file=None)

    #Following are product and details you want to get from API.
    api.execute('findItemsAdvanced', {
    'keywords': 'iphone xr',   
    'itemFilter': [{'name': 'Condition', 'value': 'Used'}],
    'paginationInput': {
        'entriesPerPage': '25',
        'pageNumber': page_num}})

    dictstr = api.response.dict()
    return dictstr

#Add csv writing function
def write_csv(response_dict):
	with open('IphoneXR_listing.csv', 'a', encoding='utf-8', newline = '') as csvfile:
		writer = csv.writer(csvfile)
		for i in range(25):
                    row = [response_dict['searchResult']['item'][i]['title'], response_dict['searchResult']['item'][i]['sellingStatus']['currentPrice']['value']]
                    writer.writerow(row)
		
def main():
    total_pages = 14  # Input: Total number of pages. You can use input() instead of specifying value here. 
    total_pages = min(total_pages, 100)
    for p in range(1, total_pages + 1):
        response_dict = find_item_advanced(p) #Get response
        write_csv(response_dict) #Write to CSV

if __name__ == '__main__':
    main()
