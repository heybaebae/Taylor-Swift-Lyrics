import urllib2
import glob, os
from random import randint
from bs4 import BeautifulSoup
from markov_python.cc_markov import MarkovChain
from fetch_data import clean_file
from fetch_data import clean_html
from fetch_data import get_data
from fetch_data import create_file
from fetch_data import grammar

'''
run. py

This file includes the code that ties the flow of the application tjazz blues backing trackogether. 
'''

# Websites with song lyrics
songs = [	'http://www.azlyrics.com/lyrics/taylorswift/22.html',
			'http://www.azlyrics.com/lyrics/taylorswift/badblood.html',
			'http://www.azlyrics.com/lyrics/taylorswift/blankspace.html',
			'http://www.azlyrics.com/lyrics/zaynmalik/idontwannaliveforever.html',
			'http://www.azlyrics.com/lyrics/taylorswift/iknewyouweretrouble.html',
			#'http://www.azlyrics.com/lyrics/taylorswift/lovestory.html',
			'http://www.azlyrics.com/lyrics/taylorswift/shakeitoff.html',
			'http://www.azlyrics.com/lyrics/taylorswift/weareneverevergettingbacktogether.html',
			'http://www.azlyrics.com/lyrics/taylorswift/youbelongwithme.html'
		]

for web in songs:
	data = get_data(web)
	print web
	text_words = clean_html(data)
	text = ' '.join(text_words)
	filename = web[43:-5]
	print filename
	create_file(text,filename)

# Clean text in the manually created text files
os.chdir("/mnt/e/Projects/markov_chain/lyrics")
for file in glob.glob("*.txt"):
	clean_file(file)

# Call the MarkovChain function
mc = MarkovChain()
os.chdir("/mnt/e/Projects/markov_chain/lyrics_clean")
for file in glob.glob("*.txt"):				#finds all ".txt" files and adds to MarkovChain 
	mc.add_file(file)

# Generate the Markov Chain and format in proper grammar
l_length = randint(5,20)
TS_words = mc.generate_text(l_length)
TS_lyrics = grammar(TS_words)

# Prints out the final result
print TS_lyrics



