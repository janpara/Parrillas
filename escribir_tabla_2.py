import sqlite3
import datetime
# se lee el fichero con todos los codigos del programa especificado
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

    # Se escriben los programas en la tabla programas
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("KIDS CLUB", "KDC"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("THE VERB CIRCUS", "Cnc"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("CULTURE VULTURE", "CVN"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("COMMUNICATION SHOW", "CSW"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("VAUGHAN 4.0 BASICO", "V4B"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("VAUGHAN 4.0 INTERMEDIO", "V4I"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("VAUGHAN 4.0 AVANZADO", "V4A"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("COMMON MISTAKES", "CMM"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("TVENGLISH", "TVE"))
    #cursor.execute('''INSERT INTO programas (nombre_programa, codigo_programa) VALUES (?,?)''' , ("VAUGHAN EN VIVO", "VEV"))

    # Se escriben los capitulos en la tabla capitulos
    #contador = 1
    #for iteration in kdc:

     #   cursor.execute('''INSERT INTO capitulos (codigo_programa,codigo_capitulo, numero_capitulo) VALUES (?,?,?)''' , ("KDC", kdc[iteration], contador))
      #  contador +=1

    #cursor.execute('''DROP TABLE kdc''')
    conexion.commit()
    #cursor.execute("UPDATE kdc set codigo = kdc[5] where id = 101")
    #conexion.commit()
    cursor.execute('SELECT * FROM programas')
    for row in cursor:
        print row
    cursor.execute('SELECT * FROM capitulos')
    for row in cursor:
        print row



    conexion.close()


def avanzar_dia(archivo_origen, nombre_fichero):
    conexion = sqlite3.connect('base_de_datos')
    cursor = conexion.cursor()
    fichero_anterior = open(archivo_origen)
    contenido = ''
    contador = 1
    for linea in fichero_anterior:
        if 'KDC' in linea:
            cursor.execute("SELECT numero_capitulo FROM capitulos where codigo_capitulo =:codigo_capitulo",{"codigo_capitulo": linea})
            dato = cursor.fetchone()
            nuevo = dato[0] + 1

            #print dato
            try:
                cursor.execute("SELECT codigo_capitulo FROM capitulos where numero_capitulo =:numero_capitulo",{"numero_capitulo": nuevo})

                nuevo_codigo = cursor.fetchone()
                contenido = contenido + nuevo_codigo[0]
            #cursor.execute('''INSERT INTO parrillas_guardadas (fecha_de_emision, orden, codigo_capitulo) VALUES (?,?,?)''' , ("2014-04-30", contador, nuevo_codigo[0]))
                contador += 1
            except Exception as e:
                print "ha ocurrido un error con la base de datos"
                print e
                cursor.execute("SELECT codigo_capitulo FROM capitulos where numero_capitulo =:numero_capitulo",{"numero_capitulo": 1})
                nuevo_codigo = cursor.fetchone()
                contenido = contenido + nuevo_codigo[0]
        else:

            contenido = contenido + linea
            #cursor.execute('''INSERT INTO parrillas_guardadas (fecha_de_emision, orden, codigo_capitulo) VALUES (?,?,?)''' , ("2014-04-30", contador, linea))
            contador += 1

    fichero_anterior.close()
    fichero_anterior = open (nombre_fichero+'.txt', 'w')
    fichero_anterior.write(contenido)
    ultimo_valor = str(nombre_fichero)
    obtener_valor = ultimo_valor.split("/")[-1:]
    print obtener_valor
    #thedate = datetime.datetime.strptime(obtener_valor, '%Y-%m-%d')
    thedate = "2033-01-01"
    cursor.execute('''INSERT INTO parrillas_guardadas (fecha_de_emision, parrilla) VALUES (?,?)''' , (thedate, contenido))
    conexion.commit()
    cursor.execute("SELECT * FROM parrillas_guardadas")
    prueba_base = cursor.fetchone()
    print prueba_base
    fichero_anterior.close()
    print 'fichero nuevo escrito'







#leer_catalogo()
#avanzar_dia()

