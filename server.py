from xmlrpc.server import SimpleXMLRPCServer
from Reporte import Reporte
from Robot import Robot
import os
import sys

import asyncio
import websockets
import random
import json
from time import sleep

# web socket antes de return art1 2 3
# open close en actv desact escritura en art1 2 3 pin para vic graficas

robot = Robot()
reportes = Reporte()
f = open("build/graficas.txt", "w")


class websckt():
    def __init__(self):
        self.socket = 0


web = websckt()


def get_robot_status():
    payload = {
        "art_1": robot.vinculo1.get_posicion(),
        "art_2": robot.vinculo2.get_posicion(),
        "art_3": robot.vinculo3.get_posicion(),
        "pinza": robot.efector.get_estado()
    }
    print(payload)
    return payload


def actv(n):
    robot.activar()
    return 1


def desactv(n):
    robot.desactivar()
    f.close()
    os.system('cd build && ./graficar')
    return 0


async def art1(n):
    if(robot.get_estado() == True):
        robot.vinculo1.set_posicion(n)
        reportes.add_reporte("art1:"+str(robot.vinculo1.get_posicion()))
        articulaciones = [int(robot.vinculo1.get_posicion()), int(
            robot.vinculo2.get_posicion()), int(robot.vinculo3.get_posicion())]
        await f.write(str(articulaciones)+"\n")
        await web.socket.send(json.dumps(get_robot_status(), ensure_ascii=False))
        return articulaciones
    else:
        return "El robot esta desactivado"


async def art2(n):
    if(robot.get_estado() == True):
        robot.vinculo2.set_posicion(n)
        reportes.add_reporte("art2:"+str(robot.vinculo2.get_posicion()))
        articulaciones = [int(robot.vinculo1.get_posicion()), int(
            robot.vinculo2.get_posicion()), int(robot.vinculo3.get_posicion())]
        await f.writelines(str(articulaciones)+"\n")
        await web.socket.send(json.dumps(get_robot_status(), ensure_ascii=False))
        return articulaciones
    else:
        return "El robot esta desactivado"


async def art3(n):
    if(robot.get_estado() == True):
        robot.vinculo3.set_posicion(n)
        reportes.add_reporte("art3:"+str(robot.vinculo3.get_posicion()))
        articulaciones = [int(robot.vinculo1.get_posicion()), int(
            robot.vinculo2.get_posicion()), int(robot.vinculo3.get_posicion())]
        await f.writelines(str(articulaciones)+"\n")
        await web.socket.send(json.dumps(get_robot_status(), ensure_ascii=False))
        return articulaciones
    else:
        return "El robot esta desactivado"


async def hom(n):
    if(robot.get_estado() == True):
        robot.vinculo1.set_posicion(0)
        robot.vinculo2.set_posicion(0)
        robot.vinculo3.set_posicion(0)
        reportes.add_reporte("hom:"+str(0))
        articulaciones = [int(robot.vinculo1.get_posicion()), int(
            robot.vinculo2.get_posicion()), int(robot.vinculo3.get_posicion())]
        await web.socket.send(json.dumps(get_robot_status(), ensure_ascii=False))
        return articulaciones
    else:
        return "El robot esta desactivado"


async def efec(n):
    if(robot.get_estado() == True):
        if (n == 0):
            robot.efector.cerrar()
            devuelve = "pinza esta cerrada (" + \
                str(robot.efector.get_estado())+")"

        if (n == 1):
            robot.efector.abrir()
            devuelve = "pinza esta abierta (" + \
                str(robot.efector.get_estado())+")"

        reportes.add_reporte("pin:"+str(n))
        await web.socket.send(json.dumps(get_robot_status(), ensure_ascii=False))
        # articulaciones=[robot.vinculo1.get_posicion(),robot.vinculo2.get_posicion(),robot.vinculo3.get_posicion()]
        return devuelve
    else:
        return "El robot esta desactivado"


def rep(n):
    aux2 = ""

    for aux in reportes.get_reporte():
        aux2 = aux2+aux+"\n"

    return aux2


async def server(websocket, path):
    web.socket = websocket
    server = SimpleXMLRPCServer(("localhost", 8080))
    print("Listening on port 8080...")
    name = input("si no tiene archivo aprete enter, sino ingrese su nombre: ")
    if(name != ""):
        aut = open(name)
        n = 0
        for linea in aut:
            linea = linea.rstrip("\n\r")
            print(linea)
            palabras = linea.split(" ")
            if(palabras[0] == "actv"):
                print(actv(n))
            if(palabras[0] == "desactv"):
                print(await desactv(n))
            if(palabras[0] == "art1"):
                n = float(palabras[1])
                print(await art1(n))
            if(palabras[0] == "art2"):
                n = float(palabras[1])
                print(await art2(n))
            if(palabras[0] == "art3"):
                n = float(palabras[1])
                print(await art3(n))
            if(palabras[0] == "pin"):
                n = float(palabras[1])
                print(await efec(n))
            if(palabras[0] == "hom"):
                print(await hom(n))
            if(palabras[0] == "rep"):
                print(rep(n))
            sleep(5 + random.random() * 5)

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


start_server = websockets.serve(server, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
