import socket
import threading

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Dirrecion IPV4 , Conexion TCP
servidor.bind(("localhost", 8000))
servidor.listen(5)
servidor_act = True

clientes = []

#Mensajes de los clientes
def recibir(conexion, nombre):
    while True:
        try:
            mensaje = conexion.recv(1024).decode()
            if not mensaje:
                break
            for c, _ in clientes:
                if c!= conexion:
                    c.send(f"{nombre}: {mensaje}".encode())
        except:
            break
        
    #Quitar al cliente
    conexion.close()
    clientes.remove((conexion,nombre))
    print(f"{nombre} se desconecto")
    
#Por donde se conecto
def cliente(conexion,direccion):
    nombre = conexion.recv(1024).decode()
    print(f"{nombre} se conecto desde la {direccion}")
    clientes.append((conexion,nombre))
    
    hilo = threading.Thread(target=recibir, args=(conexion,nombre))
    hilo.start()
    

#Para que el cliente se conecte 
def conexiones():
    while True:
        try:
            conexion , direccion = servidor.accept()
            threading.Thread(target=cliente, args=(conexion,direccion)).start()
        except:
            break
        
    

print("Servidor iniciado en el puerto 8000. Escribe salir para cerrar el servidor")

#Esperara nuevos clientes 
hilo_conexiones = threading.Thread(target= conexiones)
hilo_conexiones.start()

#Cierre del servidor 
while True:
    letra = input()
    if letra.lower() == 'salir':
        servidor_act = False
        servidor.close()
        print("Servidor cerrado")
        for conexion, nombre in clientes:
            try:
                conexion.send("El servidor se a cerrado".encode())
                conexion.close()
            except:
                pass
        break
            