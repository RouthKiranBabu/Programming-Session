from requests_html import HTML,HTMLSession
import csv
##is used to find id
'''
with open('index.html') as html_file:
	source=html_file.read()
	html=HTML(html=source)

#prints the index.html
print(html.html)

#to know url
print(html)
print()

#to see the result of index file
print(html.text)

#to find the title
print("the title of the index")
match=html.find('title')
print(match)

match=html.find('title')
print("the match in html format")
print(match[0].html)

match=html.find('title')
print("to print text")
print(match[0].text)

#matches the first element found
match=html.find('title',first=True)
print("to print text")
print(match.text)


match=html.find('#footer',first=True)
print("to find the footer id")
print(match.text)

article=html.find('div.article',first=True)
print("to print the the text inside div tag and article class")
print(article.text)

article=html.find('div.article',first=True)
print('get headline and summary individually')
headline=article.find('h2',first=True)
summary=article.find('p',first=True)
print(headline.text)
print(summary.text)

article=html.find('div.article',first=True)
print('get headline and summary individually')
headline=article.find('h2',first=True).text
summary=article.find('p',first=True).text
print(headline)
print(summary)

articles=html.find('div.article')
for article in articles:
	print('get headline and summary individually and finding all articles')
	headline=article.find('h2',first=True).text
	summary=article.find('p',first=True).text
	print(headline)
	print(summary)
'''
'''
session=HTMLSession()
#r is response object
r=session.get('https://coreyms.com/')
#finds url
print(r.html)
#output: <HTML url='https://coreyms.com/'>

article=r.html.find('article',first=True)
print(article)
#output:
#<Element 'article' class=('post-1642', 'post', 'type-post',
# 'status-publish', 'format-standard', 'has-post-thumbnail',
#  'category-development', 'category-python',
 #  'tag-development-environment', 'tag-visual-studio-code',
 #   'tag-visual-studios', 'tag-vs-code', 'tag-vscode', 'entry')
 #    itemscope='' itemtype='https://schema.org/CreativeWork'>
print()
article=r.html.find('article',first=True)
print(article.html)
#output:
#<article class="post-1642 post type-post status-publish format-standard has-post-thumbnail category-development category-python tag-development-environment tag-visual-studio-code tag-visual-studios tag-vs-code tag-vscode entry" itemscope="" itemtype="https://schema.org/CreativeWork"><header class="entry-header"><h2 class="entry-title" itemprop="headline"><a class="entry-title-link" href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview" rel="bookmark">Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview</a></h2>
#<p class="entry-meta"><time class="entry-time" datetime="2019-05-01T14:03:24+00:00" itemprop="datePublished">May 1, 2019</time> by <span class="entry-author" itemprop="author" itemscope="" itemtype="https://schema.org/Person"><a class="entry-author-link" href="https://coreyms.com/author/coreymschafer" itemprop="url" rel="author"><span class="entry-author-name" itemprop="name">Corey Schafer</span></a></span> <span class="entry-comments-link"><a href="https://coreyms.com/development/python/visual-studio-code-windows-setting-up-a-python-development-environment-and-complete-overview#respond"><span class="dsq-postid" data-dsqidentifier="1642 http://coreyms.com/?p=1642">Leave a Comment</span></a></span> </p></header><div class="entry-content" itemprop="text">
#<p>In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…</p>
#<p>VSCode on MacOS – https://youtu.be/06I63_p-2A4</p>
#<p>Timestamps for topics in this tutorial:<br/> Installation – 1:13<br/> Python Extension – 5:48<br/> Switching Interpreters – 10:04<br/> Changing Color Themes – 12:35<br/> VSCode Settings – 16:16<br/> Set Default Python – 21:33<br/> Using Virtual Environments – 25:10<br/> IntelliSense – 29:45<br/> Code Formatting – 32:13<br/> Code Linting – 37:06<br/> Code Runner Extension – 39:42<br/> Git Integration – 47:44<br/> Use Different Terminal – 51:07<br/> Debugging – 58:45<br/> Unit Testing – 1:03:25<br/> Zen Mode – 1:09:55</p>
#<figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
#<span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"/></span>
#</div></figure>
#</div><footer class="entry-footer"><p class="entry-meta"><span class="entry-categories">Filed Under: <a href="https://coreyms.com/category/development" rel="category tag">Development</a>, <a href="https://coreyms.com/category/development/python" rel="category tag">Python</a></span> <span class="entry-tags">Tagged With: <a href="https://coreyms.com/tag/development-environment" rel="tag">Development Environment</a>, <a href="https://coreyms.com/tag/visual-studio-code" rel="tag">visual studio code</a>, <a href="https://coreyms.com/tag/visual-studios" rel="tag">visual studios</a>, <a href="https://coreyms.com/tag/vs-code" rel="tag">vs code</a>, <a href="https://coreyms.com/tag/vscode" rel="tag">vscode</a></span></p></footer></article>

session=HTMLSession()
r=session.get('https://coreyms.com/')
#to know for success
print(r)
'''
'''
session=HTMLSession()
r=session.get('https://coreyms.com/')
article=r.html.find('article',first=True)
headline=article.find('.entry-title-link',first=True).text
print(headline)
#output:
#Visual Studio Code (Windows) – Setting up a Python Development Environment and Complete Overview
summary=article.find('.entry-content p',first=True).text
print(summary)
#output:
#In this Python Programming Tutorial, we will be learning how to set up a Python development environment in VSCode on Windows. VSCode is a very nice free editor for writing Python applications and many developers are now switching over to this editor. In this video, we will learn how to install VSCode, get the Python extension installed, how to change Python interpreters, create virtual environments, format/lint our code, how to use Git within VSCode, how to debug our programs, how unit testing works, and more. We have a lot to cover, so let’s go ahead and get started…

vid_src=article.find('iframe',first=True)
print(vid_src.html)
#output:
#<iframe allowfullscreen="true" class="youtube-player" height="360" src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"/>
#src="https://www.youtube.com/embed/-nh9rCzPJ20?version=3&amp where nh9rCzPJ20 is id of the utube vedio

vid_src=article.find('iframe',first=True)
print(vid_src.attrs)
#output
#{'allowfullscreen': 'true', 'class': ('youtube-player',), 'height': '360', 'src': 'https://www.youtube.com/embed/-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent', 'style': 'border:0;', 'type': 'text/html', 'width': '640'}

vid_src=article.find('iframe',first=True)
print(vid_src.attrs['src'])
#shows the entire url of vedio
#https://www.youtube.com/embed/-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

vid_src=article.find('iframe',first=True).attrs['src']
vid_id=vid_src.split('/')
print(vid_id)
#output
#['https:', '', 'www.youtube.com', 'embed', '-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent']

vid_src=article.find('iframe',first=True).attrs['src']
vid_id=vid_src.split('/')[4]
print(vid_id)
#output
#-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

vid_src=article.find('iframe',first=True).attrs['src']
vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]
print(vid_id)
#to get id of you tube vedio
#output
#-nh9rCzPJ20

youtubeLink=f"https://youtube.com/watch?v={vid_id}"
print(youtubeLink)#copy that and paste in web to see that works

session=HTMLSession()
r=session.get('https://coreyms.com/')
articles=r.html.find('article')
for article in articles:
	#you can print headline and summary
	headline=article.find('.entry-title-link',first=True).text
	summary=article.find('.entry-content p',first=True).text
	vid_src=article.find('iframe',first=True).attrs['src']
	vid_id=vid_src.split('/')[4]
	vid_id=vid_id.split('?')[0]
	youtubeLink=f"https://youtube.com/watch?v={vid_id}"
	print(youtubeLink)
	print()
#output
#https://youtube.com/watch?v=-nh9rCzPJ20

#https://youtube.com/watch?v=06I63_p-2A4

#https://youtube.com/watch?v=_JGmemuINww

#https://youtube.com/watch?v=zdJEYhA2AZQ

#https://youtube.com/watch?v=kIdiWut8eD8

#https://youtube.com/watch?v=1lxrb_ezP-g

#https://youtube.com/watch?v=SELYgZvAZbU

#https://youtube.com/watch?v=APOPm01BVrk

#https://youtube.com/watch?v=Kg1Yvry_Ydk

#https://youtube.com/watch?v=C-gEQdGVXbk
'''
'''
csv_file=open('cms_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video'])

session=HTMLSession()
r=session.get('https://coreyms.com/')
articles=r.html.find('article')
for article in articles:
	headline=article.find('.entry-title-link',first=True).text
	summary=article.find('.entry-content p',first=True).text
	vid_src=article.find('iframe',first=True).attrs['src']
	vid_id=vid_src.split('/')[4]
	vid_id=vid_id.split('?')[0]
	youtubeLink=f"https://youtube.com/watch?v={vid_id}"
	print(youtubeLink)
	print()
	csv_writer.writerow([headline,summary,youtubeLink])
csv_file.close()
'''
'''
#to get all the links
session=HTMLSession()
r=session.get('https://coreyms.com/')
for link in r.html.links:
	print(link)
#output
#https://coreyms.com/development/python/10-python-tips-and-tricks-for-writing-better-code#respond
#https://coreyms.com/category/development/git
#https://coreyms.com/category/diy/home-improvement
#https://coreyms.com/giveaway
#https://github.com/CoreyMSchafer
#http://talkpython.fm/
#http://shoptalkshow.com/
#https://coreyms.com/tag/enumerate
#https://coreyms.com/tag/virtualenv
#https://coreyms.com/tag/ternary-operator
#http://coreyms.com/portfolio
#https://coreyms.com/support 
#and so on

for link in r.html.absolute_links:
	print(link)
'''
'''
with open('index.html') as html_file:
	source=html_file.read()
	html=HTML(html=source)
match=html.find('#footer',first=True)
print(match.html)
#output
#<div id="footer">
#<p>Footer Information</p>
#</div>
import time
with open('index.html') as html_file:
	source=html_file.read()
	html=HTML(html=source)
	#downloads a file
	html.render()
match=html.find('#footer',first=True)
print(match.html)
'''
'''
#synchronus timing requests
import time 	
from requests_html import HTMLSession
session=HTMLSession()
t1=time.perf_counter()

r=session.get('https://httpbin.org/delay/1')
response=r.html.url
print(response)

r=session.get('https://httpbin.org/delay/2')
response=r.html.url
print(response)

r=session.get('https://httpbin.org/delay/3')
response=r.html.url
print(response)

t2=time.perf_counter()

print(f"Synchronous: {t2-t1} seconds.")
#output
#https://httpbin.org/delay/1
#https://httpbin.org/delay/2
#https://httpbin.org/delay/3
#Synchronous: 8.535399884057972 seconds.
'''

