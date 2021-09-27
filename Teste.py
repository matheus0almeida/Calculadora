import unittest

class TESTES(unittest.TestCase):    
    
    def test_soma(self):
        resultado=1+2
        self.assertEqual(3,resultado)

    def test_sub(self):
        resultado=5-3
        self.assertEqual(2,resultado)

    def test_mult(self):
        resultado=5*3
        self.assertEqual(15,resultado)

    def test_div(self):
        resultado=21/3
        self.assertEqual(7,resultado)

    def test_div_por_0(self):
        divisor=0
        self.assertIsNot(0,divisor)


if __name__ == '__main__':
    unittest.main()