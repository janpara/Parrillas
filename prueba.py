from random import randint
import sqlite3
class Programa(object):
    def __init__(self, nombre, capitulo):
        #self.catalogo = {}
        #self.clave = clave
        self.nombre = nombre
        self.capitulo = capitulo
        #self.codigo = codigo
        #self.duracion = duracion
        #self.tipo = tipo
        #self.ponderacion = ponderacion

    def inicializar_programa(self):

        self.catalogo = {}
        #self.tipo = tipo
        for iteracion in range(1,self.capitulo+1):
            self.catalogo[iteracion] = [self.nombre,self.capitulo,iteracion]
        return self.catalogo

    def inventar_duracion(self,min,max):
        self.min = min
        self.max = max
        for iteracion in range(1,self.capitulo+1):
            self.catalogo[iteracion].append(randint(self.min,self.max))

    def imprimir_catalogo(self):
        print "Nombre Total Cap Dur"
        for iteracion in range(1,self.capitulo+1):
            print self.catalogo[iteracion]

def leer_catalogo():
    kdc = {}
    #leemos el fichero con todos los capitulos y creamos un diccionario con ellos
    lineas = len(open('KDC.txt').readlines())
    fichero = open("KDC.txt", "r")
    for iteracion in range(lineas):
        dato = fichero.readline()
        if "/" in dato:
            pass
        else:
            #print dato
            kdc[iteracion] = dato

    # nos conectamos a la base de datos
    conexion = sqlite3.connect('base_de_datos')
    cursor = conexion.cursor()
    # creamos la tabla kdc con las columnas id y codigo
    #cursor.execute('''
    #CREATE TABLE kdc (
    #id		 INT	 PRIMARY KEY,
    #codigo	 TEXT
    #)
    #''')

    # con esto escribimos la base de datos con los valeores del diccionario kdc
    #for iteration in kdc:
    #    cursor.execute('''INSERT INTO kdc (id, codigo) VALUES (?,?)''' , (iteration, kdc[iteration]))


    #cursor.execute('''DROP TABLE kdc''')
    conexion.commit()
    #cursor.execute("UPDATE kdc set codigo = kdc[5] where id = 101")
    #conexion.commit()
    cursor.execute('SELECT * FROM kdc where id = 58')
    for row in cursor:
        print row



    #conexion.close()


tele = Programa("nes", 10)
noche = Programa("noche", 25)

tele.inicializar_programa()
noche.inicializar_programa()

#print tele.nombre
#print tele.capitulo
#print tele.catalogo

#print noche.nombre
#print noche.capitulo
#print noche.catalogo

#noche.inventar_duracion(10,30)

#print noche.catalogo
#noche.imprimir_catalogo()

leer_catalogo()





