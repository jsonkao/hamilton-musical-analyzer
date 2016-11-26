import urllib
import urllib2
import cookielib
import re
import requests

def main():

    # loads links
    HTML = urllib.urlopen('http://atlanticrecords.com/HamiltonMusic/').read()
    HTML = HTML[HTML.find('<ul class="lyrics'):HTML.rfind('<div class="bottom')]
    linkRegex = re.compile(r'<a href="[^=]*=(\d+)')
    EMBED_ID = linkRegex.findall(HTML)
    
    for x in EMBED_ID:
        h = requests.get('http://genius.com/songs/'+x).url # returns redirect address
        title = h[h.rfind('miranda-')+len('miranda-'):h.rfind('-lyrics')]

        # User-Agent change due to genius.com 403
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        req = urllib2.Request(h,headers=hdr)
        HTML = urllib2.urlopen(req).read()
        lyrics = HTML[HTML.find('<lyrics'):HTML.find('</lyrics')]

        # cleans up content
        lyrics = re.sub(r'<[^>]*>',' ',lyrics) # removes tags
        lyrics = re.sub(r'[^\w\[\]\s\/]','',lyrics) # removes bad chars
        lyrics = re.sub(r'\s{2,}',' ',lyrics) # trims spaces
        lyrics = lyrics.replace('\n','').replace('/',' ').replace('amp ','')
        lyrics = lyrics[lyrics.find('['):].lower() # removes stage directions

        # writes file
        f = open('data/'+title+'.txt','w')
        f.write(lyrics)
        f.close()
        print 'wrote data/'+title+'.txt'

if __name__ == '__main__':
    main()
