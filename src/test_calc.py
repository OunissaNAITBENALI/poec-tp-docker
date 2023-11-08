
from calc import apply_percent
import unittest


class TestCalcMethods(unittest.TestCase):
    def test_calc_nominal_case(self):
        self.assertEqual(apply_percent(100, 20), 120)
        #self.assertEqual(apply_percent(55.25, 5.5), 58.29)   #prendre que deux chiffres après la virgule
        #self.assertEqual(apply_percent(0, 10), 0)


        #self.assertEqual(apply_percent('Wrong Value', 10))

if __name__ == '__main__':
    unittest.main()

    #def test_calc_exception(self):
        #raise apply_percent(-10.99, 10)
        #except
        #print('ValueError: Price ($-10.99) is negative')"""








#effectuer les tests unitaires:
 #Tester que la fonction renvoie à chaque fois une valeur correcte:
#price = 100, percent = 20
#price = 55.25, percent = 5.5,
#price = 0, percent = 10,
#price = -10.99, percent = 10,
#price = 'wrong value', percent = 10
#price = 100, percent = -10
#price = 100, percent = 110"""


#class test_calc:
    #def __init__(self, price, percent):
     #   self.price = price
      #  self.percent = percent """
