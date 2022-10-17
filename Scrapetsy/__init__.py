'''
This is package to get detail product from www.etsy.com
'''

# Import external package
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Define Class Scrapetsy
class get_response:

    # define class variable
    def __init__(self, headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
                 driver_path='C:/geckodriver-v0.31.0-win64/geckodriver.exe',
                 pagination=False,
                 webdriver_opt={'head': '--headless',
                                'sandbox': '--no-sandbox',
                                'gpu' :'--disable-gpu',
                                'translate': '--disable-translate',
                                'user-agent':  "user-agent='Mozilla/5.0 "
                                              "(Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'"}
                 ):
        self.headers = headers
        self.driver_path = driver_path
        self.pagination = pagination
        self.webdriver_opt = webdriver_opt

    # define class function
    def get_url(self, url):
        options = Options()
        options.add_argument(self.webdriver_opt['head'])
        options.add_argument(self.webdriver_opt['sandbox'])
        options.add_argument(self.webdriver_opt['gpu'])
        options.add_argument(self.webdriver_opt['translate'])
        options.add_argument(self.webdriver_opt['user-agent'])
        driver = webdriver.Firefox(executable_path=self.driver_path, options=options)
        driver.get(url)
        response = WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.ID, 'content')))
        parent = response.find_element(By.XPATH, "//ul[@class='wt-grid wt-grid--block wt-pl-xs-0 tab-reorder-container']")
        child = parent.find_elements(By.XPATH, "//li[@class='wt-list-unstyled wt-grid__item-xs-6 wt-grid__item-md-4 wt-grid__item-lg-3 wt-order-xs-0 wt-order-md-0 wt-order-lg-0 wt-show-xs wt-show-md wt-show-lg']")
        hasil=[]
        for i in child:
            item=i.find_element(By.XPATH, "//a").get_attribute('href')
            hasil.append(item)
        return hasil


