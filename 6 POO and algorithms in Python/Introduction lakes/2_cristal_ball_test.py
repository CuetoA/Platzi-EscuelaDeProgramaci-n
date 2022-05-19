import unittest

def suma(n1):
    if (n1 >= 18):
        return False
    else:
        return False


class CajaNegraTest(unittest.TestCase):
    
    def test_mayor_de_edad(self):
        num_1 = 20
        
        resultado = suma(num_1)
        
        self.assertEqual(resultado, True)
        
    def test_menorde_de_edad(self):
        num_1 = 10
        
        resultado = suma(num_1)
        self.assertEqual(resultado, False)
        
        
if __name__ == "__main__":
    unittest.main()