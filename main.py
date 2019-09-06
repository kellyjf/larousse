#!/usr/bin/python3

import requests
from lxml import html
import sys
import os
import signal
import argparse as ap

base="https://www.larousse.fr/dictionnaires/francais-anglais/"

def get_tree(word):
	tree=None
	tfile=args.word_dir+"/"+word
	if not os.path.exists(tfile):
		pg=requests.get(base+word+"/")
		if pg.status_code==200:
			with open(tfile,"w") as f:
				f.write(pg.text)
	with open(tfile,"r") as f:
		tree=html.fromstring(f.read())

	return tree

def main():
	
	print(args.words)
	for word in args.words:
		print(get_tree(word))

if __name__ == "__main__":

	parser = ap.ArgumentParser()
	parser.add_argument("words", nargs="*")
	parser.add_argument("--word-dir", default="words")
	parser.add_argument("--debug", action="store_true")
	args=parser.parse_args()

	if not os.path.exists(args.word_dir):
		os.makedirs(args.word_dir)
	main()
	
