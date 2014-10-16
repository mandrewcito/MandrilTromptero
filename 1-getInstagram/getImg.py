#/usr/bin/env python
# -*- cofing: utf-8 -*-
import os
import urllib
link=raw_input("introduce enlace \n")
get = urllib.urlopen(link)
pagina = get.read()
c=pagina.split("meta property=\"og:image\" content=\"")
f=c[1].split("\"")
imagen=f[0]
os.system("wget "+imagen)

