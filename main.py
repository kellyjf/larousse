#!/usr/bin/python

import requests
from lxml import html
import sys
import os
import signal
import argparse as ap

base="https://www.larousse.fr/dictionnaires/francais-anglais/"

def main():
	
	print args.words
	for word in args.words:
		tfile=args.word_dir+"/"+word
		if not os.path.exists(tfile):
			pg=requests.get(base+word+"/")
			with open(tfile,"w") as f:
				f.write(pg.text.encode('utf-8'))
			

if __name__ == "__main__":

	parser = ap.ArgumentParser()
	parser.add_argument("words", nargs="*")
	parser.add_argument("--word-dir", default="words")
	parser.add_argument("--debug", action="store_true")
	args=parser.parse_args()

	main()
	
