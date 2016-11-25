import urllib2
import cookielib
import re

def h():
    
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    req = urllib2.Request('http://genius.com/albums/Lin-manuel-miranda/Hamilton-original-broadway-cast-recording',headers=hdr)
    HTML = urllib2.urlopen(req).read()
    HTML = HTML[HTML.find('<ul class="song_list'):HTML.rfind('<div class="back_to_albums')]
 
    hrefRegex = re.compile(r'<a href="([^"]*)')
    hrefs = hrefRegex.findall(HTML)

    for h in hrefs:
        req = urllib2.Request(h,headers=hdr)
        song_HTML = urllib2.urlopen(req).read()
        return song_HTML
