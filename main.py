import time, threading
from selenium import webdriver

class Bot():

    def click(self, i):
        try:      
            PROXY = i
            webdriver.DesiredCapabilities.FIREFOX['proxy']={
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                "proxyType":"MANUAL",
            }
            firefox_profile = webdriver.FirefoxProfile()
            # firefox_profile.set_preference('permissions.default.stylesheet', 2)
            # firefox_profile.set_preference('permissions.default.image', 2)
            # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            browser_driver = webdriver.Firefox(firefox_profile=firefox_profile)
            browser_driver.set_page_load_timeout(300)
            browser_driver.get('https://sfbay.craigslist.org/sfc/cto/d/concord-2005-vw-passat-motion-18t/7091270964.html')
            with open('worked_ips_12_03_2020_18_15.txt', 'a') as g:
                g.write(i)
            element = browser_driver.find_element_by_class_name("flag")
            if element:
                element.click()
                print('clicked')
            browser_driver.close()
        except Exception as e:
            browser_driver.close()
            print('error', e)

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
        
        with open('worked_ips_12_03_2020_11_44.txt', 'r') as f:
            proxies = f.readlines()
            j= -1
            while True:
                j += 1
                threads = []
                for proxy in proxies[j:j+4]:
                    x = threading.Thread(target=self.click, args=(proxy,))
                    x.start()
                    threads.append(x)
                
                for thread in threads:
                    thread.join()
                print('here')
                

if __name__ == '__main__':
    bot = Bot()