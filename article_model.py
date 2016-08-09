from db import MongoDB
import scrapy

db = MongoDB()

# BBC article model
class BBCArticleItem(scrapy.Item):
	_id = scrapy.Field() # preset id field for mongo db
	title = scrapy.Field()
	date = scrapy.Field()
	time = scrapy.Field()
	section = scrapy.Field()
	content = scrapy.Field()
	url = scrapy.Field()
	
	def save(self):
                # write data to database
                db.insert_article(self)

        def update(self, updates={}):
                db.update_article(self, updates)


	@classmethod
        def fetch_by_title(cls, title):
                results = db.find_article_by_title(title)
                return cls.parse_result(results)


	@classmethod
        def fetch_by_section(cls, section):
                results = db.find_articles_by_section(section)
                return cls.parse_result(results)

	@classmethod
	def parse_result(cls, results):
		for result in results:
			article = BBCArticleItem()
                        article['_id'] = result['_id']
                        article['title'] = result['title']
                        article['date'] = result['date']
                        article['time'] = result['time']
                        article['section'] = result['section']
                        article['content'] = result['content']
                        article['url'] = result['url']
                        yield article
