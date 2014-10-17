#/usr/bin/env python
# -*- cofing: utf-8 -*-
import os,sys
import urllib
from getPic import GetPic

def main():
  # Get the total number of args passed to the demo.py
  total = len(sys.argv)-1
  # Get the arguments list 
  args = sys.argv[1:]
  if args[0]=="-h" or args[0]=="--help" or total==0:
    print "getImg.py [OPTIONS][SOURCE]"
    print "SOURCE can be a file(with links separated with \n) or an link"
    print "-h | --help  -> print this menu"
    print "-q quiet "
    return
  isFile=os.path.isfile(args[total-1])
  isURL=args[total-1].startswith("http://")
  if not isURL and not isFile:
    print "enter a valid url or a valid file "
    return
  quiet=""
  folder="."
  for n,arg in enumerate(args):
    if arg=="-q":
      quiet=arg
    if arg=="-f":
      folder=arg[n+1]
  getter=GetPic(quiet,folder)
  if isFile:
    getter.getMultimediaFromFile(args[total-1])
  if isURL:
    getter.getMultimedia(args[total-1])
if __name__ == "__main__":
    main()
