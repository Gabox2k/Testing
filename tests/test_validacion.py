from utils import validar_mensaje

#Validacion de mensajes largos 
def test_no_mensajes_largos():
    mensaje = "s" * 200
    
    assert validar_mensaje(mensaje) == False
    
    