from xmlrpc.server import SimpleXMLRPCServer
from Reporte import Reporte
reportes=Reporte()
from Robot import Robot
robot=Robot()
import os
f=open("build/graficas.txt","w")
import sys
# web socket antes de return art1 2 3
# open close en actv desact escritura en art1 2 3 pin para vic graficas
def actv(n):
    robot.activar()
    return 1

def desactv(n):
    robot.desactivar()
    f.close()
    os.system('cd build && ./graficar')
    return 0

def art1(n):
    if(robot.get_estado()==True):
        robot.vinculo1.set_posicion(n)
        reportes.add_reporte("art1:"+str(robot.vinculo1.get_posicion()))
        articulaciones=[int(robot.vinculo1.get_posicion()),int(robot.vinculo2.get_posicion()),int(robot.vinculo3.get_posicion())]
        f.write(str(articulaciones)+"\n")
        return articulaciones
    else:
        return "El robot esta desactivado"
def art2(n):
    if(robot.get_estado()==True):
        robot.vinculo2.set_posicion(n)
        reportes.add_reporte("art2:"+str(robot.vinculo2.get_posicion()))
        articulaciones=[int(robot.vinculo1.get_posicion()),int(robot.vinculo2.get_posicion()),int(robot.vinculo3.get_posicion())]
        f.writelines(str(articulaciones)+"\n")
        return articulaciones
    else:
        return "El robot esta desactivado"
def art3(n):
    if(robot.get_estado()==True):
        robot.vinculo3.set_posicion(n)
        reportes.add_reporte("art3:"+str(robot.vinculo3.get_posicion()))
        articulaciones=[int(robot.vinculo1.get_posicion()),int(robot.vinculo2.get_posicion()),int(robot.vinculo3.get_posicion())]
        f.writelines(str(articulaciones)+"\n")
        return articulaciones
    else:
        return "El robot esta desactivado"

def hom(n):
    if(robot.get_estado()==True):
        robot.vinculo1.set_posicion(0)
        robot.vinculo2.set_posicion(0)
        robot.vinculo3.set_posicion(0)
        reportes.add_reporte("hom:"+str(0))
        articulaciones=[int(robot.vinculo1.get_posicion()),int(robot.vinculo2.get_posicion()),int(robot.vinculo3.get_posicion())]
        return articulaciones
    else:
        return "El robot esta desactivado"

def efec(n):
    if(robot.get_estado()==True):
        if (n==0):
            robot.efector.cerrar()
            devuelve="pinza esta cerrada ("+str(robot.efector.get_estado())+")"
        
        if (n==1):
            robot.efector.abrir()
            devuelve="pinza esta abierta ("+str(robot.efector.get_estado())+")"
        
        reportes.add_reporte("pin:"+str(n))
        # articulaciones=[robot.vinculo1.get_posicion(),robot.vinculo2.get_posicion(),robot.vinculo3.get_posicion()]
        return devuelve
    else:
        return "El robot esta desactivado"
def rep(n):
    aux2=""

    for aux in reportes.get_reporte():
        aux2=aux2+aux+"\n"
    
    return aux2 

server = SimpleXMLRPCServer(("localhost", 8080))
print("Listening on port 8080...")
name=input("si no tiene archivo aprete enter, sino ingrese su nombre: ")
if(name!=""):
    aut = open(name)
    n=0
    for linea in aut:
        linea=linea.rstrip("\n\r")
        print(linea)
        palabras=linea.split(" ")
        if(palabras[0]=="actv"):
            print(actv(n))
        if(palabras[0]=="desactv"):
            print(desactv(n))
        if(palabras[0]=="art1"):
            n=float(palabras[1])
            print(art1(n))
        if(palabras[0]=="art2"):
            n=float(palabras[1])
            print(art2(n))
        if(palabras[0]=="art3"):
            n=float(palabras[1])
            print(art3(n))
        if(palabras[0]=="pin"):
            n=float(palabras[1])
            print(efec(n))
        if(palabras[0]=="hom"):
            print(hom(n))
        if(palabras[0]=="rep"):
            print(rep(n))
    print("La carga automatica ha finalizado... Por favor Reinicie")
    sys.exit(0)    
server.register_function(art1, "art1")
server.register_function(art2, "art2")
server.register_function(art3, "art3")
server.register_function(efec, "efec")
server.register_function(rep, "rep")
server.register_function(actv, "actv")
server.register_function(desactv, "desactv")
server.register_function(hom, "hom")

server.serve_forever()
