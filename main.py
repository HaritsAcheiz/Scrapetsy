import Scrapetsy

if __name__ == '__main__':
    se = Scrapetsy.get_response(headers='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0',
                   driver_path='C:/geckodriver-v0.31.0-win64/geckodriver.exe',
                   pagination=False)
    response = se.get_url(url='https://www.etsy.com/search?q=gift+for+women&ref=pagination&anchor_listing_id=737271222&page=1')
    print(response)