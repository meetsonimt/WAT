from WAT1_0.utilities.HAR_processor import HttpTrafficHAR
import pprint
import json
from lxml import html

class ProductData(HttpTrafficHAR):
    def __init__(self):
        pass
    def product_filter_records(self,json_data,link):
        data = json_data['log']['entries']
        product_list = list()
        if data:
            for row in data:
                product_list.append({
                'request': row.get('request'),
                'response': row.get('response'),
                'content': row.get('response').get('content').get('text')
                })
       
        #now we have to find product in content
        find_by_title_xpath = "//meta[@property=\"og:title\"]/@content"

        filter_data_depth_1 = list()
        for data in product_list:
            temp_content = data.get('content')
            print(temp_content)
            if temp_content and html.fromstring(temp_content).find('.//*') is not None:
                doc = html.fromstring(temp_content)
                if link in data.get('request').get('url') or doc.xpath(find_by_title_xpath):
                    IsJson = "HTML Response"
                    filter_data_depth_1.append({
                    'request' : data.get('request'),
                    'response' : data.get('response'),
                    'content' : data.get('response').get('content').get('text'),
                    'IsJson' : IsJson
                })   
            else: #if we found Response Type other than HTML
                filter_data_depth_1.append({
                    'request' : data.get('request'),
                    'response' : data.get('response'),
                    'content' : data.get('response').get('content').get('text'),
                    'IsJson' : "Json Response"
                }) 

        with open('data.txt', 'w') as outfile:
            json.dump(filter_data_depth_1, outfile)
        return filter_data_depth_1
# obj = ProductData()
# link="https://www.ebay.com/itm/USB-2-0-Printer-Cable-A-B-Male-Type-for-Dell-HP-Canon-Dell-Lexmark-Brother-Epson/303446800496"
# data = obj.get_HAR(link)
#print(obj.product_filter_records(data,link))