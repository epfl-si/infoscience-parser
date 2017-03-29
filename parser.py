#!/usr/bin/env python
""" (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017 """

import argparse
import logging

try:
    # python 3
    from urllib.request import urlopen
except:
    # python 2.7
    from urllib2 import urlopen

class Record:
    def __init__(self, id="", title=""):
        self.id = id
        self.title = title
        self.authors = []

class Author:
    def __init__(self, name="", sciper=""):
        self.name = name
        self.sciper = sciper

def do_request(url):
    logging.info("Fetching %s"% url)
    c = urlopen(url)
    records = []

    old_id = 0
    r = Record()

    for line in c:
        logging.debug("Parsing line %s"% line)
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

    logging.info("Fetched %d records"% len(records))
    return records

def display_records(records):
    for r in records:
        for author in r.authors:
            print(author.name)


if __name__ == '__main__':
    # create parser for command line arguments
    parser = argparse.ArgumentParser(description='Parse result from request on Infoscience')
    parser.add_argument('url', metavar='URL', type=str,
                        help='The URL where to make the request')
    parser.add_argument('--display-records', dest='display', action='store_true',
                        help='Print records fetched')
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='Set logging level to DEBUG (default is INFO)')
    parser.add_argument('--quiet', dest='quiet', action='store_true',
                        help='Set logging level to WARNING (default is INFO)')
    args = parser.parse_args()
    # set debug level
    if args.quiet:
        logging.basicConfig(level=logging.WARNING)
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    # query URL and parse records
    logging.info("Starting parser...")
    records = do_request(args.url)
    # display records (if gently asked)
    if args.display:
        logging.info("Displaying records...")
        display_records(records)