
import re
import codecs

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MyCrawlSpider(CrawlSpider):
    name = "opinioncrawler"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/commentisfree"]

    rules = (
         Rule(LinkExtractor(allow="commentisfree/2023/"), callback = "parse_item"),
    )

    def parse_item(self, response):
        article_response = response.css("#maincontent").get()
        url = response.url

        yield {
            "date" : url[42:53],
            "title": response.css("h1::text").get(),
            "author": response.css(".dcr-1uv1bpy a::text").get(),
            "article" : re.sub(r'<.*?>', '', article_response),
            "url" : url,
            }