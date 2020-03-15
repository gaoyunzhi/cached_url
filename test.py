#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cached_url

print(cached_url.get('https://www.bbc.com/zhongwen/simp'))
print(cached_url.get('https://img9.doubanio.com/view/status/l/public/64f0c054cbc6f3d.jpg', mode='b'))