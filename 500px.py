#!/usr/bin/env python

import feedparser
from BeautifulSoup import BeautifulSoup
import urllib2
import commands
from random import randint
import sys

URL = 'http://feed.500px.com/500px-best'

DOWNLOAD_PATH = '/home/ronsen/pictures/' # change this

def get_random_image():
	feed = feedparser.parse(URL)
	images = []
	for entry in feed.entries:
		content = BeautifulSoup(entry.description)
		images.append(content.find('img')['src'])
		
	return images[randint(0, len(images) - 1)]

def download_image(image, path):
	f = urllib2.urlopen(image)
	
	data = f.read()
	with open(path, "wb") as code:
		code.write(data)

def set_as_background(path):
	command = "gsettings set org.gnome.desktop.background picture-uri file://" + path
	status, output = commands.getstatusoutput(command)
	return status

if __name__ == "__main__":
	try:
		image = get_random_image()
		path = DOWNLOAD_PATH + image.split('/')[-1] + '.jpg'
		
		download_image(image, path)
		set_as_background(path)
	except Exception, e:
		print e
		sys.exit(1)
