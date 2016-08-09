#!/usr/bin/python
import sys, getopt
sys.path.append('./')

from article_model import BBCArticleItem
from DECCSpider import BBCArticleSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main(argv):

	try:
		opts, args = getopt.getopt(argv, "ch:t:s:", ['title=', 'section='])
	except getopt.GetoptError:
		print 'Usage:\npython2.7 decc.py -h(help)\npython2.7 decc.py -c(crawl articles)\npython2.7 decc.py -s(search article by section) <section>\npython2.7 decc.py -t(search article by title) <title>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage:\npython2.7 decc.py -h(help)\npython2.7 decc.py -c(crawl articles)\npython2.7 decc.py -s(search article by section) <section>\npython2.7 decc.py -t(search article by title) <title>'
			sys.exit()
		elif opt == '-c':
			# start crawling article here
			print "crawling"
			process = CrawlerProcess(get_project_settings())
			process.crawl(BBCArticleSpider)
			process.start()
		elif opt in  ('-t', '--title'):
			print "search by title"
			# start searching article by title
			results = BBCArticleItem.fetch_by_title(arg)
			for result in results:
				print result
		elif opt in ('-s', '--section'):
			print "search by section"
			# start searching article by section
			results = BBCArticleItem.fetch_by_section(arg)
			for result in results:
				print result

if __name__ == "__main__":
	main(sys.argv[1:])

