import Scrapetsy

if __name__ == '__main__':
    se = Scrapetsy.get_response(driver_path='C:/geckodriver-v0.31.0-win64/geckodriver.exe',
                   pagination=False)
    proxies = se.get_proxy(url='https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')
    urls = se.get_url(url='https://www.etsy.com/search?q=gift+for+women&ref=pagination&anchor_listing_id=737271222&page=1', proxies=proxies)
    data = []
    for url in urls:
        data.append(se.get_detail(url, proxies = proxies))
    se.create_file(data=data)