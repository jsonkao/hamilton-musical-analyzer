from collections import defaultdict
import re
import os

def get_actors(L):
    L = L.split(' ')
    actors = []

    men = ['hamilton','burr','lafayette','jefferson','washington','laurens','mulligan','madison']
    women = ['eliza','angelica','peggy']

    if 'all' in L:
        return
        
    while w < len(L):
        if 'all' == L[w]:
            new_ = eval(L[w+1])
            if 'except' in L:
                actors += eval(L[w+1]).remove(L.index('excerpt')+1)
                L[L.index('except')+1]
        else:
            actors.append(L[w])

def list_formats():
    d = set()
    os.chdir('data/')
    for filename in os.listdir(os.getcwd()):
        with open(filename) as f:
            s = f.read()
        reg = re.compile(r'\[([^\]]*)\]')
        a = reg.findall(s)
        for thing in a:
            d.add(thing)
    return d
            

def parse(filename):
    with open(filename) as f:
        content = f.read()

    linesRegex = re.compile(r'\[([^\]]*)\]([^\[]*)') # speaker, line
    lines = linesRegex.findall(content)

    actorLines = defaultdict(str)
    for L in lines:
        return L
        

#parse('data/alexander-hamilton.txt')

    
