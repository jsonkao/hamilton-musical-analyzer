import re
from collections import defaultdict

def find_actors(filename):
    
    
def parse(filename):
    with open(filename) as f:
        content = f.read()

    linesRegex = re.compile(r'\[([^\]]*)\]([^\[]*)') # speaker, line
    lines = linesRegex.findall(content)

    actorLines = defaultdict(str)
    for L in lines:
        return L
        

parse('data/alexander-hamilton.txt')

    
