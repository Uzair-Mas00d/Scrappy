import scrapy
from quotes_js_scraper.items import QuoteItem
 
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield SeleniumRequest(
                    url=url, 
                    callback=self.parse, 
                    # wait_time=10, if quote div cannot visible within 10 sec it throw an error make sure to adjust wait_time according to your need 
                    # wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'quote'))   wait until all quote div renders on browser
                    script="document.querySelector('.pager .next>a').click()", # for clicking button on web
                    )

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.selector.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item