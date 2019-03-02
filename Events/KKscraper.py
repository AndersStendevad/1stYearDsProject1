import requests
from bs4 import BeautifulSoup
import re

def collect_links(filename):
	links = []
	with open(filename) as file:
		for line in file:
			page = requests.get(line.strip())
			soup = BeautifulSoup(page.content, 'html.parser')
			for i in soup.find_all('a'):
				if 'Læs mere om arrangementet' in i:
					links.append(i.get('href'))

	return links

def events_des(list_of_events):
	description = []
	for event in list_of_events:
		page = requests.get(event)
		soup = BeautifulSoup(page.content, 'html.parser')
		for paragraph in soup.find_all('p'):
			description.append(paragraph.text)
		description.append('\n')
		
	return description

Places = ['Indre_by', 'Amager', 'Norrebro', 'Ostebro', 'Valby', 'Vestebro']	

for place in Places:
	Links_to_events = collect_links(place+'.txt')
	text = events_des(Links_to_events)
	log = open(place+'_clean.txt', 'w')
	lines_no_special = [re.sub('[^a-zåøæ]', ' ', line.lower()) for line in text]
	lines_one_space = [re.sub(' +', ' ', line) for line in lines_no_special]
	for line in lines_one_space:
		log.write(line)

log.close()