from browsermobproxy import Server
server = Server("C:\Santosh\WAT\WAT\browsermob-proxy-2.1.4\bin")
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://www.google.com")
proxy.har # returns a HAR JSON blob

server.stop()
driver.quit()