import time
from selenium import webdriver

class Bot():

    def __init__(self):
        # PROXY = '136.25.2.43:40614'
        # webdriver.DesiredCapabilities.FIREFOX['proxy']={
        #     "httpProxy":PROXY,
        #     "ftpProxy":PROXY,
        #     "sslProxy":PROXY,
        #     "proxyType":"MANUAL",
        # }
        # profile = webdriver.FirefoxProfile()

        # profile.set_preference("dom.webnotifications.enabled", False)
        
        with open('./ips-test.txt', 'r') as f:
            for i in f.readlines():
                try:
                    print(i)
                    PROXY = i
                    webdriver.DesiredCapabilities.FIREFOX['proxy']={
                        "httpProxy":PROXY,
                        "ftpProxy":PROXY,
                        "sslProxy":PROXY,
                        "proxyType":"MANUAL",
                    }
                    browser_driver = webdriver.Firefox()
                    browser_driver.set_page_load_timeout(40)
                    browser_driver.get('https://httpbin.org/ip')
                    time.sleep(4)
                    browser_driver.close()
                    with open('worked_ips.txt', 'a') as g:
                        g.write(i)
                except:
                    browser_driver.close()
                    print('error')
                

if __name__ == '__main__':
    bot = Bot()