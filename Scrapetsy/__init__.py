'''
This is package to get detail product from www.etsy.com
'''



# Import external package
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random
import json
import requests


# Define Class Scrapetsy
class get_response:

    # define class variable
    def __init__(self, headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
                 driver_path='C:/geckodriver-v0.31.0-win64/geckodriver.exe',
                 pagination=False,
                 webdriver_opt={'head': '--headless',
                                'sandbox': '--no-sandbox',
                                'gpu' :'--disable-gpu',
                                'translate': '--disable-translate'}
                 ):
        self.headers = headers
        self.driver_path = driver_path
        self.pagination = pagination
        self.webdriver_opt = webdriver_opt

    # define class function
    def get_url(self, url, proxies):
        ua = ['Mozilla/5.0 (Windows NT 6.2; rv:84.0.2) Gecko/20100101 Firefox/84.0.2 anonymized by Abelssoft 298666885',
              'Mozilla/5.0 (Linux; Android 9; POT-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 10; SM-J810G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.346',
              'Mozilla/5.0 (Linux; Android 7.0; HM-G552-FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 8.0.0; G3221) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36',
              'Mozilla/5.0 (Linux; Android 9; COR-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/61.2.3076.56749',
              'Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.7.7) Gecko/20050414 Firefox/50.0.1',
              'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 OcIdWebView ({\x22os\x22:\x22iOS\x22,\x22appVersion\x22:\x225.58.3\x22,\x22app\x22:\x22com.google.Maps\x22,\x22osVersion\x22:\x2214.2\x22,\x22style\x22:2,\x22isDarkTheme\x22:false,\x22libraryVersion\x22:\x221.19.10.0\x22,\x22zoom\x22:0.90947546531302881})',
              'Mozilla/5.0 (Linux; Android 6.0.1; Moto G Play Build/MPI24.241-15.3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/290.0.0.44.121']
        user_agent=random.Random(500).choice(ua)
        print(user_agent)
        options = Options()
        options.add_argument(self.webdriver_opt['head'])
        options.add_argument(self.webdriver_opt['sandbox'])
        options.add_argument(self.webdriver_opt['gpu'])
        options.add_argument(self.webdriver_opt['translate'])
        options.add_argument(f"user-agent={user_agent}")
        options.add_argument('--proxy-server=%s' % proxies)
        driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
        driver.get(url)
        response = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'content')))
        parent = response.find_element(By.CSS_SELECTOR, ".wt-grid.wt-grid--block.wt-pl-xs-0.tab-reorder-container")
        child = parent.find_elements(By.CSS_SELECTOR, ".wt-list-unstyled.wt-grid__item-xs-6.wt-grid__item-md-4.wt-grid__item-lg-3.wt-order-xs-0.wt-order-md-0.wt-order-lg-0.wt-show-xs.wt-show-md.wt-show-lg")
        hasil=[]
        print(len(child))
        for i in child:
            item=i.find_element(By.TAG_NAME, "a").get_attribute('href')
            hasil.append(item)
        driver.quit()
        return hasil

    def get_proxy(self, url):
        ### Set the first result from Geonode result ###
        proxy_index = 0

        try:
            ### Request keys and values from Geonode. ###
            proxy_json_url = json.loads(requests.get(
                url=url).text)
            prox = random.choice(proxy_json_url['data'])
            print(f"{prox['ip']}:{prox['port']}")
            ### Return a string based on "proxy_index" (first result). ###
            return f"{prox['ip']}:{prox['port']}"

        except requests.exceptions.ProxyError:
            ### Return '' string on error ###
            return ""
