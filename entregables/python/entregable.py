from tkinter import *
from tkinter.ttk import Combobox, Separator
from tkinter import messagebox
from tkinter import ttk
root=Tk()
root.geometry("800x600")
root.title("Ferreteria el tornillo feliz")
root.configure(bg='white')
nombre=StringVar()
apellido=StringVar()
dni=StringVar()
direccion=StringVar()
celular=StringVar()

listado={"Martillo":10.0,
        "Alicate":8.50,
        "Cemento":24,
        "Ladrillo":8.50,
        "Clavos":1,
        "Yeso":3.50,
        "Perno":2,
        "Desarmador":5,
        "Foco":15,
        "Enchufe":3.50,
        "Tubo PVC":12}


cod1=StringVar()
cod2=StringVar()
cod3=StringVar()

descr1=StringVar()
descr2=StringVar()
descr3=StringVar()

unidad1=IntVar()
unidad2=IntVar()
unidad3=IntVar()


precio1=DoubleVar()
precio2=DoubleVar()
precio3=DoubleVar()

subtotal1=StringVar()
subtotal2=StringVar()
subtotal3=StringVar()
subtotal=StringVar()
global lst_nombre,lst_telefono,lst_pago,lst_producto
lst_nombre=[]
lst_apellido=[]
lst_dni=[]
lst_direccion=[]
lst_telefono=[]
lst_pago=[]
lst_producto=[]

def registrar():
    global subtotal,subtotal1,subtotal2,subtotal3
    lst_nombre.append(nombre.get())
    lst_dni.append(dni.get())
    lst_apellido.append(apellido.get())
    lst_direccion.append(direccion.get())
    lst_telefono.append(celular.get())
    
    subtotal1=unidad1.get()*listado.get(descr1.get())
    subtotal2=unidad2.get()*listado.get(descr2.get())
    subtotal3=unidad3.get()*listado.get(descr3.get())
    subtotal=subtotal1+subtotal2+subtotal3
    lst_pago.append(subtotal)
    #labels
    global x,y,z
    x=Label(root,text="s/."+str(listado.get(descr1.get())),bg="#fff")
    x.place(x=450,y=360,width=80)
    y=Label(root,text="s/."+str(listado.get(descr2.get())),bg="#fff")
    y.place(x=450,y=390,width=80)
    z=Label(root,text="s/."+str(listado.get(descr3.get())),bg="#fff")
    z.place(x=450,y=420,width=80)
    global lblsub1,lblsub2,lblsub3,lblresultado
    lblsub1=Label(root,text="s/."+str(subtotal1),bg="#fff")
    lblsub1.place(x=560,y=360)
    lblsub2=Label(root,text="s/."+str(subtotal2),bg="#fff")
    lblsub2.place(x=560,y=390)
    lblsub3=Label(root,text="s/."+str(subtotal3),bg="#fff")
    lblsub3.place(x=560,y=420)
    
    lblresultado=Label(root,text="El total es: "+str(subtotal),bg="#fff",font=("Curier 10"))
    lblresultado.place(x=650,y=500)
    
    #obtener del diccionario == listado.get(descr3.get())
