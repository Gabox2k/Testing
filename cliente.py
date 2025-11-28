import socket
import threading
import time 

#Recibir el mensaje del servidor 
def recibir(cliente):
    while True:
        try:
            mensaje= cliente.recv(1024).decode()
            if not mensaje:
                break
            print(mensaje)
        except:
            break

#Enviar el mensaje a otra persona
def enviar(cliente):
    while True:
        try:
            mensaje = input()
            if mensaje.lower ()== 'salir':
                cliente.close()
                break
            cliente.send(mensaje.encode())
        except:
            break
    

#Conectar con el servidor 
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conectar_servidor():
    for intento in range(3):
        try:
            cliente.connect(("localhost", 8000))
            print("Conectado con el servidor")
            return 
        except:
            print(f"Se esta intentando conectar con el servidor {intento +1}/3")
            time.sleep(1)
    else:
        print("No se pudo conectar con el servidor")
        exit()

conectar_servidor()

nombre = input("Nombre: ")
cliente.send(nombre.encode())

#Reicibir y enviar los mensajes 
threading.Thread(target=recibir, args=(cliente,)).start()
threading.Thread(target=enviar, args=(cliente,)).start()
