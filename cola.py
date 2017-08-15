class Cola:

    def __init__(self):
        self.items=[]

    def encolar(self, item):
        self.items.append(item)
        
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        return self.items == []
    
class estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

q = Cola()
numero = int(raw_input("Digite el numero de estudiantes que haran cola: "))
for i in range(numero):
    nombre = raw_input("escriba el nombre del estudiante: ")
    apellido = raw_input("escriba el apellido del estudiante: ")
    estudiante1= estudiante(nombre, apellido)
    q.encolar(estudiante1)
numero2 = int(raw_input("Digite el numero de zonas de parqueo disponibles: "))    
for i in range(numero2):
    if (q.es_vacia()==False):
        estudiante4=q.desencolar()
        print("la zona de parqueo numero " + str(i+1) + " fue asignada al estudiante: " + estudiante4.nombre + " "+ estudiante4.apellido)
