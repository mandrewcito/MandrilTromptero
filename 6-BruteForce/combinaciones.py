#/usr/bin/env python
# --*-- coding: utf-8 --*--

import const as c
import os,sys
def main():
  # Get the total number of args passed
  total = len(sys.argv)-1
  # Get the arguments list 
  args = sys.argv[1:]
  #your_list = open("probar.txt").readline().replace("\n","")
  your_list = c.letrasPermutar
  complete_list = []
  for current in xrange(10):
    a = [i for i in your_list]
    for y in xrange(current):
      a = [x+i for i in your_list for x in a]
    complete_list = complete_list+a

if __name__ == "__main__":
  main()
