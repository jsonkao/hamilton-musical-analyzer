import re
from collections import defaultdict


def list_formats():
    for filename in os.listdir(os.getcwd() + '/data'):
	with open(filename) as f:
            s = f.read()
	reg = re.compile(r'\[[^\]]*\]')
	a = reg.findall(s)
	for thing in a:
		d.add(thing)
	print 'finished ' + i

def get_actors(filename):
    return
    
def parse(filename):
    with open(filename) as f:
        content = f.read()

    linesRegex = re.compile(r'\[([^\]]*)\]([^\[]*)') # speaker, line
    lines = linesRegex.findall(content)

    actorLines = defaultdict(str)
    for L in lines:
        return L
        

parse('data/alexander-hamilton.txt')

    
