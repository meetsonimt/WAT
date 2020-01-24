from browsermobproxy import Server
import psutil
import os
import time
import json
from haralyzer import HarParser, HarPage
from selenium import webdriver
import pprint

class HttpTrafficHAR:
    def __init__(self):
        pass
    def get_HAR(self,url,term=None):
        for proc in psutil.process_iter():
    # check whether the process name matches
            if proc.name() == "browsermob-proxy":
                proc.kill()

        dict = {'port': 8090}
        server = Server(path="C:/Santosh/WAT/WAT/browsermob-proxy-2.1.4/bin/browsermob-proxy", options=dict)
        server.start()
        time.sleep(1)
        proxy = server.create_proxy()
        #proxy.new_har('req',options={'captureHeaders': True,'captureContent':True})
        time.sleep(1)
        profile = webdriver.FirefoxProfile()
        selenium_proxy = proxy.selenium_proxy()
        profile.set_proxy(selenium_proxy)
        driver = webdriver.Firefox(firefox_profile=profile)
        proxy.new_har(term,options={'captureHeaders': True,'captureContent':True})
        driver.get(url)# replace with url
        #with open('data.txt', 'w') as outfile:
        #    json.dump(proxy.har, outfile)
        #results = []
        #print(type(proxy.har))
        #har_parser = HarParser(json.loads(str(proxy.har).replace("\'","\"")))
        #har_data = json.loads(str(proxy.har).replace("\'","\""))
        har_data = proxy.har# json.loads(proxy.har)
        server.stop()
        driver.quit()
        return har_data
        #pprint.pprint(proxy.har)
          

#myobj = HttpTrafficHAR()
#a = myobj.get_HAR("https://docs.python.org/3/reference/lexical_analysis.html","lexical")
#print(a)
