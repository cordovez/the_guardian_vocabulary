
import scrapy
import re
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class MyCrawlSpider(scrapy.Spider):
    name = "opinioncrawler"
    allowed_domains = ["theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/commentisfree",]

    def parse(self, response):
        opinions = response.css(
            '#opinion .fc-slice-wrapper  li.l-row__item .fc-item .fc-item__container')

        for opinion in opinions:
            title = opinion.css('span.js-headline-text::text').get()
            url = opinion.css(' ::attr(href)').get()
            byline = opinion.css(' .fc-item__byline::text').get().strip()
            date_regex = r"\d{4}/\w{3}/\d{2}"
            match = re.search(date_regex, url)
            if match:
                date = match.group(0)

            yield scrapy.Request(url, callback=self.parse_text, meta={
                "title": title,
                "byline": byline,
                "url": url,
                "date": date,
            })

    # follow url to get article text
    def parse_text(self, response):
        title = response.meta["title"]
        byline = response.meta["byline"]
        url = response.meta["url"]
        date = response.meta["date"]

        # Join all the <p>s
        html_text = "".join(response.css('.dcr-1bfjmfh').getall())
        # remove all html tags
        clean_text = re.sub(r'<[^>]*>', '', html_text)

        yield {
            "title": title,
            "byline": byline,
            "url": url,
            "date": date,
            "text": clean_text.replace('\n', '').replace('\r', ''),
        }
