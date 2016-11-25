import urllib
import re

def loadLinks():
    HTML = urllib.urlopen('http://atlanticrecords.com/HamiltonMusic/').read()
    HTML = HTML[HTML.rfind('<ul class="lyrics'):HTML.rfind('<div class="bottom')]
    # returns a list of (href,title)
    linkRegex = re.compile(r'<a href="([^"]*)"\sdata-ref="[^"]*">([^<]*)')
    L = linkRegex.findall(HTML)
    return L
    
