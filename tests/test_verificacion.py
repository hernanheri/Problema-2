import unittest
from src.verificacion import verificar_suma

class TestVerificarSuma(unittest.TestCase):
    def test_suma_igual_tercero(self):
        # Casos donde la suma de dos números es igual al tercero
        self.assertTrue(verificar_suma(2, 3, 5))
        self.assertTrue(verificar_suma(5, 3, 2))
        self.assertTrue(verificar_suma(10, 15, 25))
    
    def test_suma_no_igual_tercero(self):
        # Casos donde la suma de dos números no es igual al tercero
        self.assertFalse(verificar_suma(1, 2, 4))
        self.assertFalse(verificar_suma(5, 5, 1))
        self.assertFalse(verificar_suma(7, 9, 3))

if __name__ == "__main__":
    unittest.main()
