from browsermobproxy import Server
import psutil
import os
import time
import json
from haralyzer import HarParser, HarPage
from selenium import webdriver

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
        time.sleep(1)
        profile = webdriver.FirefoxProfile()
        selenium_proxy = proxy.selenium_proxy()
        profile.set_proxy(selenium_proxy)
        driver = webdriver.Firefox(firefox_profile=profile)
        proxy.new_har(term)
        driver.get(url)# replace with url
        #json.loads(proxy.har)['log']
        #har_parser = HarParser(json.loads(str(proxy.har).replace("\'","\"")))
        har_data = json.loads(str(proxy.har).replace("\'","\""))
        server.stop()
        driver.quit()
        return har_data
        #print(har_data)
        #for h in har_data['log']['entries']:
        #    print(h)
        #print (json.loads(proxy.har)['log']) # returns a HAR JSON blob       

myobj = HttpTrafficHAR()
a = myobj.get_HAR("https://www.snapdeal.com/search?keyword=usb","usb")
print(a)
