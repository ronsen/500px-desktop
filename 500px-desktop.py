#!/usr/bin/env python

import feedparser
from BeautifulSoup import BeautifulSoup
import urllib2
import commands
from random import randint
import sys

feeds = []
feeds.append('http://feed.500px.com/500px-best')
feeds.append('http://feed.500px.com/500px-editors')
feeds.append('http://feed.500px.com/500px-upcoming')
feeds.append('http://feed.500px.com/500px-fresh')

DOWNLOAD_PATH = '/home/ronsen/pictures/' # change this

def get_random_image():
	feed = feedparser.parse(feeds[randint(0, len(feeds) - 1)])
	images = []
	for entry in feed.entries:
		content = BeautifulSoup(entry.description)
		images.append(content.find('img')['src'])
		
	return images[randint(0, len(images) - 1)]

def download_image(image):
	path = DOWNLOAD_PATH + image.split('/')[-1] + '.jpg'

	f = urllib2.urlopen(image)
	data = f.read()
	with open(path, "wb") as code:
		code.write(data)

	return path

def set_as_background(path):
	command = "gsettings set org.gnome.desktop.background picture-uri file://" + path
	status, output = commands.getstatusoutput(command)
	return status

if __name__ == "__main__":
	try:
		image = get_random_image()
		path = download_image(image)
		set_as_background(path)
	except Exception, e:
		print e
		sys.exit(1)
