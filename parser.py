try:
    # python 3
    from urllib.request import urlopen
except:
    # python 2.7
    from urllib2 import urlopen

c = urlopen("https://infoscience.epfl.ch/search?cc=Infoscience%2FResearch%2FENAC&ln=fr&as=1&ext=collection%3AARTICLE&rg=50&of=t&ot=001,700,245")

class Record:
    def __init__(self, id="", title=""):
        self.id = id
        self.title = title
        self.authors = []

class Author:
    def __init__(self, name="", sciper=""):
        self.name = name
        self.sciper = sciper

records = []

old_id = 0
r = Record()

for line in c:
    id = line[:9]
    
    if id != old_id: # New record
        records.append(r)
        r = Record(id)
    else: # Same record
        nb = line[10:13]
        if nb == b'245': # Title
            title = line[19:-1]
            r.title = title
        elif nb == b'700': # Author
            a = Author(line[19:-1])
            r.authors.append(a)

    old_id = id


for r in records:
    for author in r.authors:
        print(author.name)

