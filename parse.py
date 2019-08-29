#!/usr/bin/python

from lxml import html
import sys
import os
import signal
import argparse as ap


	
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
					g1=gram[0].text_content()
				if phones:
					ph=phones[1].text_content()
				if adr:
					a1=adr[0].text_content()
				print "LIEN", ph,ls,g1,"ADR:",a1

				examples=ze.xpath("..//li[@class='itemZONESEM']")
				for example in examples:
					indic=example.xpath("span[@class='Indicateur']")
					if indic:
						i1="".join([x.text_content() for x in indic])
						print "INDIC",i1
					exprs=example.xpath("div[@class='ZoneExpression1']") +  example.xpath("div[@class='ZoneExpression']")
					for expr in exprs:
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
						print "EXAMPLE", l3,l2,t2
			return tree
	



if __name__ == "__main__":
	parser = ap.ArgumentParser()
	parser.add_argument("words", nargs="*", default=['avoir'])
	parser.add_argument("--word-dir", default="words")
	parser.add_argument("--debug", action="store_true")
	args=parser.parse_args()
	print args	
	main()
