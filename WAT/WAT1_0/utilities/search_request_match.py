from HAR_processor import HttpTrafficHAR
import pprint

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
                        if item in row['request']['url']:
                            search_list.append({
                                'request': item['request'],
                                'response': item['response'],
                                'content': item['response']['content']['text']
                            })
        else:
            for row in data:
                if term[0] in row['request']['url']:
                    search_list.append({
                        'request': row['request'],
                        'response': row['response'],
                        'content': row['response']['content']['text']
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
        pprint.pprint(filter_data_depth_1)
obj = SerachData()
data = obj.get_HAR("https://docs.python.org/3/reference/lexical_analysis.html","lexical")
obj.searching_filter_records(data,"lexical")