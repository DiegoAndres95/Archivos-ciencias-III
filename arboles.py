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
        
class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der
def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))   
      return int(arbol.valor)
    except AttributeError:
      return int(arbol)

p=Pila()

cadena= raw_input("Ingrese la operacion en notacion postfija: ")
notacion=cadena.split(" ")

for i in range(len(notacion)):
    if(notacion[i]!='+' and notacion[i]!='-' and notacion[i]!='*' and notacion[i]!='/'):
        p.incluir(notacion[i])
    else:
        num1=p.extraer()
        num2=p.extraer()
        nodo=Nodo(notacion[i],num2,num1)
        p.incluir(nodo)
  
print ("el valor de la operacion es: " + str(evaluar(p.extraer())))
