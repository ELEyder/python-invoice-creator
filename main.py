# Importando tkinter para graficos, ttk para opciones extras y datetime para la hora actual
from tkinter import *
from tkinter import ttk
from datetime import *

# Saber la hora
horaActual = str(datetime.now().strftime("%H:%M:%S"))

# ----------------------------------------------------------- Funciones -------------------------------------------------------------
# Refrescar el tiempo que aparece en la pantalla actualizando la variable varHora
def refrescar_tiempo_transcurrido():
    # Extraer hora actual
    horaActual = str(datetime.now().strftime("%H:%M:%S"))
    # Cambiar variable de e lblHora
    varHora.set(horaActual)
    # Loop
    ventana.after(1, refrescar_tiempo_transcurrido)

# Leer para colocar automaticamente el numero de la boleta
def leerFactura():
    # Ruta de ek numero de boleta que sigue
    ruta = "datos/num.txt"
    # Abrir archivo
    archivoNum = open(ruta,"r")
    # Comprobar de que no está vacío
    index = archivoNum.readline()
    if index == "":
        archivoNum.write("0")
    # Guardar el numero + 1
    nuevoNum = (int(index) + 1)
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
def calcular():
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
def comprobar():
    if varRuc.get() != "" and varEmpresa.get() != "":
        guardar()
    else:
        # ---------------------------------------------------- Inicio de Ventana Emergente -------------------------------------------------------
        ventana_top = Toplevel(ventana)
        ventana_top.title("Alerta")
        ventana_top.geometry("300x100")
        ventana_top.resizable(height = False, width = False)
        centrarVentana(ventana_top,300,100)

        lblTop= Label(ventana_top, text="El ruc o el nombre de la empresa está Vacío")
        lblTop.place(x=35,y=20)
        
        btnCerrarTop = Button(ventana_top, text="Aceptar", command=ventana_top.destroy)
        btnCerrarTop.place(x=125,y=60)
        ventana_top.focus()
        ventana_top.grab_set()
# Guardar los datos en el archivo txt
def guardar():
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
    leerFactura()
    print("Factura Guardada")

posicion = 0
# Agregar un precio escrito 
def agregar():
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

# ---------------------------------------------------- Inicio de Mi ventana -------------------------------------------------------
#CARACTERISTICAS
ventana = Tk()
ventana.title("SISTEMA DE VENTAS")
ventana.geometry("800x500")
ventana.resizable(height = False, width = False)
ventana.iconbitmap("icon.ico")
centrarVentana(ventana,800,500)

# ----------------------------------------- Variables que se usaran de tkinter para modificar los labels ---------------------------- 
varFacSerie=StringVar()
varNumeroFac=StringVar()
varCantidad=IntVar()
varArticulo=StringVar()
varPrecioUni=DoubleVar()
varSubTotal=DoubleVar()
varIgv=DoubleVar()
varTotal=DoubleVar()
varRuc=StringVar()
varEmpresa=StringVar()
varHora=StringVar()
# Numero al lado del numero de la factura
numcorrelativa = 10
varFacSerie.set(numcorrelativa)
# -------------------------------------------------- Cuerpo de la ventana ---------------------------------------------------------
# Titulo en el cuerpo
lblTitulo = Label(ventana,text="Creación de Facturas").place(x=300,y=20)
# Datos de la empresa
lblRuc = Label(ventana,text="RUC:").place(x=50, y=60)
lblEmpresa = Label(ventana,text="Empresa:").place(x=50, y=90)

txtRuc=Entry(ventana,textvariable=varRuc).place(x=130,y=60)
txtEmpresa=Entry(ventana,textvariable=varEmpresa).place(x=130,y=90)
# La hora
lblHora = Label(ventana,textvariable=varHora).place(x=700, y=50)
# Datos de factura a la derecha
lblFactura = Label(ventana,text="Nro. de factura:").place(x=400 ,y=100 )

txtFactura = Entry(ventana,textvariable=varNumeroFac).place(x=500,y=100)
txtboleta2 = Entry(ventana,textvariable=varFacSerie).place(x=600,y=100)
# Datos a ingresar a la tabla
lblboleta = Label(ventana,text="CANTIDAD              ARTICULO                      PRECIO UNITARIO").place(x=100, y=150)
# Entradas
txtCantidad = Entry(ventana,textvariable = varCantidad).place(x=100,y=170)
txtArticulo = Entry(ventana,textvariable = varArticulo)
txtArticulo.place(x=200,y=170)
txtArticulo.insert(0,"null")
txtPrecioUni = Entry(ventana,textvariable = varPrecioUni).place(x=320,y=170)
# Botones
bntguardar=Button(ventana, text="Agregar",command = agregar).place(x=450, y=165)
bntguardar=Button(ventana, text="Guardar Boleta",command = comprobar).place(x=100, y=450)
bntguardar=Button(ventana, text="Calcular",command = calcular).place(x=520, y=450)
# --------------------------------------------------- VENTANA DE LAS CUENTAS ---------------------------------------------------------
tv = ttk.Treeview(ventana)
tv["columns"] = ("CANTIDAD","ARTICULO","PRECIOUNIT","IMPORTE")
tv.column("#0", width = 0, stretch = NO)
tv.column("CANTIDAD", anchor = CENTER, width=100)
tv.column("ARTICULO", anchor = CENTER, width=100)
tv.column("PRECIOUNIT", anchor = CENTER, width=100)
tv.column("IMPORTE", anchor = CENTER, width=100)

tv.heading("#0",text="",anchor = CENTER)
tv.heading("CANTIDAD",text="CANTIDAD",anchor = CENTER)
tv.heading("ARTICULO",text="ARTICULO",anchor = CENTER)
tv.heading("PRECIOUNIT",text="PRECIOUNIT",anchor = CENTER)
tv.heading("IMPORTE",text="IMPORTE",anchor = CENTER)

tv.place(x=100,y=210)
# Etiquetas
lblSubtotal = Label(ventana,text="SUBTOTAL:").place(x = 520, y = 350)
lblIgv = Label(ventana,text="IGV:").place(x = 520, y = 380)
lblTotal = Label(ventana,text="TOTAL:").place(x = 520, y = 410)
# Entradas
txtSubtotal = Entry(ventana,textvariable = varSubTotal).place(x = 600,y = 350)
txtIgv = Entry(ventana,textvariable = varIgv).place(x = 600,y = 380)
txtTotal = Entry(ventana,textvariable = varTotal).place(x = 600,y = 410)

leerFactura()
refrescar_tiempo_transcurrido()
ventana.mainloop()