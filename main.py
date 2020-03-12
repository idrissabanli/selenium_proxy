import time, threading
from datetime import datetime
from selenium import webdriver

class Bot():
    url = 'https://sfbay.craigslist.org/sfc/cto/d/concord-2005-vw-passat-motion-18t/7091270964.html' # target add url
    ip_file_name = 'worked_ips_12_03_2020_11_44.txt' # IP file
    worker_count = 2 # selenium bot count

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
            browser_driver.get(self.url)
            with open(f'worked_ips_{datetime.now()}.txt', 'a') as g:
                g.write(i)
            element = browser_driver.find_element_by_class_name("flag")
            if element:
                element.click()
                print(f"Proxy ip ----- {PROXY} clicked")
            browser_driver.close()
        except Exception as e:
            browser_driver.close()
            print(f"Proxy ip ----- {PROXY} error", e)

    def __init__(self):

        with open(self.ip_file_name, 'r') as f:
            proxies = f.readlines()
            j= 0
            while True:
                threads = []
                for proxy in proxies[j:j+self.worker_count]:
                    j += 1
                    print(f'loop count {j}')
                    x = threading.Thread(target=self.click, args=(proxy,))
                    x.start()
                    threads.append(x)
                
                for thread in threads:
                    thread.join()
                
                if j == len(proxies):
                    break
                

if __name__ == '__main__':
    bot = Bot()