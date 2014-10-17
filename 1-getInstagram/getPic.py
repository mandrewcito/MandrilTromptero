import os
import urllib

class GetPic:
  def __init__(self,quiet,carpetaDestino):
    self.destino=carpetaDestino
    self.quiet=quiet

  def getMultimedia(self,link):
    get = urllib.urlopen(link)
    pagina = get.read()
    c=pagina.split("meta property=\"og:image\" content=\"")
    f=c[1].split("\"")
    imagen=f[0]
    os.system("wget "+self.quiet+" "+imagen+" ")

  def getMultimediaFromFile(self,fich):
    f=open(fich)
    lineas=f.read().split("\n")
    for linea in lineas:
      if linea.startswith("http://"):
        self.getMultimedia(linea)
      else:
        print linea+"is not a valid link"
