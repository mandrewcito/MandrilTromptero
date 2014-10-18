import os
import urllib

class GetPic:
  def __init__(self,quiet,carpetaDestino,progress):
    self.destino=carpetaDestino
    self.quiet=quiet
    self.progress=progress

  def getMultimedia(self,link):
    get = urllib.urlopen(link)
    pagina = get.read()
    c=pagina.split("meta property=\"og:video\" content=\"")
    if len(c)==1:
      c=pagina.split("meta property=\"og:image\" content=\"")
    f=c[1].split("\"")
    mult=f[0]
    testfile = urllib.URLopener()
    nombre=mult.split("/")
    testfile.retrieve(mult, self.destino+"/"+nombre[len(nombre)-1])

  def getMultimediaFromFile(self,fich):
    f=open(fich)
    lineas=f.read().split("\n")
    descarga="---"
    for linea in lineas:
      if linea.startswith("http://"):
        self.getMultimedia(linea)
        if self.progress:
          print descarga+">"
        if not self.quiet:
          print "fichero "+linea+" descargado"
          descarga+=descarga
      else:
        if not self.quiet:
          print linea+"is not a valid link"
