# Unittest: Pruebas en el propio codigo
# Resultado de los test unitarios
# OK: Pasado con Exito
# F: Fallo asertivo(Falso)
# E: Error tradicional

import unittest

def doblar(a):return a*2
def sumar(a,b):return a+b
def es_par(a):return True if a%2 == 0 else False

# class PruebasFunciones(unittest.TestCase):
#     def test(self):
#         pass
#         #raise AssertionError()
#         # 1/0
#     def test_doblar(self):
#         self.assertEqual(doblar(10),20)
#         self.assertEqual(doblar('Ab'),'AbAb')

#     def test_sumar(self):
#         self.assertEqual(sumar(-15,15),0)
#         self.assertEqual(sumar('Ab',0),'Abc0')
    
#     def test_es_par(self):
#         self.assertEqual(es_par(11), False)
#         self.assertEqual(es_par(69), True)

# class PruebasMetodosCadenas(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual('hola'.upper(), 'HOLA')
    
#     def test_isupper(self):
#         self.assertTrue('HOLA'.isupper())
#         self.assertFalse('hola'.isupper())

#     def test_split(self):
#         s = 'Hola mundo'
#         self.assertEqual(s.split(" "), ['Hola', 'mundo'])

#unittest.TestCase
#setUp : Contructor
#tearDown : Destructor

class PruebaTestFixture(unittest.TestCase):
    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]
    
    def test(self):
        print("Realizando una prueba")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)

if __name__ == "__main__":
    unittest.main()

