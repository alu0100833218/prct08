#! /usr/bin/python
#!encoding: UTF-8


PI = 3.14159265358979323846264338327950288

def g(n):
  if (n!=0):
    suma=0
    for i in range (1, n+1):
      a = float (i-1)/n
      b = float (i)/n
      xi = (i-0.5)/n
      fxi = 4.0/(1.0 + xi*xi)
      suma += fxi
    pi = float (suma)/n
    return pi
 
if (__name__=="__main__"):
  import sys
  if((len(sys.argv) == 1) or (len(sys.argv) == 2)):
    print"No ha introducido los argumentos necesarios, usaremos los estándar, que son 100 intervalos y 10 repeticiones"
    n = 100
    v = 10
  else:
    n = int(sys.argv[1])
    v = int(sys.argv[2])
  lista = []
  for j in range (1, v+1):
    pi = g(j*n)
    lista = lista + [pi]
  print lista