from pathlib import Path
import scrapy
from scrapy.http import headers
from scrapy_selenium import SeleniumRequest



class JobScraper(scrapy.Spider):
    name="jobs"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
    def start_requests(self):
        urls = [#urls go here],
        for [url] in urls:
            print("URLS:  ",url)
            yield SeleniumRequest(url=url,headers=self.headers,callback=self.parse)

    def parse(self, response):
        page = response.body
        filename=f'indeed.html'
        Path(filename).write_bytes(response.body)



