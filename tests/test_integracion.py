import socket
import threading
import time

host = "localhost"
port = 8000

def crear_cliente(nombre):
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, port))
    c.send(nombre.encode())
    
    return c

def recibir_mensajes(cliente, recibidos):
    while True:
        try:
            msg = cliente.recv(1024).decode()
            if not msg:
                break
            recibidos.append(msg)
        except:
            break
        
def multiple_conexiones():
    c1 = crear_cliente("pedro")
    mensaje1= []
    threading.Thread(target=recibir_mensajes, args=(c1, mensaje1), daemon=True).start()
    
    c2= crear_cliente("juan")
    mensaje2 = []
    threading.Thread(target=recibir_mensajes, args=(c2, mensaje2), daemon=True).start()
    
    c1.send("hola juan".encode())
    
    time.sleep(0.5)

    assert all ("pedro" in m for m in mensaje2)
    assert len(mensaje1) == 0
    
    c1.close()
    c2.close()
    
    def test_desconexion():
        c1= crear_cliente("pedro")
        c2= crear_cliente("luis")
        
        mensaje_c2 = []
        threading.Thread(target=recibir_mensajes, args=(c2, mensaje_c2), daemon=True).start()

        c1.close()
        
        c2.send("se cerro".encode())
        
        time.sleep(0.3)
        
        assert len(mensaje_c2) >= 0
        
        c2.close()