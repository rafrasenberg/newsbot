import scrapy
import nltk
from scraper.items import ArticleItem

class WikiSpider(scrapy.Spider):
    name = "wikinews"
    start_urls = ["https://en.wikinews.org/wiki/Main_Page"]

    def parse(self, response):
        data = response.xpath("//div[@class='latest_news_text']//ul//li")

        for line in data:
            link = line.xpath(".//a/@href").extract_first()
            full_link = 'https://en.wikinews.org' + link
            
            yield scrapy.Request(url=full_link, callback=self.parse_attr)


    def parse_attr(self, response):
        item = ArticleItem()

        text = "".join(response.xpath("(//div[@class='mw-parser-output']/p)").extract())
        title = "".join(response.xpath("(//h1[@id='firstHeading']/text())").extract())
        image = response.urljoin("".join(response.xpath("(//div[@class='thumbinner']//a//img/@src)[1]").extract()))

        item['title'] = title
        item['text'] = text
        item['image'] = image

        yield item