def imprimir():
    ventana = Tk()
    ventana.geometry("500x400")
    
    titulo=Label(ventana,text="BOLETA DE PAGO",font=("Curier 20")).pack()
    Label(ventana,text="Nombre y Apellido:",font=("Curier 11")).place(x=50,y=50)
    Label(ventana,text=nombre.get()+" "+apellido.get(),font=("Curier 11")).place(x=190,y=50)
    Label(ventana,text="Dirección: ",font=("Curier 11")).place(x=50,y=90)
    Label(ventana,text=direccion.get(),font=("Curier 11")).place(x=190,y=90)
    Label(ventana,text="Descripcion",font=("Curier 9")).place(x=100,y=150)
    Label(ventana,text=descr1.get(),font=("Curier 9")).place(x=100,y=180)
    Label(ventana,text=descr2.get(),font=("Curier 9")).place(x=100,y=210)
    Label(ventana,text=descr3.get(),font=("Curier 9")).place(x=100,y=240)
    Label(ventana,text="Cantidad",font=("Curier 9")).place(x=200,y=150)
    Label(ventana,text=unidad1.get(),font=("Curier 9")).place(x=200,y=180)
    Label(ventana,text=unidad2.get(),font=("Curier 9")).place(x=200,y=210)
    Label(ventana,text=unidad3.get(),font=("Curier 9")).place(x=200,y=240)
    Label(ventana,text="P.Unitario",font=("Curier 9")).place(x=280,y=150)
    Label(ventana,text=listado.get(descr1.get()),font=("Curier 9")).place(x=280,y=180)
    Label(ventana,text=listado.get(descr2.get()),font=("Curier 9")).place(x=280,y=210)
    Label(ventana,text=listado.get(descr3.get()),font=("Curier 9")).place(x=280,y=240)
    Label(ventana,text="Valor de venta",font=("Curier 9")).place(x=360,y=150)
    Label(ventana,text=subtotal1,font=("Curier 9")).place(x=360,y=180)
    Label(ventana,text=subtotal2,font=("Curier 9")).place(x=360,y=210)
    Label(ventana,text=subtotal3,font=("Curier 9")).place(x=360,y=240)
    Label(ventana,text="Total a pagar",font=("Curier 9")).place(x=240,y=350)
    Label(ventana,text="s/."+str(subtotal),font=("Curier 9")).place(x=360,y=350)
    ventana.mainloop()

def limpiar():
    dni.set("")
    apellido.set("")
    nombre.set("")
    direccion.set("")
    celular.set("")
    cod1.set("")
    cod2.set("")
    cod3.set("")
    descr1.set("")
    descr2.set("")
    descr3.set("")
    unidad1.set(0)
    unidad2.set(0)
    unidad3.set(0)
    x["text"]=""
    y["text"]=""
    z["text"]=""
    lblsub1["text"]=""
    lblsub2["text"]=""
    lblsub3["text"]=""
    lblresultado["text"]=""
def registro():
    ws=Tk()
    ws.title('Cuadro Datos')
    ws.geometry('800x600')
    ws['bg']='#fb0'
    tv=ttk.Treeview(ws)
    Label(ws,text="Registro de clientes",font=("Curier 20"),bg="#fb0").pack()
    tv['columns']=('Nombre','DNI','Total de pago','Telefono')
    tv.column('#0',width=0,stretch=NO)
    tv.column('Nombre',anchor=CENTER,width=200)
    tv.column('DNI',anchor=CENTER,width=200)
    tv.column('Total de pago',anchor=CENTER,width=200)
    tv.column('Telefono',anchor=CENTER,width=200)

    tv.heading('#0',text='',anchor=CENTER)
    tv.heading('Nombre',text='Nombre',anchor=CENTER)
    tv.heading('DNI',text='DNI',anchor=CENTER)
    tv.heading('Total de pago',text='Total de pago',anchor=CENTER)
    tv.heading('Telefono',text='Telefono',anchor=CENTER)
    i=0
    elementos=len(lst_nombre)
    while i<elementos:
        tv.insert(parent='',index=i,iid=i,text='',values=(lst_nombre[i],lst_dni[i],lst_pago[i],lst_telefono[i]))
        i+=1    
    tv.place(y=150)
    ws.mainloop()
#############################################################
#barra menu 
menuBar=Menu(root)
root.config(menu=menuBar)

def cerrar():
    messagebox.askquestion("Cerrar", message="¿Estas seguro?")
def version():
    messagebox.showinfo("Version", message="Version 2.0")
def error():
    messagebox.showerror("Error critico", message="Se encontro un error fatal")
def atencion():
    messagebox.showwarning("Atencion", message="Se borrara actual")
archivoMenu=Menu(menuBar,tearoff=0)

archivoMenu.add_command(label="Registro",command=registro)
archivoMenu.add_command(label="Abrir", command=atencion)
archivoMenu.add_command(label="Guardar", command=error)
archivoMenu.add_command(label="Imprimir",command=imprimir)
#separar salir de las demas
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=root.quit)

editMenu= Menu(menuBar,tearoff=0)
editMenu.add_command(label='Cortar')
editMenu.add_command(label='Copiar')
editMenu.add_command(label='Pegar')

