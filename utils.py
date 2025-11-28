def validar_mensaje(mensaje ):

    if mensaje is None:
        return False
    if len(mensaje.strip()) == 0:
        return False
    
    return True   