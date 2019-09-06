#!/usr/bin/python3


import requests
from lxml import html
import sqlite3

con=sqlite3.connect('fr.sqlite')
cur=con.cursor()

r=requests.get("https://www.larousse.fr/dictionnaires/francais-anglais/bonjour/")


if r.status_code==200:
	tree=html.fromstring(r.content)
	res=tree.xpath("//span[@class='Phonetique']")
	val=str(res[1].text_content())
	print(val,type(val));
	a=cur.execute("insert into test (pron) values ('Hello')")
	b=cur.execute("insert into test (pron) values (?)",(val,))
	print(a,b)
	cur.close()
	con.commit()

print(tree)

