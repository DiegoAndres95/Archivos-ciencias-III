class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)

class pelicula:
    def __init__(self, nombre,genero):
        self.nombre = nombre
        self.genero = genero
       
p=Pila()
p2 = Pila()
numero = int(raw_input("Digite el numero de peliculas que ingresara a la pila: "))
for i in range (numero):
     nombre=raw_input("escriba el nombre de la pelicula: ")
     genero=raw_input("escriba el genero de la pelicula: ")
     print("-----------------------------------------------------")
     peli=pelicula(nombre,genero)
     p.incluir(peli)
for j in range (p.tamano()):
     peli2=p.extraer()
     p2.incluir(peli2)
busqueda = raw_input("digite el genero de las peliculas a buscar: ")
for h in range(p2.tamano()):
     if p2.items[h].genero == busqueda:
          print(p2.items[h].nombre +" "+ p2.items[h].genero )
print("-----------------------------------------------------")
print("peliculas en la pila: ")
for k in range(p2.tamano()):
     print(p2.items[k].nombre +" "+ p2.items[k].genero )
     
