#/usr/bin/env python
# --*-- coding: utf-8 --*--
import const as c
import os,sys,time,subprocess
from subprocess import Popen, PIPE
def main():
  # Get the total number of args passed 
  total = len(sys.argv)-1
  # Get the arguments list 
  args = sys.argv[1:]
  programaObjeto=args[0]
  t1=time.time()
  p = subprocess.Popen(["python",programaObjeto])
  p.communicate() #wait
  t2=time.time()
  print str(t2-t1)+" sec"

if __name__ == "__main__":
  main()
