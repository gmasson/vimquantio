#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Conexão MySQL
# import pymysql
# import sqlite3
# conn = sqlite3.connect('database.db')
# database = conn.cursor()

import urllib2

# URL para ser minerada
website = "http://gmasson.com.br/"

link = urllib2.urlopen(website).read()

# Mineração ignorando parametros da tag
tag_title = link.split('<title')[1:]
tag_title = [ tag.split('</title>')[0].split('>',1)[1] for tag in tag_title ]

print("<title> ---------------------")

# aqui é para salvar no banco de dados
for i in tag_title:
  print i

