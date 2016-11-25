import urllib
import re

def loadLinks():
    HTML = urllib.urlopen('http://atlanticrecords.com/HamiltonMusic/').read()
    
    # returns a list of (href,title)
    linkRegex = re.compile(r'<a href="([^"]*)"\sdata-ref="[^"]*">([^<]*)')
    L = linkRegex.findall(HTML)

    
