#!/usr/bin/python3

from lxml import html
import sys
import os
import signal
import argparse as ap
import requests
from local import get_tree

import database

_audio = False

def getaudio(relpath):
	base="https://www.larousse.fr/"
	name=relpath.split("/")[-1]
	afile=args.audio_dir+"/"+name
	if not os.path.exists(afile):
		resp=requests.get(base+relpath)
		#print("GET",resp.status_code)
		if resp.status_code==200:
			with open(afile,"wb") as f:
				for chunk in resp:
					f.write(chunk)

class Entry:
	def __init__(self, tree=None):
		self.db={}
		if tree is not None:
			self.load(tree)

	def __repr__(self):
		return ",".join("{0}:{1}".format(x.get('address'),x.get('ipa')) for x in self.zones) 

	def load(self, tree):
		self.db={}
		self.zones=[]
		zes=tree.xpath("//div[@class='ZoneEntree']")
		for ze in zes:
			zdict={ 'indics':[], 'lienson':None, 'part': None, 'ipa':None, 'address':None}
			self.zones.append(zdict)
			lienson=ze.xpath("a[@class='lienson']")
			gram=ze.xpath("div[@class='ZoneGram']")
			phones=ze.xpath("span[@class='Phonetique']")
			adr=ze.xpath("h2[@class='Adresse']")
			if lienson:
				zdict['lienson']=lienson[0].attrib['href']
			if gram:
				zdict['part']=gram[0].text_content()
			if phones:
				zdict['ipa']=phones[1].text_content()
			if adr:
				zdict['address']=adr[0].text_content()

			if _audio:
				getaudio(ls)


			examples=[x.getparent() for x in ze.xpath("..//span[@class='Indicateur']")]
			if not examples:
				examples=ze.xpath("..//div[@class='ZoneTexte']")
				examples=examples+ze.xpath("..//div[@class='ZoneTexte1']")

			for example in examples:
				edict={ 'expressions':[] }
				zdict['indics'].append(edict)
				indic=example.xpath("span[@class='Indicateur']")
				if indic:
					i1="".join([x.text_content() for x in indic])
					edict['indic']=i1
				exprs=example.xpath("div[@class='ZoneExpression1']") +  example.xpath("div[@class='ZoneExpression']")
				for expr in exprs:
					xdict={}
					loc2=expr.xpath("span[@class='Locution2']")
					trad2=expr.xpath("span[@class='Traduction2']")
					lien3=expr.xpath("a[@class='lienson3']")
					l2=t2=l3=None
					if loc2:
						l2="".join([x.text_content() for x in loc2])
					if trad2:
						t2="".join([x.text_content() for x in trad2])
					if lien3:
						l3="".join([x.attrib['href'] for x in lien3])
					xdict['locution']=l2
					xdict['traduction']=t2
					xdict['lienson']=l3
					edict['expressions'].append(xdict)

					#print "EXAMPLE", l3,l2,t2
					if _audio:
						getaudio(l3)
		
if __name__ == "__main__":
	parser = ap.ArgumentParser()
	parser.add_argument("words", nargs="*", default=['avoir'])
	parser.add_argument("--word-dir", default="words")
	parser.add_argument("--audio-dir", default="audio")
	parser.add_argument("--audio", action="store_true")
	parser.add_argument("--debug", action="store_true")
	args=parser.parse_args()

	for d in [ args.audio_dir, args.word_dir ]:
		if not os.path.exists(d):
			os.makedirs(d)

	database.create()
	asess=database.Session()
	qsess=database.Session()

	for word in args.words:
		if asess.query(database.Root.root).filter(database.Root.root==word).first():
			continue
		tree=get_tree(word)
		e=Entry(tree)
		root=database.Root(root=word)
		asess.add(root)
		for zone in e.zones:
			print("{0} {1} {2}".format(zone.get('address'), zone.get('ipa'),zone.get('part')))
			usage=database.Usage(address=zone.get('address'),
					lienson=zone.get('lienson'),
					phonetic=zone.get('ipa'),
					grammar=zone.get('part'), 
					root=root)
			asess.add(usage)
			if args.audio and zone.get('lienson'):
				getaudio(zone.get('lienson'))
			for indic in zone.get('indics'):
				mean=database.Meaning(meaning=indic.get('indic'), usage=usage)
				asess.add(mean)
				print("\t",indic.get('indic'))
				for expr in indic.get('expressions'):
					exam=database.Example(meaning=mean, 
						expression=expr.get('locution'),
						translation=expr.get('traduction'),
						lienson=expr.get('lienson')
						)
					asess.add(exam)
					if args.audio and expr.get('lienson'):
						getaudio(expr.get('lienson'))
					print("\t\t",expr.get('locution'))
		asess.commit()
