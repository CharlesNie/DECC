import scrapy
from article_model import BBCArticleItem


# spider class 
class BBCArticleSpider(scrapy.Spider):
	name = 'bbcarticlespider'
	start_urls = ['http://www.bbc.com/news']
	

	# parsing from start_urls and get the sub menus under news section
	def parse(self, response):
		for url in response.xpath('//ul[contains(@role, "navigation")]/li/a/@href').extract():
			yield scrapy.Request(response.urljoin(url), self.parse_article_list)

	
	# parsing article list under sections found from above parse function
	def parse_article_list(self, response):
		for url in response.xpath('//a[contains(@class, "faux-block-link__overlay-link")]/@href').extract():
			yield scrapy.Request(response.urljoin(url), self.parse_article_detail)

	
	# get article details from list url found from above parse_article_list function
	def parse_article_detail(self, response):
		article = BBCArticleItem()
		article['title'] = response.xpath('//h1[contains(@class, "story-body__h1")]/text()').extract_first()
		if article['title'] is None:
			article['title'] = response.xpath('//h2[contains(@class, "unit_title")]/span/text()').extract_first()
		article['date'] = response.xpath('//div[contains(@class, "date")]/@data-datetime').extract_first()
		article['time'] = response.xpath('//div[contains(@class, "date")]/@data-seconds').extract_first()
		article['section'] = response.xpath('//a[contains(@class, "mini-info-list__section")]/text()').extract_first()
		article['content'] = response.xpath('//div[contains(@class, "story-body__inner")]/p/text()').extract()
		article['url'] = response.url

		article.save()

 