import time
from requests_html import AsyncHTMLSession
asession=AsyncHTMLSession()

async def get_delay1():
	r=await asession.get('https://httpbin.org/delay/1')
	return r

async def get_delay2():
	r=await asession.get('https://httpbin.org/delay/2')
	return r

async def get_delay3():
	r=await asession.get('https://httpbin.org/delay/3')
	return r

t1=time.perf_counter()
#runs parallel not like sync that proceed for run when previous run is done
results=asession.run(get_delay1,get_delay2,get_delay3)

for result in results:
	response=result.html.url
	print(response)

t2=time.perf_counter()

print(f"Asynchronous: {t2-t1} seconds.")
#output:
#https://httpbin.org/delay/2
#https://httpbin.org/delay/1
#https://httpbin.org/delay/3
#Asynchronous: 5.1695177584541065 seconds.

session=HTMLSession()

r=session.get("https://www.google.com/search?source=hp&ei=kI8JXamCFsj-9QOm07rwCg&q=temperature+today&oq=temp&gs_l=psy-ab.3.1.0j0i131j0l5j0i131j0l2.97021.110809..113573...17.0..0.417.6469.1j0j19j3j1......0....1..gws-wiz.....0..0i10.uCzGIJxN0T4")
print(r.html)
val=r.html.find("#wob_d > div > div:nth-child(2)",first=True)#copy the copy selector from inspect
print(val.text)