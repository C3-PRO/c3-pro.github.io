#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('build', 'templates'))

# index page (with architecture)
index = env.get_template('index.html')
with io.open('index.html', 'w', encoding='utf-8') as h:
	h.write(index.render())
