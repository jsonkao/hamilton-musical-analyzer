# coding=utf-8

import urllib
import re

hrefs = ['/3706-alexander-hamilton-lyrics.html', '/3705-aaron-burr-sir-lyrics.html', '/3704-my-shot-lyrics-hamilton.html', '/3703-the-story-of-tonight-lyrics.html', '/3702-the-schuyler-sisters-lyrics.html', '/3701-farmer-refuted-lyrics.html', '/3700-youll-be-back-lyrics-hamilton.html', '/3699-right-hand-man-lyrics.html', '/3698-a-winters-ball-lyrics.html', '/3697-helpless-lyrics.html', '/3696-satisfied-lyrics.html', '/3695-the-story-of-tonight-reprise-lyrics.html', '/3694-wait-for-it-lyrics-hamilton-the-musical.html', '/3693-stay-alive-lyrics.html', '/3692-ten-duel-commandments-lyrics.html', '/3691-meet-me-inside-lyrics.html', '/3690-that-would-be-enough-lyrics.html', '/3689-guns-and-ships-lyrics.html', '/3688-history-has-its-eyes-on-you-lyrics.html', '/3687-yorktown-the-world-turned-upside-down-lyrics.html', '/3686-what-comes-next-lyrics.html', '/3685-dear-theodosia-lyrics.html', '/3684-non-stop-lyrics.html', '/3683-whatd-i-miss-lyrics.html', '/3682-cabinet-battle-1-lyrics.html', '/3681-take-a-break-lyrics.html', '/3680-say-no-to-this-lyrics.html', '/3679-the-room-where-it-happens-lyrics.html', '/3678-schuyler-defeated-lyrics.html', '/3677-cabinet-battle-2-lyrics-hamilton.html', '/3676-washington-on-your-side-lyrics-hamilton.html', '/3675-one-last-time-lyrics.html', '/3674-i-know-him-lyrics.html', '/3673-the-adams-administration-lyrics.html', '/3672-we-know-lyrics.html', '/3671-hurricane-lyrics.html', '/3670-the-reynolds-pamphlet-lyrics.html', '/3669-burn-lyrics-hamilton-the-musical.html', '/3668-blow-us-all-away-lyrics.html', '/3667-stay-alive-reprise-lyrics.html', '/3666-its-quiet-uptown-lyrics.html', '/3665-election-of-1800-lyrics-hamilton.html', '/3664-your-obedient-servant-lyrics.html', '/3663-best-of-wives-and-best-of-women-lyrics.html', '/3662-the-world-was-wide-enough-lyrics.html', '/3661-who-lives-who-dies-who-tells-your-story-lyrics.html',]

def writeFile(href):
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical-lyrics"

    titleRegex = re.compile(r'\/\d{4}-.*[^\.html]')
    title = titleRegex.search(href).group()

    if int(title[1:5]) > 3706 or int(title[1:5]) < 3661:
        print "rejected " + title + ".txt"
        return None

    fc = urllib.urlopen(main_url + href).read()
    fc = fc[fc.find("Hamilton the Musical - "):]

    fc = re.sub(r'<[^>]*>', '\n', fc)  # tags
    fc = re.sub(r'(\sand\s)?\([^\)]*\)', '', fc)  # parantheses

    encoding_faults = [u'\u2014',u'\u2019',u'\u2026']
    for o in encoding_faults:
        fc = fc.replace(o, '')

    fc = fc.replace('/'," AND ")
    fc = fc.replace('&amp;',"AND")

    for c in ':—-!",?.\xe2\x80\x9c\x9d\r':
        fc = fc.replace(c, '')

    startRegex = re.compile(r'[A-Z]{2,}|[A-Z][a-z]+\ssay|I\ssaved|\[[A-Za-z\/:\s,]*\]')
    start = startRegex.search(fc).group()
    fc_s = fc.find(start)

    fc = fc[fc_s:fc.rfind('Read more')]

    return [fc,title]

def drive(x):
    fileContent = writeFile(hrefs[x])
    f = open('data/' + fileContent[1] + '.txt', 'w')
    f.write(fileContent[0])
    f.close()

drive(0)