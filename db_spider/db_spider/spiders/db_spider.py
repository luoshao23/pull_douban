import scrapy

class db_Spider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [ "https://movie.douban.com/subject/25937854/" ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
        	f.write(response.body)
