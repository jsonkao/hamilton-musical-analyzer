import urllib
import re

def main():
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical.html"
    f = urllib.urlopen(main_url).read()
    
    hrefs = re.findall(r'/h/.+lyrics.*\.html',f)

    for href in hrefs[4:5]:
        titleRegex = re.compile(r'\d{4}-.*[^\.html]') 
        title = titleRegex.search(href).group()
        
        f = urllib.urlopen(main_url+href).read()
        
        f = re.sub(r'<[^>]*>','\n', f) # deleted tags
        f = re.sub(r'(\sand\s)?\([^\)]*\)','', f) # deleted parantheses
        f = re.sub(u'\u2019'.encode('utf8'),'', f) # deleted curved apostrophes
        
        startRegex = re.compile(r'[A-Z][A-Z]+:')
        try:
            start = startRegex.search(f).group()

        except AttributeError:
            if 'King George' in f:
                startRegex = re.compile(r'\w+\ssay')
                start = startRegex.search(f).group()
            else:

        f_s = f.find(start)
        f_e = f.find('lyrics',f_s)
        f = f[f_s:f_e]
        
        """
        lyricFile = open('data/'+title+'.txt', 'w')
        lyricFile.write(f)
        lyricFile.close()
        print "wrote "+title+".txt"
"""
        
if __name__ == '__main__':
    main()
