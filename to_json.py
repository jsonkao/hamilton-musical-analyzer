"""
1. split into lines
2. for each line, check if there's speaker
3. use defaultdict(list) to add on sentences
4. return dicitionary with lists of each singer, convert to json
"""
import re
import os
from collections import defaultdict

os.chdir('data/')

tests = [
    '3706-alexander-hamilton-lyrics.txt',
    '3705-aaron-burr-sir-lyrics.txt',
    '3704-my-shot-lyrics-hamilton.txt',
    '3703-the-story-of-tonight-lyrics.txt'
    ]


def presentActors(line):
    actorRegex = re.compile(r'[A-Z]{3,}')
    actors = actorRegex.findall(line)

    fake = ["ENSEMBLE", "COMPANY", "AND"]
    for s in fake:
        if s in actors: actors.remove(s)
    return actors if actors else None

def main(filename):
    
    with open(filename) as f:
        script = f.read().split("\n")

    # splits script into actors' lines
    size = len(script)
    i = 1

    while i < size:
        if not (script[i][:3].isupper()):
            script[i - 1] += " " + script.pop(i)
            size -= 1
        else:
            i += 1
    f = open('test.txt','w')
    f.write(str(script))
    f.close()
    data = defaultdict(list)
    for line in script:
        actors = presentActors(line)
        if actors is not None:
            lastIndex = line.find(actors[-1]) + len(actors[-1])

            try:
                if "]" in line[lastIndex]: lastIndex += 2
            except IndexError: # occurs when lines blank (parantheses text)
                continue

            for actor in actors:
                data[actor].append(line[lastIndex:].strip())
    for key in data:
        data[key] = ' '.join(data[key])
    return data

d = main(tests[0])
print d.keys()

def drive():
    files = os.listdir(os.curdir)
    print main(files[3]) #3706

