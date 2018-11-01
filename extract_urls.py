#!/usr/bin/env python
import sys, re

def extract_urls(fname):
    with open(fname) as f:
        return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', f.read())
      
def main(argv):
    list = extract_urls(argv[1])
    for links in list:
        print(links)

if __name__ == '__main__':
    main(sys.argv)
