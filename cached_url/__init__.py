#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'cached_url'
import os
import sys
import hashlib
import requests

def getUrlContent(url):
	headers = {
		'method': 'GET',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
	}
	return requests.get(url, headers=headers).text

def cachedContent(url):
	cache = 'tmp/' + hashlib.sha224(url.encode('utf-8')).hexdigest()[:3] + '.html'
	try:
		with open(cache) as f:
			return f.read()
	except:
		content = getUrlContent(url)
		os.system('mkdir tmp > /dev/null 2>&1')
		with open(cache, 'w') as f:
			f.write(content)
		return content

def get(url):
	if 'test' in str(sys.argv):
		return cachedContent(url)
	else:
		return getUrlContent(url)