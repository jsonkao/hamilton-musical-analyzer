import urllib
import re

def main():
    main_url = "http://www.themusicallyrics.com/h/351-hamilton-the-musical.html"
    f = urllib.urlopen(main_url)
    s = f.read()

    table_s = s.find('<form action="http://www.themusicallyrics.com/h/351-hamilton-the-musical.html" method="post" name="adminForm">')
    table_e = s.find('<input type="hidden" name="id" value="351">', table_s)
    table_html = s[table_s:table_e].split('</tr>')[3:]

    links = []
    for entry in table_html[:2]:
        href_s = entry.find('<a href="') + len('<a href="')
        href_e = entry.find('">', href_s)
        href = entry[href_s:href_e]
        
        s = urllib.urlopen(main_url + href).read()
        mark = '</em><br /><br />'
        piece_s = s.find(mark) + len(mark)
        piece_e = s.find('</p>',piece_s)

        

