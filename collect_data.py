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
    song_list = HTML[HTML.find('<ul class="song_list'):HTML.rfind('<div class="back_to_albums')]
 
    hrefRegex = re.compile(r'<a href="([^"]*)')
    hrefs = hrefRegex.findall(song_list)
    for h in hrefs:
        title = h[h.rfind('miranda-')+len('miranda-'):h.rfind('-lyrics')]
        print title
        """
        req = urllib2.Request(h,headers=hdr)
        HTML = urllib2.urlopen(req).read()
        lyrics = HTML[HTML.find('<lyrics'):HTML.find('</lyrics')]

        lyrics = re.sub(r'<[^>]*>',' ',lyrics) # removes tags
        lyrics = re.sub(r'[^\w\[\]\s]||\samp','',lyrics) # removes bad chars
        lyrics = re.sub(r'\s{2,}',' ',lyrics) # trims spaces
        lyrics = lyrics.replace('\n','')
        lyrics = lyrics[lyrics.find('['):].lower() # removes stage directions"""

 #       f = open('data/'+title+'.txt')
print h()
