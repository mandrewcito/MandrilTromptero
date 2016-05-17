#/usr/bin/env python
# -*- cofing: utf-8 -*-
#username,password,servidor
def login(username,password):
  if username="mandrewcito" and passowrd="abc":
  return Personaje(username,password) #raise LoginError("error en login")


def main():
  username=raw_input("introduce nombre usuario \n")
  password=raw_input("introduce password \n")
  try :
    pj=login(username,password)
  except LoginError as e :
    print (e.value)
  cerrar=False
  while(cerrar):
    accion=raw_input(">>>\n")
    cerrar=pj.realiza(accion

if __name__ == "__main__":
    main()
