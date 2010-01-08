#!/usr/bin/env python

import urllib2
from stream import AsyncThreadPool

URLs = ['http://www.cnn.com/',
	'http://www.bbc.co.uk/',
	'http://www.economist.com/',
	'http://nonexistant.website.at.baddomain/',
	'http://slashdot.org/',
	'http://reddit.com/',
	'http://news.ycombinator.com/',
]

def retrieve(urls, timeout=10):
	for url in urls:
		yield url, urllib2.urlopen(url, timeout=timeout).read()

if __name__ == '__main__':
	retrieved = URLs >> AsyncThreadPool(retrieve, poolsize=4)
	for url, content in retrieved:
		print '%r is %d bytes' % (url, len(content))
	for url, exception in retrieved.failure:
		print '%r failed: %s' % (url, exception)
