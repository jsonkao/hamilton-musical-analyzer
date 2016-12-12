from collections import defaultdict
import re
import os

def get_actors(L):
    L = L.split(' ')
    actors = []

    men = ['hamilton','burr','lafayette','jefferson','washington','laurens','mulligan','madison']
    women = ['eliza','angelica','peggy']

    if 'all' in L:
        index = L.index('all')
        actors = L[:index]
        new_ = eval(L[index+1])
        if 'except' in L[index:]:
            new_.remove(L[L.index('except')+1])
        actors += new_
    elif 'voter' in L or 'voters' in L:
        actors = ['voters']
    #elif 'women' in L or 'woman' in L:
    else:
        actors = L

    blank = ['ensemble']
    for w in blank:
        if w in actors:
            actors.remove(w)

    return actors

def list_formats(L):
    if 'data' not in os.getcwd():
        os.chdir('data/')
    isEmpty = not L
    d = set()
    for filename in os.listdir(os.getcwd()):
        with open(filename) as f:
            s = f.read()
        reg = re.compile(r'\[([^\]]*)\]')
        a = reg.findall(s)
        for thing in a:
            addMe = False
            for l in L:
                if l in thing:
                    addMe = True
                    break
            if addMe or isEmpty:
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
        
print list_formats([])
