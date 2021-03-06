import time, threading
from datetime import datetime
from selenium import webdriver

class Bot():
    url = 'https://sfbay.craigslist.org/sfc/cto/d/concord-2005-vw-passat-motion-18t/7091270964.html' # target add url
    ip_file_name = 'ips-test.txt' # IP file
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
            with open(f'worked_ips_{self.worked_time}.txt', 'a') as g:
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
        self.worked_time = datetime.now()
        j = 0
        break_loop = False
        while not break_loop:
            threads = []
            for i in range(j, j + self.worker_count):
                with open(self.ip_file_name, 'r') as f:
                    proxies = f.readlines()
                    if j == len(proxies)-1:
                        break_loop = True
                        break
                    proxy = proxies[j]
                j += 1
                print(f'loop count {j}')
                x = threading.Thread(target=self.click, args=(proxy,))
                x.start()
                threads.append(x)
            
            for thread in threads:
                thread.join()
            
            
                

if __name__ == '__main__':
    bot = Bot()