from WAT1_0.utilities.HAR_processor import HttpTrafficHAR
import pprint
from lxml import html
import json

class SerachData(HttpTrafficHAR):
    def __init__(self):
        pass
    def searching_filter_records(self,json_data,term):
        data = json_data['log']['entries']
        term = term.split(' ') #if term contains space
        search_list = list()
        if len(term) > 1:
                for row in data:
                    for item in term:
                        if item in row['request']['url'] or item in row.get('request').get('postData',''):
                            search_list.append({
                                'request': item.get('request'),
                                'response': item.get('response'),
                                'content': item.get('response').get('content').get('text',"")
                            })
        else:
            for row in data:
                if term[0] in row['request']['url'] or term[0] in row.get('request').get('postData',''):
                    search_list.append({
                        'request': row.get('request'),
                        'response': row.get('response'),
                        'content': row.get('response').get('content').get('text',"")
                        })
       
        #now we have to find search term in content
        filter_data_depth_1 = list()

        for item in search_list:
            temp_content = item.get('content')
            if term[0] in temp_content:
                filter_data_depth_1.append({
                    'request' : item.get('request'),
                    'response' : item.get('response'),
                    'content' : item.get('response').get('content').get('text')
                })
        #now we will find search term in the html and grab that term using xpath
        find_by_keyword_xpath = "//title[\"{}\"]".format(term[0])
        find_by_title_xpath = "//title[\"{}\"]".format(term[0])
        #//*[contains(.,"results for usb")]
        find_by_free_text_xpath = "//*[contains(.,\"results for {}\"]".format(term[0])
        #pprint.pprint(find_by_keyword_xpath +"-" + find_by_title_xpath + "-" + find_by_free_text_xpath)
        filter_data_depth_2 = list()
        for data in filter_data_depth_1:
            temp_content = data.get('content')
            if html.fromstring(temp_content).find('.//*') is not None:
                doc = html.fromstring(temp_content)
                if doc.xpath(find_by_keyword_xpath) or doc.xpath(find_by_title_xpath) or doc.xpath(find_by_free_text_xpath):
                    IsJson = "HTML Response"
                    filter_data_depth_2.append({
                    'request' : data.get('request'),
                    'response' : data.get('response'),
                    'content' : data.get('response').get('content').get('text'),
                    'IsJson' : IsJson
                })   
            else: #if we found Response Type other than HTML
                filter_data_depth_2.append({
                    'request' : data.get('request'),
                    'response' : data.get('response'),
                    'content' : data.get('response').get('content').get('text'),
                    'IsJson' : "Json Response"
                })   


        pprint.pprint(len(filter_data_depth_2))
        with open('data.txt', 'w') as outfile:
            json.dump(filter_data_depth_2, outfile)
        return filter_data_depth_2