import sys 
import re
class Variable:
      def __init__(self, nombre, valor):
        self.nombre=nombre
        self.valor=valor

class Token:
      def __init__(self, tipo, valor):
        self.tipo=tipo
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
patronVariable = re.compile('^[^a-z]|[^a-zA-Z0-9_]')
patronValor = re.compile('[^0-9]')
patronOperador = re.compile('^[+]$|^[*]$|^[-]$|^[/]$|^[=]$')
lista = []
lista2 = []
valido = True
while (opcion!='2'):
    valido = True  
    opcion = raw_input("Seleccione una de las siguientes opciones:   \n 1. Agregar una nueva operación \n 2. Terminar la ejecución \n")
    if (opcion == '1'):
        p=Pila()
        cadena= raw_input("Ingrese la operacion en notacion postfija: ")
        notacion=cadena.split(" ")
        for i in range(len(notacion)):
              if not(patronVariable.search(notacion[i])):
                    if (valido):
                          token = Token("Variable", notacion[i])
                          lista2.append(token)
                          if notacion[i+1] == '=':
                              valor = evaluar(p.extraer())
                              print(notacion[i] + ' = ' + str(valor))
                              variable = Variable(notacion[i],valor)
                              lista.append(variable)
                          else:
                               for j in range (len(lista)):
                                    if (lista[j].nombre==notacion[i]):
                                         p.incluir(lista[j].valor)  
                        
              else:
                    if not (patronValor.search(notacion[i])):
                           if (valido):
                                token = Token("Valor", notacion[i])
                                lista2.append(token)
                                p.incluir(notacion[i])
                    else:
                          if (patronOperador.search(notacion[i])):
                                if (valido):
                                      token = Token("Operador", notacion[i])
                                      lista2.append(token)
                                      if notacion[i] != '=':
                                          num1=p.extraer()
                                          num2=p.extraer()
                                          nodo=Nodo(notacion[i],num2,num1)
                                          p.incluir(nodo)    
                          else:
                                print ("se introdujo una expresion no valida, debido a la variable: " + notacion[i])
                                valido = False
        if (valido):                        
              print ("se ingresaron los siguientes elementos:")
              for j in range(len(lista2)):
                  print (lista2[j].tipo + " " + lista2[j].valor)                            
    else:
        if (opcion == '2'):
            print ("Gracias")
            print ("Los datos guardados en la ejecucion fueron los siguientes:")
            for j in range(len(lista2)):
                  print (lista2[j].tipo + " " + lista2[j].valor)  
        else:
            print ("Seleccione una opcion valida")
