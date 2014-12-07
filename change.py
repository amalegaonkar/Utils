#!/usr/bin/python
from bs4 import BeautifulSoup as Soup
from bs4 import BeautifulSoup, Tag, NavigableString, Comment, Declaration



import sys
reload(sys)
sys.setdefaultencoding('utf-8')


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

program_name = sys.argv[0]
arguments = sys.argv[1:]

f = open(arguments[0],'rw+')
temp = f.read()
temp = temp.replace('\r\n', '\n')
soup = Soup(temp)
#soup.insert(0, "<!DOCTYPE html>")
soup.prettify(encoding='UTF-8')

#soup.insert(0, Declaration("DOCTYPE"))

meta = soup.new_tag('meta')
meta['name'] = "viewport"
meta['content'] = "width=device-width, initial-scale=1"
head = soup.find('head')
head.insert(1, meta)
f.close()
newfile = arguments[1] + "/"+arguments[0]
f = open(newfile, 'w')
f.write (soup.prettify())
f.close()


#f = open(arguments[0], 'w')
#f.write("<!DOCTYPE html>\n")
#
#f.write(temp)
#f.close()
