frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
Lista-->list-->lista
Elemento->str-->elemento
Salidas
Lista-->list
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    a=i.replace(elemento,"")
    auxilar.append(a)
  return auxilar
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  print(nueva)
#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista-list-->lista
Salidas:
lista-list-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def copia_lista(lista):
  aux=[]
  for i in lista:
    aux.append(i)
  return aux
#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-list-->lista
Salidas:
lista-list-->lista
"""  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar 
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_pares(nueva)
  print(nueva_dos)
#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
Lista-->list-->lista
Elemento->str-->elemento
Salidas:
lista-list-->lista
"""  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def numeros_pares(lista):
  aux=[]
  for i in lista:
    if(float(i)%2==0):
      aux.append(i)
  return aux
def elimina_elemento_lista(lista,elemento):
  lista.remove(elemento)
  return lista
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_pares(nueva)
  eliminar=elimina_elemento_lista(nueva_dos,'10')
  print(eliminar)
#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Lista-->list-->lista
Elemento->str-->elemento
Salidas:
lista-list-->lista
"""  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def letra(lista,elemento):
  auxiliar=[]
  for x in lista:
    if(x[0]=="X"):
      print(x)
      auxiliar.append(x)
  return auxiliar
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=letra(nueva,"")
  print(nueva_dos)
#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Lista-->list-->lista
Salidas:
Tamaño-->int-->tamano
"""   
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def tamano_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux 
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=tamano_lista(nueva)
  print(nueva_dos)
#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
Lista-->list-->lista
Salidas:
Tamaño-->int-->tamano
"""  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def informacion_lista(lista):
  aux=[]
  for i in lista:
    print (len(lista))
    return aux
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
  nueva_dos=informacion_lista(nueva)
  print(type(nueva_dos))
#Retornar una lista con los numeros negativos  
"""
Entradas:
Lista-->list-->lista
Salidas:
Lista-->list-->lista
"""  
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def numeros_negativos(lista):
  aux=[]
  for i in lista:
    if(float(i)<=0):
      aux.append(i)
  return aux
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  nueva_dos=numeros_negativos(nueva)
  print(nueva_dos)
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Lista-->list-->lista
Elemento->str-->elemento
Salidas:
lista-list-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def posicion_elemento(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return lista_posiciones
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
print("Ingresa una fruta que se encuentre en la lista:")
elemento = input() 
posicion = posicion_elemento(nueva, elemento)
print(posicion)
#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Lista-->list-->lista
Elemento->str-->elemento
Salidas:
lista-list-->lista
"""
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def frutas(lista,elemento):
  lista.append(elemento)
  return lista
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_frutas,"\n")
print("Ingrese la nueva fruta: ")
elemento=input()
nueva_fruta = frutas(nueva, elemento)
print(nueva_fruta)
#Realizar una funcion que cuente el numero de veces que se repite un elemento 
"""
Entradas:
Lista-->list-->lista
Salidas:
Lista-->list-->lista
""" 
def eliminar_un_caracter(lista,elemento):
  auxilar=[]
  for i in lista:
    X=i.replace(elemento,"")
    auxilar.append(X)
  return auxilar
def repetir(lista , elemento):
    lista_posiciones = []
    for i in list(range(0,len(lista))):
        if str(lista[i]) == str(elemento): 
            lista_posiciones.append(i)
    return len(lista_posiciones)
if __name__ == "__main__":
  nueva=eliminar_un_caracter(lista_numeros,"\n")
  print("Ingresa el numero que se repite en la lista de numeros: ")
  elemento = input()
  repeticiones = repetir(nueva, elemento)
  print(repeticiones)
