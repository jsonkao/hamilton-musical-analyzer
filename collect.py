# coding=utf-8

import urllib
import re

def writeFile(href):
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical-lyrics"

    titleRegex = re.compile(r'\/\d{4}-.*[^\.html]')
    title = titleRegex.search(href).group()

    if int(title[1:5]) > 3706 or int(title[1:5]) < 3661:
        print "rejected " + title + ".txt"
        return None

    fc = urllib.urlopen(main_url + href).read()
    fc = fc[fc.find("Hamilton the Musical - "):]

    fc = re.sub(r'<[^>]*>', '\n', fc)  # tags
    fc = re.sub(r'(\sand\s)?\([^\)]*\)', '', fc)  # parantheses

    encoding_faults = [u'\u00AE', u'\u0308', u'\u00F2', u'\u2014', u'\u2018', u'\u2019', u'\u2026']
    for o in encoding_faults:
        fc = fc.replace(o.encode('utf-8'), '')

    fc = fc.replace('/'," AND ")
    fc = fc.replace('&amp;',"AND")

    for c in ':—-!",?.\xe2\x80\x9c\x9d\r':
        fc = fc.replace(c, '')

    startRegex = re.compile(r'[A-Z]{2,}|[A-Z][a-z]+\ssay|I\ssaved|\[[A-Za-z\/:\s,]*\]')
    start = startRegex.search(fc).group()
    fc_s = fc.find(start)

    fc = fc[fc_s:fc.rfind('Read more')]


    f = open('data/' + title + '.txt','w')
    f.write(fc)
    f.close()

    print "wrote " + title + ".txt"

def gatherHrefs():
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical.html"
    f = urllib.urlopen(main_url).read()
    hrefs = re.findall(r'\/\d{4}[a-z\-0-9]+\.html',f)

    return hrefs

def main():
    hrefs = gatherHrefs()[-30:-20]
    
    for href in hrefs:
        writeFile(href)

if __name__ == '__main__':
    main()
