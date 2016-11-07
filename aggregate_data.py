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

    fc = re.sub(r'<[^>]*>','\n',fc) # tags
    fc = re.sub(r'(\sand\s)?\([^\)]*\)','',fc) # parantheses
    fc = re.sub(u'\u2019'.encode('utf-8'),'',fc) # \u2019
    fc = re.sub(r'Lyrics HAMILTON','',fc) # removes misleading mark
    
    startRegex = re.compile(r'[A-Z][A-Z]+|[A-Z][a-z]+\ssay|I\ssaved|\[[A-Za-z\/:\s,]*\]')
    start = startRegex.search(fc).group()
    fc_s = fc.find(start)
        
    fc = fc[fc_s:fc.rfind('Read more:')]

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
    hrefs = gatherHrefs()
    
    for href in hrefs:
        writeFile(href)

if __name__ == '__main__':
    main()


    
