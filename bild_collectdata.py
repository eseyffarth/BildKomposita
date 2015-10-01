__author__ = 'Esther'

import re
import urllib.request
import xml.etree.ElementTree as ET

################################################################################
### NLP part                                                                   #
################################################################################

def find_compounds(text):
    """
    Find compounds with a linking "-" via regular expression
    """
    compound_pattern = re.compile(u"[A-ZÄÖÜa-zäöüß]+\-[A-ZÄÖÜa-zäöüß]+")
    firsts = set()
    seconds = set()
    for item in re.findall(compound_pattern, text):
        f, s = item.split("-")
        firsts.add(f)
        seconds.add(s)
    return [firsts, seconds]

################################################################################
### data collection part                                                       #
################################################################################

def write_data(first_path, second_path, data):
    """
    Write data to files in order to access word parts later
    """
    with open(first_path, "r", encoding="utf8") as first_file:
        firsts = set([line.strip() for line in first_file.readlines()])
    with open(second_path, "r", encoding="utf8") as second_file:
        seconds = set([line.strip() for line in second_file.readlines()])

    first_file = open(first_path, "w", encoding="utf8")
    second_file = open(second_path, "w", encoding="utf8")

    for item in data[0]:
        firsts.add(item)
    for item in data[1]:
        seconds.add(item)

    for item in firsts:
        first_file.write(item + "\n")
    for item in seconds:
        second_file.write(item + "\n")

    first_file.close()
    second_file.close()
    return

def data_collect():
    """
    Open RSS Feed, read link descriptions from last 100 posts, look for compounds,
    write results to files
    """
    feedurl = "http://www.bild.de/rss/feeds/bild-3409238,n=100,sort=1,view=rss2.bild.xml"
    feedpage = urllib.request.urlopen(feedurl)
    feedcontent = feedpage.read()
    feedcontent = feedcontent.decode("utf-8")
    data = ET.fromstring(feedcontent)[0]

    content = ""
    for child in data:
        if child.tag == "item":
            content += child[0].text + "\n"

    comps = find_compounds(content)
    write_data("./bild_data/1.txt", "./bild_data/2.txt", comps)


data_collect()

