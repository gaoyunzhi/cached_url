#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'cached_url'
import os
import sys
import hashlib
import requests
import re
import time


def getUrlContent(url, headers={}, mode='', sleep=0):
    headers['method'] = headers.get('method', 'GET')
    headers['accept'] = headers.get('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/apng,*/*;q=0.8,application/signed-exchange;v=b3')
    headers['user-agent'] = headers.get('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
    time.sleep(sleep)

    with requests.get(url, headers=headers, stream=True) as r:
        if r.status_code != 200:
            print('cached_url', url, r.status_code, r.text)
            raise Exception('HTTP ' + str(r.status_code) + ' : ' + url)

        if mode == 'b':  # for binary
            return r.content

        # for text
        accept_list = ['text', 'html', 'xml', 'json']
        if r.headers.get('content-type') and any(accept in r.headers['content-type'] for accept in accept_list):  # is webpage
            r.iter_content()
            if r.encoding == 'ISO-8859-1':  # requests use default ISO-8859-1 while encoding is not set
                r.encoding = None  # set encoding to None so Response.text() will detect the encoding
            return r.text

        raise Exception('Not a webpage: ' + url)


def getFileName(url):
    k = re.sub(r'\W+', '', url.strip('/').split('/')[-1].split('.')[0])[:8]
    h = hashlib.sha224(url.encode('utf-8')).hexdigest()[:15 - len(k)][:7]
    return k + '_' + h


def getFilePath(url):
    text = url
    for char in ['=', '&', ',']:
        text = text.replace(char, '.')
    text = text.split('?')[0]
    ext = os.path.splitext(text)[1] or '.html'
    if len(ext) > 10:
        ext = ext[0] + ext[-9:]
    return 'tmp/' + getFileName(url) + ext


def cachedContent(url, headers={}, mode='', sleep=0):
    cache = getFilePath(url)
    try:
        with open(cache, 'r' + mode) as f:
            return f.read()
    except:
        content = getUrlContent(url, headers, mode, sleep)
        os.system('mkdir tmp > /dev/null 2>&1')
        with open(cache, 'w' + mode) as f:
            f.write(content)
        return content


def get(url, headers={}, force_cache=False, mode='', sleep=0):
    if force_cache or 'test' in str(sys.argv):
        return cachedContent(url, headers, mode, sleep)
    else:
        return getUrlContent(url, headers, mode, sleep)
