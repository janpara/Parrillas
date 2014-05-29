import sqlite3
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
    cursor.execute('SELECT codigo FROM kdc where id = 5')
    for row in cursor:
        print row



    #conexion.close()


def avanzar_dia():
    conexion = sqlite3.connect('base_de_datos')
    cursor = conexion.cursor()
    fichero_anterior = open("prueba.txt","r+")
    longitud = len(open('prueba.txt').readlines())
    for iteracion in range(longitud):
        #fichero = anterior.readline()
        #print iteracion
        #print fichero
        posicion = fichero_anterior.tell()
        actual = fichero_anterior.readline()

        print posicion
        if 'KDC' in actual:
            cursor.execute("SELECT id FROM kdc where codigo =:codigo",{"codigo": actual})
            dato = cursor.fetchone()
            nuevo = dato[0] + 1

            #print dato
            cursor.execute("SELECT codigo FROM kdc where id =:id",{"id": nuevo})

            nuevo_codigo = cursor.fetchone()
            print nuevo_codigo
            #print dato
            #print nuevo
            #fichero_anterior = open("prueba.txt","w")
            fichero_anterior.seek(posicion)
            fichero_anterior.write(nuevo_codigo[0])






#leer_catalogo()
avanzar_dia()
