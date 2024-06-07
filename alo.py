import os
import msvcrt
import csv

#funcion para crear titulos
def titulo(texto:str):
    print(f"{texto.upper()}")
def error(texto:str):
    print(f"{texto.upper()}")
def exito(texto:str):
    print(f"{texto.upper()}")
#tuplas-clases
clases=[("Pesas","LUN-MIE 8:30-10:00 a.m",10),
        ("Zumba","MAR-JUE 3:30-5:40 p.m",20),
        ("Nutricion","VIE 6:00-7:30 a.m",2),
        ("Crossfit","SAB 11:30-12:55 p.m",10)]
#diccionario - usuarios
usuarios={}
#listas - reservas
reservas=[]
#contador id
numero_usuario=100
#comenzamos el sistema
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")

    print("""
          sistema de gestion fitlife
          ═══════════════════════════
          1) Registrar usuario
          2) Reservar clase
          3) Consultar clases disponibles
          4) Consultar clases de usuario
          5) Consultar usuarios
          0) Salir""")
    opcion=int(input("Seleccione: "))
    if opcion==0:
        titulo("Adios")
        break
    elif opcion==1:
        titulo("Registrar usuario")
        nombre=input("Ingrese nombre de usuario: ").title()
        #validar que nombre de usuario no se repite
        if nombre not in usuarios.values():
            usuarios[numero_usuario]=nombre
            exito(f" Usuario {numero_usuario} registrado")
            numero_usuario+=100
        else:
            error("Usuario ya registrado")
    elif opcion==2:
        titulo("Reservar clase")
        codigo=int(input("Ingrese codigo de usuario: "))
        if codigo in usuarios:
            curso=input("Ingrese curso para inscribir: ").capitalize()
            centinelacurso=False
            centinelacupos=False
            for c in clases:
                if c[0].capitalize()==curso:
                    centinelacurso=True
                    if c[2]>0: #veridicamos si hay cupos
                        centinelacupos=True
                        #realizar la reserva
                        reservas.append(codigo, usuarios[codigo],c[0],c[1])
                        exito("Reserva realizada")
                        #descontar cupo
                        actualizacioncupo=(c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacioncupo)
                        with open('reporte_reservas.csv','w',newline='',encoding='utf-8') as a:
                            escribir=csv.writer(a,delimiter=",")
                            escribir.writerows(reservas)
                        break
            if not centinelacurso:
                error("Curso inexistente")
            if not centinelacupos:
                error("No hay cupos disponibles")
        else:
            error("Codigo no exite")
    elif opcion==3:
        titulo("consultar clases disponibles")
        for c in clases:
            print(f"{c[0]} Horario: {c[1]} Cupos: {c[2]}")
    elif opcion==4:
        titulo("consultar clases de usuario")
        if len(reservas)>0:
            codigo=int(input("ingrese codigo de usuario: "))
            centinela=False
            for r in reservas:
                if r[0]==codigo:
                    print(f"{r[0]} {r[1]} {r[2]} {r[3]}")
                    centinela=True
            if centinela==False:
                error("El codigo no tiene reservas asociadas")
        else:
            error("No existen reservas")
    elif opcion==5:
        titulo("consultar usuarios")
        if len(usuarios)>0:
            for u in usuarios:
                print(f"{u}: {usuarios[u]}")
        else:
            error("No hay usuarios registrados")