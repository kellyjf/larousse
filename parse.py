#!/usr/bin/python

from lxml import html
import sys
import os
import signal
import argparse as ap
import requests

def getaudio(relpath):
	base="https://www.larousse.fr/"
	name=relpath.split("/")[-1]
	afile=args.audio_dir+"/"+name
	if not os.path.exists(afile):
		print "GET",base+relpath
		resp=requests.get(base+relpath)
		print "GET",resp.status_code
		if resp.status_code==200:
			with open(afile,"w") as f:
				f.write(resp.content)


	
def main():
	
	for word in args.words:
		tfile=args.word_dir+"/"+word
		if os.path.exists(tfile):
			tree=html.parse(tfile)
			zes=tree.xpath("//div[@class='ZoneEntree']")
			for ze in zes:
				ls=ph=g1=a1=None
				lienson=ze.xpath("a[@class='lienson']")
				gram=ze.xpath("div[@class='ZoneGram']")
				phones=ze.xpath("span[@class='Phonetique']")
				adr=ze.xpath("h2[@class='Adresse']")
				if lienson:
					ls=lienson[0].attrib['href']
				if gram:
					g1=gram[0].text_content().encode('utf-8')
				if phones:
					ph=phones[1].text_content().encode('utf-8')
				if adr:
					a1=adr[0].text_content().encode('utf-8')
				print "LIEN", ph,ls,g1,"ADR:",a1,"TYPE",type(ls),type(g1),type(ph),type(adr)
				if args.audio:
					getaudio(ls)

				if False:
					examples=ze.xpath("..//li[@class='itemZONESEM']")
					if not examples:
						examples=ze.xpath("..//div[@class='ZoneTexte']")

				examples=[x.getparent() for x in ze.xpath("..//span[@class='Indicateur']")]
				if not examples:
					examples=ze.xpath("..//div[@class='ZoneTexte']")
					examples=examples+ze.xpath("..//div[@class='ZoneTexte1']")

				for example in examples:
					indic=example.xpath("span[@class='Indicateur']")
					if indic:
						i1="".join([x.text_content().encode('utf-8') for x in indic])
						print "INDIC",i1
					exprs=example.xpath("div[@class='ZoneExpression1']") +  example.xpath("div[@class='ZoneExpression']")
					for expr in exprs:
						loc2=expr.xpath("span[@class='Locution2']")
						trad2=expr.xpath("span[@class='Traduction2']")
						lien3=expr.xpath("a[@class='lienson3']")
						l2=t2=l3=None
						if loc2:
							l2="".join([x.text_content().encode('utf-8') for x in loc2])
						if trad2:
							t2="".join([x.text_content().encode('utf-8') for x in trad2])
						if lien3:
							l3="".join([x.attrib['href'] for x in lien3])
						print "EXAMPLE", l3,l2,t2
						if args.audio:
							getaudio(l3)
			return tree
	



if __name__ == "__main__":
	parser = ap.ArgumentParser()
	parser.add_argument("words", nargs="*", default=['avoir'])
	parser.add_argument("--word-dir", default="words")
	parser.add_argument("--audio-dir", default="audio")
	parser.add_argument("--audio", action="store_true")
	parser.add_argument("--debug", action="store_true")
	args=parser.parse_args()
	print args	
	main()
