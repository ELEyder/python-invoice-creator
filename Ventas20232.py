from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import *

ttotal=0
posicion=0
importe=0
numcorrelativa=10
hora = datetime.now()
hora = str(hora.strftime("%Y-%m-%d %H:%M:%S"))
def refrescar_tiempo_transcurrido():
    hora = datetime.now()
    hora = str(hora.strftime("%Y-%m-%d %H:%M:%S"))
    horita.set(hora)
    ventana.after(1, refrescar_tiempo_transcurrido)

def leerboleta():
    ruta = "Banco/num.txt"
    archivonum = open(ruta,"r")
    newnum = int(archivonum.readline())+1
    archivonum.close()
    
    archivonum2 = open(ruta,"w")
    if newnum < 10:
        newnum2 = "F00"+(str(newnum))
    elif newnum < 100:
        newnum2 = "F0"+(str(newnum))
    facnumero.set(newnum2)
    archivonum2.write(str(newnum))
    archivonum2.close()
def calcular():
    global ttotal
    ttotal=0
    for child in tv.get_children():
        ttotal = float(tv.item(child,'values')[3]) + ttotal
        print(tv.get_children())
    subtotal.set(ttotal)
    igv.set(round(ttotal*0.18,3))
    total.set(round((subtotal.get()+igv.get()),3))
    print("calcular")
def guardar():
    ruta = "Banco/FACTURACAB.txt"
    print(ruta)
    archivo = open(ruta,"a")
    hora = datetime.now()
    hora = str(hora.strftime("%Y-%m-%d %H:%M:%S"))
    #archivo = open("Banco/boletas.txt,"a")
    sep="-"
    facturacab=facnumero.get()+sep+bolserie.get()+sep+ruc.get()+sep+empresa.get()+sep+str(subtotal.get())+sep+str(igv.get())+sep+str(total.get())+sep+hora
    archivo.write(facturacab+"\n")

    ruta = "Banco/FACTURADET.txt"
    print(ruta)
    archivo = open(ruta,"a")
    #archivo = open("Banco/boletas.txt,"a")
    for child in tv.get_children():
        facturacab=facnumero.get()+sep+bolserie.get()+sep+tv.item(child,'values')[1]+sep+tv.item(child,'values')[0]+sep+tv.item(child,'values')[2]+sep+tv.item(child,'values')[3]
        archivo.write(facturacab+"\n")
    
    leerboleta()
def agregar():
    global posicion
    global importe
    importe=cantidad.get()*preciou.get()
    tv.insert(parent='',index=posicion,iid=posicion,text='',values=(cantidad.get(),articulo.get(),preciou.get(),importe))
    posicion=posicion+1
    print("agregar")

ventana = Tk()
ventana.title("SISTEMA DE VENTAS")
ventana.geometry("800x500")

bolserie=StringVar()
facnumero=StringVar()
cantidad=IntVar()
articulo=StringVar()
preciou=DoubleVar()
subtotal=DoubleVar()
igv=DoubleVar()
total=DoubleVar()
ruc=StringVar()
empresa=StringVar()
direccion=StringVar()
distrito=StringVar()
horita=StringVar()


lblboleta=Label(ventana,text="Factura:").place(x=500 ,y=50 )
lblboleta=Label(ventana,text="SISTEMA DE VENTANAS").place(x=200,y=20)
txtboleta=Entry(ventana,textvariable=facnumero).place(x=560,y=50)
bolserie.set(numcorrelativa)

txtboleta2=Entry(ventana,textvariable=bolserie).place(x=660,y=50)

lblboleta=Label(ventana,text="RUC").place(x=50, y=60)
lblboleta=Label(ventana,text="EMPRESA").place(x=50, y=90)
lblboleta=Label(ventana,text=hora,textvariable=horita)
lblboleta.place(x=50, y=130)
#lblboleta=Label(ventana,text="DISTRITO").place(x=350, y=130)
lblboleta=Label(ventana,text="CANTIDAD          ARTICULO           PRECIOUNIT").place(x=120, y=150)

lblboleta=Label(ventana,text="SUBTOTAL:").place(x=520, y=350)
lblboleta=Label(ventana,text="IGV:").place(x=520, y=380)
lblboleta=Label(ventana,text="TOTAL:").place(x=520, y=410)

txtboleta=Entry(ventana,textvariable=ruc).place(x=150,y=60)
txtboleta=Entry(ventana,textvariable=empresa).place(x=150,y=90)
#txtboleta=Entry(ventana,textvariable=direccion).place(x=150,y=130)
#txtboleta=Entry(ventana,textvariable=distrito).place(x=450,y=130)

txtboleta=Entry(ventana,textvariable=subtotal).place(x=600,y=350)
txtboleta=Entry(ventana,textvariable=igv).place(x=600,y=380)
txtboleta=Entry(ventana,textvariable=total).place(x=600,y=410)

txtboleta=Entry(ventana,textvariable=cantidad).place(x=120,y=170)
txtboleta=Entry(ventana,textvariable=articulo).place(x=220,y=170)
txtboleta=Entry(ventana,textvariable=preciou).place(x=350,y=170)

bntguardar=Button(ventana, text="Agregar",command=agregar).place(x=50, y=170)
bntguardar=Button(ventana, text="Guardar",command=guardar).place(x=50, y=350)
bntguardar=Button(ventana, text="Calcular",command=calcular).place(x=50, y=450)

tv=ttk.Treeview(ventana)
tv["columns"]=("CANTIDAD","ARTICULO","PRECIOUNIT","IMPORTE")
tv.column("#0",width=0,stretch=NO)
tv.column("CANTIDAD",anchor=CENTER, width=100)
tv.column("ARTICULO",anchor=CENTER, width=100)
tv.column("PRECIOUNIT",anchor=CENTER, width=100)
tv.column("IMPORTE",anchor=CENTER, width=100)

tv.heading("#0",text="",anchor=CENTER)
tv.heading("CANTIDAD",text="CANTIDAD",anchor=CENTER)
tv.heading("ARTICULO",text="ARTICULO",anchor=CENTER)
tv.heading("PRECIOUNIT",text="PRECIOUNIT",anchor=CENTER)
tv.heading("IMPORTE",text="IMPORTE",anchor=CENTER)

tv.place(x=100,y=210)
leerboleta()
refrescar_tiempo_transcurrido()
ventana.mainloop()
