import Scrapetsy

if __name__ == '__main__':
    se = Scrapetsy.get_response(driver_path='C:/geckodriver-v0.31.0-win64/geckodriver.exe',
                   pagination=True)
    proxies = se.get_proxy()
    urls = se.get_url(url='https://www.etsy.com/search?q=gift+for+women&ref=pagination&anchor_listing_id=737271222&page=250', proxies=proxies)
    data = []
    for url in urls:
        data.append(se.get_detail(url, proxies = proxies))
    se.create_file(data=data, filepath='C:/project/Scrapetsy/result.csv')