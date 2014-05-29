import Tkinter, tkFileDialog
import escribir_tabla_2
ventana = Tkinter.Tk()
def obtener_archivo():
    tipo = [
    ('texto','*.txt')]

    import Tkinter,tkFileDialog

    root = Tkinter.Tk()
    root.withdraw()

    file = tkFileDialog.askopenfile(parent=root,mode='rb',filetypes = tipo, title='Elige parrilla de origen')
    if file != None:

        archivo = file.name



    myFormats = [
    ('texto','*.txt')]


    root = Tkinter.Tk()
    root.withdraw()
    nombre_nuevo = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Introduce la fecha de la nueva parrilla (yyyy-mm-dd)")
    if len(nombre_nuevo ) > 0:

        escribir_tabla_2.avanzar_dia(archivo, nombre_nuevo)


ventana.config(bg="grey")
ventana.geometry("600x400")
ventana.title("Parrillas Generator")
boton = Tkinter.Button(ventana,text="Seleccionar parrilla origen", command =obtener_archivo)

boton.grid(row=3,column=0)
ventana.mainloop()

