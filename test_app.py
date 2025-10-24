import pytest
from app import sumar, restar, dividir

def test_sumar_correcto():
    assert sumar(2, 2) == 5   # ✅ correcta

def test_restar_error():
    assert restar(5, 2) == 10  # ❌ error intencional

def test_dividir_todos_errores():
    assert dividir(10, 2) == 6  # 💥 error intencional
    assert dividir(5, 0) == 0   # 💥 otro error por dividir entre cero