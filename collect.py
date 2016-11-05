import urllib
import re
omg = '3704-my-shot-lyrics-hamilton.html'
def writeFile(href):
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical-lyrics/"

    titleRegex = re.compile(r'\d{4}-.*[^\.html]')
    title = titleRegex.search(href).group()

    f = urllib.urlopen(main_url + href).read()

    f = re.sub(r'<[^>]*>','\n',f) # tags
    f = re.sub(r'(\sand\s)?\([^\)]*\)','',f) # parantheses
    f = re.sub(u'\u2019'.encode('utf-8'),'',f)
    
    startRegex = re.compile(r'[A-Z][A-Z]+|[A-Z][a-z]+\ssay|I\ssaved|\[[A-Za-z\/:\s,]*\]')
    start = startRegex.search(f).group()
    f = f[f.find(start):f.rfind('Read more:')]

    return [title, f]

def gatherHrefs():
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical.html"
    f = urllib.urlopen(main_url).read()
    hrefs = re.findall(r'\d{4}[a-z\-]+\.html',f)
    return hrefs

def main():
    hrefs = gatherHrefs()
    for href in hrefs:
        
        fileContent = write(href)
        f = open('data/'+fileContent[0]+'.txt','w')
        f.write(fileContent[1])
        f.close()

        
        #3665-electionof1800, 3669-burn, 3677-cabinetbattle, 3682-catbinet battle
faulty=['3665-election-of-1800-lyrics-hamilton.html',
        '3677-cabinet-battle-2-lyrics-hamilton.html',
        '3682-cabinet-battle-1-lyrics.html',
        '3669-burn-lyrics-hamilton-the-musica',
        '3702-the-schuyler-sisters-lyrics',
        '3704-my-shot-lyrics-hamilton.html'
        
        ]


def makeup(n):
    fileContent = writeFile(faulty[n])
    f = open('data/'+fileContent[0]+'.txt','w')
    f.write(fileContent[1])
    d=open('data/'+fileContent[0]+'.txt','rU').read()[:50]
    f.close()
