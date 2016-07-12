#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import json
import os.path
import logging
from os import walk
from markdown import markdown

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('build', 'templates'))

# index page (with architecture/modules)
def render_index():
	index = env.get_template('index.html')
	with io.open('index.html', 'w', encoding='utf-8') as h:
		modules = {
			"mobile": [],
			"www": [],
			"backend": [],
			"storage": []
		}
		
		# read modules
		dirpath, _, filenames = next(walk('modules/modules'))
		for filename in filenames:
			path = os.path.join(dirpath, filename)
			with io.open(path, 'r', encoding='utf-8') as j:
				js = json.load(j)
				js = process_module_properties(js)
				name = js.get('name')
				types = js.get('type', [])
				for typ in types:
					if typ in modules:
						modules[typ].append(js)
					else:
						logging.error("The module {} has an invalid type “{}”"
							.format(name, typ))
				
		
		h.write(index.render(modules=modules))

def process_module_properties(properties):
	""" Applies Markdown to "description" and "short". Shortens "description"
	to 100 chars if "short" is not present.
	"""
	assert properties
	if 'description' in properties:
		desc = properties['description']
		properties['description'] = markdown(desc)
		if 'short' not in properties:
			properties['short'] = desc[:99].strip()+'…' if len(desc) > 100 else desc
	if 'short' in properties:
		properties['short'] = markdown(properties['short'][:100])
	return properties

# team page
def render_team():
	team = env.get_template('team.html')
	with io.open('team.html', 'w', encoding='utf-8') as h:
		h.write(team.render())

if '__main__' == __name__:
	render_index()
	render_team()
