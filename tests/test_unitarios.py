import pytest
from utils import validar_mensaje

def test_mensaje_valido():
    assert validar_mensaje("hhh") == True
    
def test_mensaje_vacio():
    assert validar_mensaje("") == False

def test_mensaje_espacios():
    assert validar_mensaje(" ") == False
    
def test_mensaje_none():
    assert validar_mensaje(None) == False
    
