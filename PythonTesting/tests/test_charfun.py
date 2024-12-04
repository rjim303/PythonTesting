import unittest
from app.scripts.charfun import esPalindromo

class TestPalindromo(unittest.TestCase):

    def test_palindromo_con_espacios(self):
        # Prueba un palíndromo con espacios
        self.assertTrue(esPalindromo("A man a plan a canal Panama"))  

    def test_palindromo_con_assertEqual(self):
        # Verifica si la cadena es un palíndromo y usa assertEqual para comparar el resultado
        self.assertEqual(esPalindromo("Anita lava la tina"), True)

    def test_no_palindromo(self):
        # Prueba con una cadena que no es palíndroma
        self.assertFalse(esPalindromo("hello"))

    def test_palindromo_muy_largo(self):
        # Prueba un palíndromo con una cadena muy larga
        self.assertTrue(esPalindromo("A" * 10000 + "B" + "A" * 10000)) 

    def test_palindromo_vacio(self):
        # Prueba con una cadena vacía
        self.assertTrue(esPalindromo(""))

    def test_palindromo_con_caracteres_no_alfanumericos(self):
        # Prueba con una cadena que contiene caracteres no alfanuméricos
        self.assertTrue(esPalindromo("!A man, a plan, a canal: Panama!"))

if __name__ == "__main__":
    unittest.main()