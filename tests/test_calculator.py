# test_calculator.py
import pytest
from calculator import addition, multiplication

def test_addition():
    """Vérifie que l'addition fonctionne correctement"""
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_multiplication():
    """Vérifie que la multiplication fonctionne correctement"""
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 3) == -6
    assert multiplication(5, 0) == 0