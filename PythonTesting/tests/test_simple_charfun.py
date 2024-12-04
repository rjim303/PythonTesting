import unittest
from app.scripts.charfun import esPalindromo

class TestPalindromoSimple(unittest.TestCase):

    def test_palindromo(self):
        # Prueba un palíndromo básico
        self.assertTrue(esPalindromo("radar")) 

if __name__ == "__main__":
    unittest.main()