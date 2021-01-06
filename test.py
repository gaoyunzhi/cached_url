#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cached_url

if __name__ == '__main__':
	url = 'https://www.coolloud.org.tw/'
	url = 'https://www.evernote.com/l/AO_PIYii3ddBnZUE832bbYtnMkNqfJnZxOU?json=1'
	# url = 'https://img9.doubanio.com/view/status/l/public/64f0c054cbc6f3d.jpg'
	# url = 'http://www.infzm.com/wap/#/content/198828'
	cached_url.get(url)