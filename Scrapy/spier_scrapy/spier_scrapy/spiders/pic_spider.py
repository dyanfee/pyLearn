import scrapy


class ImageSpider(scrapy.Spider):
    name = "pic"
    allowed_domains = ["so.com"]
    start_urls = [
        "http://image.so.com/z?ch=wallpaper"
    ]

    def parse(self, response):
        filename ='testhhhhhh--------------------------' #response.url.split("/")[-2]
        print(filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
