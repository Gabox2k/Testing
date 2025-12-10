import pytest
from utils import validar_mensaje

#validacion de mensaje
def test_mensaje_valido():
    assert validar_mensaje("hola") == True

#validacion de mensaje vacio   
def test_mensaje_vacio():
    assert validar_mensaje("") == False

#validacion con espacios
def test_mensaje_espacios():
    assert validar_mensaje(" ") == False

#validacion de solo espacios    
def test_mensaje_none():
    assert validar_mensaje(None) == False
    
