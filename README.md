# Data Engineer Coding Challenge 
This page will introduce the code I wrote for Data Engineer Coding Challenge(DECC).

# What is it
- This program I wrote is for crawling news articles from www.bbc.com/news. 
- In this program,you can crawl articles and those articles will be stored in my MongoDB hosted on [Compose](https://compose.io/).
- When you do the search by title, the title keyword have to be complete title such as "Delta blames power cut for worldwide flight delays" and the section should be like "Magazine" when doing search by section, because there is no fuzzy query implemented. 
- You can always find out more section names from www.bbc.com/news.

# How to run it
Download those codes and start with usage shown as below:

Usage:
- python2.7 decc.py -h(help)
- python2.7 decc.py -c(crawl articles)
- python2.7 decc.py -s(search article by section) <section>
- python2.7 decc.py -t(search article by title) <title>

