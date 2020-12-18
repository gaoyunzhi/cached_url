#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cached_url

url = 'https://www.bbc.com/zhongwen/simp'
# url = 'https://img9.doubanio.com/view/status/l/public/64f0c054cbc6f3d.jpg'
print(cached_url.getFilePath(url))