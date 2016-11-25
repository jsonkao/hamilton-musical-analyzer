import urllib
import re

def h():

    # loads HTML
    root_url = 'http://atlanticrecords.com/HamiltonMusic/'
    HTML = urllib.urlopen(root_url).read()
    HTML = HTML[HTML.find('<ul class="lyrics'):HTML.find('<div class="bottom')]
    
    # returns a list of (href,title)
    linkRegex = re.compile(r'<a href="([^"]*)"\sdata-ref="[^"]*">([^<]*)')
    links = linkRegex.findall(HTML)
    return links
    for i in range(0,len(links)):
        href = links[i][0]
        title = links[i][1].replace(' ','_')

        f = urllib.urlopen(root_url + href).read()
        f = f[f.find('<div class="rg_embed_body'):f.find('<div class="rg_embed_footer')]
        print len(f)
        f = re.sub(r'<[^>]*>','',f)
        return f
        
