
import scrapy
import re

class MyCrawlSpider(scrapy.Spider):
    name = "opinioncrawler"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/commentisfree",]


    def parse(self, response):
        opinions = response.css('#opinion .fc-slice-wrapper  li.l-row__item .fc-item .fc-item__container')

        
        for opinion in opinions:
            title = opinion.css('span.js-headline-text::text').get()
            url = opinion.css('a.fc-item__link::attr(href)').get()
            byline = opinion.css(' .fc-item__byline::text').get().strip()
            date_regex = r"\d{4}/\w{3}/\d{2}"
            match = re.search(date_regex, url)
            if match:
                date = match.group(0)

            yield {
                "title" : title,
                "byline" : byline,
                "url" : url,
                "date" : date
                }
        