ayudaMenu=Menu(menuBar,tearoff=0)
ayudaMenu.add_command(label="Ayuda",command=version)
ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editMenu)
menuBar.add_cascade(label="Ayuda",menu=ayudaMenu)
######################################################

lbltitulo=Label(root,text="Ferreteria El Tornillo Feliz",font=("Curier 15"),bg='white').pack()
separador=Separator(root,orient="horizontal")
separador.pack(fill='x')
lbldni=Label(root,text="DNI: ",font=("Curier 12"),bg="#fff").place(x=120,y=70)
etiqueta_dni=Entry(root,textvariable=dni,relief="solid",font=("Curier 12")).place(x=200,y=70,width=200,height=25)

lblapellido=Label(root,text="Apellido:",font=("Curier 12"),bg="#fff").place(x=120,y=110)
etiqueta_a =Entry(root,textvariable=apellido,relief="solid",font=("Curier 12")).place(x=200,y=110,width=200,height=25)

lblnombre=Label(root,text="Nombre:",font=("Curier 12"),bg="#fff").place(x=120,y=150)
etiqueta_nombre=Entry(root,textvariable=nombre,relief="solid",font=("Curier 12")).place(x=200,y=150,width=200,height=25)

lbldireccion=Label(root,text="Dirección:",font=("Curier 12"),bg="#fff").place(x=120,y=190)
etiqueta_direccion=Entry(root,textvariable=direccion,relief="solid",font=("Curier 12")).place(x=200,y=190,width=300,height=25)

lblfono=Label(root,text="Celular:",font=("Curier 12"),bg="#fff").place(x=120,y=230)
etiqueta_fono=Entry(root,textvariable=celular,relief="solid",font=("Curier 12")).place(x=200,y=230,width=100,height=25)

#botones
btnregistrar=Button(root,text="Registrar",command=registrar,bg='#49A',fg="#fff",relief='flat',font=("Arial 11")).place(x=300,y=480,width=120,height=30)
#btnimp=Button(root,text="Imprimir",command=imprimir,bg='#49A',fg="#fff",relief='flat',font=("Arial 10")).place(x=590,y=550,width=80,height=30)
btnlimpiar=Button(root,text="Nuevo",command=limpiar,bg='#49A',fg="#fff",relief='flat',font=("Arial 10")).place(x=480,y=550,width=80,height=30)


#combobox

lbldesc=Label(root,text="Descripción",bg="#fff").place(x=230,y=330)
txtdes1=Combobox(root,textvariable=descr1)
txtdes1.place(x=210,y=360,width=90)
txtdes1['values']=("-","Alicate","Cemento","Ladrillo","Clavos","Yeso","Perno","Desarmador","Foco","Enchufe","Tubo PVC")
txtdes2=Combobox(root,textvariable=descr2)
txtdes2.place(x=210,y=390,width=90)
txtdes2["values"]=("-","Alicate","Cemento","Ladrillo","Clavos","Yeso","Perno","Desarmador","Foco","Enchufe","Tubo PVC")
txtdes3=Combobox(root,textvariable=descr3)
txtdes3.place(x=210,y=420,width=90)
txtdes3["values"]=("-","Alicate","Cemento","Ladrillo","Clavos","Yeso","Perno","Desarmador","Foco","Enchufe","Tubo PVC")


lblunidad=Label(root,text="Cantidad",bg="#fff").place(x=340,y=330)
txtuni1=Entry(root,textvariable=unidad1).place(x=340,y=360,width=80)
txtuni2=Entry(root,textvariable=unidad2).place(x=340,y=390,width=80)
txtuni3=Entry(root,textvariable=unidad3).place(x=340,y=420,width=80)

lblprecio=Label(root,text="Precio Unitario",bg="#fff").place(x=450,y=330)
txtprecio1=Label(root,textvariable=precio1,bg="#fff").place(x=450,y=360,width=80)
txtprecio2=Label(root,textvariable=precio2,bg="#fff").place(x=450,y=390,width=80)
txtprecio3=Label(root,textvariable=precio3,bg="#fff").place(x=450,y=420,width=80)

lblsubtotal=Label(root,text="Subtotal",bg="#fff").place(x=560,y=330)



root.mainloop()