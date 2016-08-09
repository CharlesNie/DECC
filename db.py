from pymongo import MongoClient
import ssl


class MongoDB:

	db_uri = 'mongodb://DECC:fortestonly@aws-us-east-1-portal.17.dblayer.com:11853/DECCdb'
	
	def __init__(self, uri=None):
		if uri is not None:
			self.db_uri = uri

		# ssl_cert_reqs for security concern, use non cert here
		self.client = MongoClient(self.db_uri, ssl_cert_reqs=ssl.CERT_NONE)
		self.db = self.client.get_default_database().DECCdb


	def insert_article(self, article):
		self.db.insert_one(article)

	
	def update_article(self, article, updates={}):	
		self.db.update_one({"_id": article._id},
					{
						"$set": updates 
					}
					)


	def find_article_by_title(self, title):
		cursor = self.db.find({"title":title})
		for document in cursor:
			yield document

	def find_articles_by_section(self, section):
		cursor = self.db.find({"section":section})
		for document in cursor:
			yield document

