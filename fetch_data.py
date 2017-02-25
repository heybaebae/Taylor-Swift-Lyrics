import urllib2
from bs4 import BeautifulSoup
import os.path

'''
fetch_data.py

This contains the code to fetch text data from the web and remove any non-text data from it. 

'''
def get_data(website_url):
	response = urllib2.urlopen(website_url)
	html = response.read()
	return html

# clean_text function takes html data and returns only viable text from the html data. 
# It returns a list of words form the webpage. 

def clean_html(html_doc):
	html_data = BeautifulSoup(html_doc,'html.parser')
	text = html_data.get_text()
	text_str = str(text)
	text_words = text_str.split()
	clean_text_words = []

	for word in text_words:
		if word.isalpha():
			clean_text_words.append(word)

	return clean_text_words

# This function cleans the text in the same manner as clean_html function, but just with
# already existing .txt files. It takes the file name as the input, which must be in
# the current directory.

def clean_file(filename):
	f = open(filename,'r+')
	text = f.read()
	text_words = text.split()
	clean_text_words = []

	for word in text_words:
		if word.isalpha():
			clean_text_words.append(word)

	clean_text = " ".join(clean_text_words)
	f.close()

	save_path = '/mnt/e/Projects/markov_chain/lyrics_clean/'
	complete_path = os.path.join(save_path, filename)
	f1 = open(complete_path,"w+")
	f1.write(clean_text)

# This function creates new text files with given lyrics. 

def create_file(lyrics,filename):
	save_path = '/mnt/e/Projects/markov_chain/lyrics_web/'
	complete_path = os.path.join(save_path, filename)

	print 'Creating a new text file...'
		
	f = open(complete_path,"w")
	f.write(lyrics)
	f.close

'''
This function fixes the grammar of the generated Markov Chain word list. It capitalizes the first
letter of the list, words like 'I', and applies grammar rules so that the word list ends on a
proper word.
'''

def grammar(lyrics_words):
	for word in lyrics_words:
		if word in 'i' == True:
			word.upper()
	lyrics_words[0] = lyrics_words[0].capitalize()
	lyrics = " ".join(lyrics_words)
	return lyrics