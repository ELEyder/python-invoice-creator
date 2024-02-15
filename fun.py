from datetime import *
from tkinter import *
# ----------------------------------------------------------- Funciones -------------------------------------------------------------
# Refrescar el tiempo que aparece en la pantalla actualizando la variable varHora


# Leer para colocar automaticamente el numero de la boleta
def leerFactura(varNumeroFac, a):
    # Ruta de el numero de boleta que sigue
    ruta = "datos/num.txt"
    # Abrir archivo
    archivoNum = open(ruta,"r")
    # Comprobar de que no está vacío
    index = archivoNum.readline()
    if index == "":
        archivoNum.close()
        archivoNum = open(ruta,"w")
        archivoNum.write("1")
        index = 1
        archivoNum.close()
        archivoNum = open(ruta,"r")
    # Guardar el numero
    try:
        nuevoNum = (int(index) + a)
    except Exception:
        archivoNum.close()
        archivoNum = open(ruta,"w")
        archivoNum.write("1")
        index = 1
        archivoNum.close()
        archivoNum = open(ruta,"r")
        nuevoNum = (int(index) + a)

    # Cerrar archivo
    archivoNum.close()
    # Escribir en el archivo donde exraimos el num
    archivoNum = open(ruta,"w")
    # Decidir el formato de que se va a escribir
    if nuevoNum < 10:
        nuevoNum2 = "F00" + (str(nuevoNum))
    elif nuevoNum < 100:
        nuevoNum2 = "F0" + (str(nuevoNum))
    else:
        nuevoNum2 = "F" + (str(nuevoNum))
    # Cambiar el texto
    varNumeroFac.set(nuevoNum2)
    # Cambiar el archivo del numero
    archivoNum.write(str(nuevoNum))
    # Cerrar archivo
    archivoNum.close()
    print("Factura Leída")

# Calcular los datos extraidos de la lista de tkinter
def calcular(tv, varSubTotal, varIgv, varTotal):
    subTotal = 0.0
    for child in tv.get_children():
        # Convertir el hijo de la tv a una lista
        lista = tv.item(child,'values')
        # Almacenar el SubTotal
        subTotal = float(lista[3]) + subTotal
    # Actualizar el subTotal
    varSubTotal.set(subTotal)
    # Calcular igv
    igv = round(subTotal*0.18,3)
    # Cambiar la Variable de varIgv
    varIgv.set(igv)
    # Actualizar la variable del total
    varTotal.set(round((subTotal + igv),3))
    print("Subtotal, IGV y Total calculado.")
# Comprobar los datos antes de guardar los datos
def comprobar(ventana, tv, varNumeroFac, varFacSerie, varRuc, varEmpresa, varSubTotal, varIgv, varTotal):
    if varRuc.get() != "" and varEmpresa.get() != "" and varFacSerie.get() != "" and varNumeroFac.get() != "":
        guardar(tv, varNumeroFac, varFacSerie, varRuc, varEmpresa, varSubTotal, varIgv, varTotal)
    else:
        # ---------------------------------------------------- Inicio de Ventana Emergente -------------------------------------------------------
        ventana_top = Toplevel(ventana)
        ventana_top.title("Alerta")
        ventana_top.geometry("300x100")
        ventana_top.resizable(height = False, width = False)
        centrarVentana(ventana_top,300,100)

        lblTop= Label(ventana_top, text="No se permiten entradas en blanco")
        lblTop.place(x=35,y=20)
        
        btnCerrarTop = Button(ventana_top, text="Aceptar", command=ventana_top.destroy)
        btnCerrarTop.place(x=125,y=60)
        ventana_top.focus()
        ventana_top.grab_set()
# Guardar los datos en el archivo txt
def guardar(tv, varNumeroFac, varFacSerie, varRuc, varEmpresa, varSubTotal, varIgv, varTotal):
    #Excribir Ruta
    ruta = "datos/principal.txt"
    # Abrir archivo
    archivo = open(ruta,"a")
    # Capturar la Hora
    hora = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sep=" - "
    principal = varNumeroFac.get() + sep + varFacSerie.get() + sep + varRuc.get() + sep + varEmpresa.get() + sep + \
        str(varSubTotal.get()) + sep + str(varIgv.get()) + sep + str(varTotal.get()) + sep + hora
    archivo.write(principal+"\n")
    archivo.close()
    # Abrir Segundo archivo
    ruta = "datos/detalles.txt"
    archivo = open(ruta,"a")
    for child in tv.get_children():
        # Extraer arreglo
        lista = tv.item(child,'values')
        detalles = varNumeroFac.get() + sep + varFacSerie.get() + sep + lista[1] + sep + lista[0] + sep + lista[2] + sep + lista[3]
        archivo.write(detalles+"\n")
    leerFactura(varNumeroFac, 1)
    print("Factura Guardada")

posicion = 0
# Agregar un precio escrito 
def agregar(tv, varCantidad, varPrecioUni, varArticulo):
    global posicion
    importe = 0
    importe = round((varCantidad.get() * varPrecioUni.get()), 3)
    tv.insert(parent='', index=posicion, iid=posicion, text='', values=(varCantidad.get(), varArticulo.get(),varPrecioUni.get(),importe))
    posicion=posicion+1
    print("Precio Agregado.")

def centrarVentana(ventana,w,h):
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = ventana.winfo_screenwidth()
    htotal = ventana.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = w
    hventana = h
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    #  Se lo aplicamos a la geometría de la ventana
    ventana.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
