# Importando tkinter para graficos, ttk para opciones extras y datetime para la hora actual
from tkinter import *
from tkinter import ttk
from fun import *

# Saber la hora y refrescarla
def refrescar_tiempo_transcurrido():
    # Extraer hora actual
    horaActual = str(datetime.now().strftime("%H:%M:%S"))
    # Cambiar variable de lblHora
    varHora.set(horaActual)
    # Loop
    ventana.after(1, refrescar_tiempo_transcurrido)

# Mi ventana principal
ventana = Tk()
ventana.title("SISTEMA DE VENTAS")
ventana.geometry("800x500")
ventana.resizable(height = False, width = False)
ventana.iconbitmap("icon.ico")
centrarVentana(ventana,800,500)

# ----------------------------------------- Variables que se usaran de tkinter para modificar los labels ---------------------------- 
varHora=StringVar()

varRuc=StringVar()
varEmpresa=StringVar()

varNumeroFac=StringVar()
varFacSerie=StringVar()

varCantidad=IntVar()
varArticulo=StringVar()
varPrecioUni=DoubleVar()

varSubTotal=DoubleVar()
varIgv=DoubleVar()
varTotal=DoubleVar()


# Numero al lado del numero de la factura
numcorrelativa = 10
varFacSerie.set(numcorrelativa)
# -------------------------------------------------- Cuerpo de la ventana ---------------------------------------------------------
# Titulo en el cuerpo
lblTitulo = Label(ventana,text="Creación de Facturas").place(x=300,y=20)

# La hora
lblHora = Label(ventana,textvariable=varHora).place(x=700, y=50)

# Datos de la empresa
lblRuc = Label(ventana,text="RUC:").place(x=50, y=60)
txtRuc=Entry(ventana,textvariable=varRuc).place(x=130,y=60)

lblEmpresa = Label(ventana,text="Empresa:").place(x=50, y=90)
txtEmpresa=Entry(ventana,textvariable=varEmpresa).place(x=130,y=90)

# Datos de factura a la derecha
lblFactura = Label(ventana,text="Nro. de factura:").place(x=400 ,y=100)
txtNumeroFac = Entry(ventana,textvariable=varNumeroFac).place(x=500,y=100)
txtFacSerie = Entry(ventana,textvariable=varFacSerie).place(x=600,y=100)
# -------------------------------------------------------------------- TABLA ---------------------------------------------------------
lblCabeceraTabla = Label(ventana,text="CANTIDAD              ARTICULO                      PRECIO UNITARIO").place(x=100, y=150)
# Entradas
txtCantidad = Entry(ventana,textvariable = varCantidad).place(x=100,y=170)
txtArticulo = Entry(ventana,textvariable = varArticulo)
txtArticulo.place(x=200,y=170)
txtArticulo.insert(0,"null")
txtPrecioUni = Entry(ventana,textvariable = varPrecioUni).place(x=320,y=170)

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

# Botones
bntAgregar=Button(ventana, text="Agregar",command = lambda:agregar(tv, varCantidad, varPrecioUni, varArticulo)).place(x=450, y=165)
bntGuardar=Button(ventana, text="Guardar Boleta",command = lambda:comprobar(ventana, tv, varNumeroFac, varFacSerie, varRuc, varEmpresa, varSubTotal, varIgv, varTotal)).place(x=100, y=450)
bntCalcular=Button(ventana, text="Calcular",command = lambda:calcular(tv, varSubTotal, varIgv, varTotal, )).place(x=520, y=450)

# Etiquetas
lblSubtotal = Label(ventana,text="SUBTOTAL:").place(x = 520, y = 350)
lblIgv = Label(ventana,text="IGV:").place(x = 520, y = 380)
lblTotal = Label(ventana,text="TOTAL:").place(x = 520, y = 410)
# Entradas
txtSubtotal = Entry(ventana,textvariable = varSubTotal).place(x = 600,y = 350)
txtIgv = Entry(ventana,textvariable = varIgv).place(x = 600,y = 380)
txtTotal = Entry(ventana,textvariable = varTotal).place(x = 600,y = 410)

leerFactura(varNumeroFac, 0)
refrescar_tiempo_transcurrido()
ventana.mainloop()