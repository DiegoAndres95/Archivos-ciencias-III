import sys

class Variable:
      def __init__(self, nombre, valor):
        self.nombre=nombre
        self.valor=valor
        
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


opcion = '0'
lista = []
while (opcion!='2'):
    opcion = raw_input("Seleccione una de las siguientes opciones:   \n 1. Agregar una nueva operación \n 2. Terminar la ejecución \n")
    if (opcion == '1'):                    
        p=Pila()
        cadena= raw_input("Ingrese la operacion en notacion postfija: ")
        notacion=cadena.split(" ")

        for i in range(len(notacion)-1):
            if notacion[i+1] == '=':
                valor = evaluar(p.extraer())
                print(notacion[i] + ' = ' + str(valor))
                variable = Variable(notacion[i],valor)
                lista.append(variable)
            else:
                if(notacion[i]!='+' and notacion[i]!='-' and notacion[i]!='*' and notacion[i]!='/'):
                    if (notacion[i].isalpha()):
                         for j in range (len(lista)):
                              if (lista[j].nombre==notacion[i]):
                                   p.incluir(lista[j].valor)                  
                    else:  
                         p.incluir(notacion[i])
                else:
                    num1=p.extraer()
                    num2=p.extraer()
                    nodo=Nodo(notacion[i],num2,num1)
                    p.incluir(nodo)        
    else:
        if (opcion == '2'):
            print ("Gracias")  
        else:
            print ("Seleccione una opcion valida")
