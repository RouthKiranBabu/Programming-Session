from bs4 import BeautifulSoup
import requests

with open("simple.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)
#Output
#<!DOCTYPE html>
#<html class="no-js" lang="">
#<head>
#<title>Test - A Sample Website</title>
#<meta charset="utf-8"/>
#<link href="css/normalize.css" rel="stylesheet"/>
#<link href="css/main.css" rel="stylesheet"/>
#</head>
#<body>
#...

#Gives clear or clarity pattern to understand
print(soup.prettify())
#Output
#<!DOCTYPE html>
#<html class="no-js" lang="">
# <head>
#  <title>
#   Test - A Sample Website
#  </title>
#  <meta charset="utf-8"/>
#  <link href="css/normalize.css" rel="stylesheet"/>
#  <link href="css/main.css" rel="stylesheet"/>
# </head>
# <body>
#  <h1 id="site_title">

#To find the text of title
print(soup.title.text)
#Output
#Test - A Sample Website

print(soup.div)
#Output
#<div class="article">
#<h2><a href="article_1.html">Article 1 Headline</a></h2>
#<p>This is a summary of article 1</p>
#</div>

article = soup.find('div', class_ = 'article')
print(article)
#Output
#<div class="article">
#<h2><a href="article_1.html">Article 1 Headline</a></h2>
#<p>This is a summary of article 1</p>
#</div>

print(article.h2.a.text)
#Output
#Article 1 Headline

summary = article.p.text 
print(summary)
#Output
#This is a summary of article 1

for article in soup.find_all('div', class_ = 'article'):
    print(article.h2.a.text)
    print(article.p.text)
#Output
#Article 1 Headline
#This is a summary of article 1
#Article 2 Headline
#This is a summary of article 2