# test_utils.py
# Author: Hadrien Hachez
# Version: February 3, 2016
# cool

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertNotEqual(utils.fact(0),0)
        with self.assertRaises(TypeError):
            utils.fact('3')
        with self.assertRaises(ValueError):
            utils.fact(-5)
    
    def test_roots(self):
        self.assertEqual(utils.roots(0,3,2),-2/3)
        self.assertNotEqual(utils.roots(0,5,0),2)
        with self.assertRaises(TypeError):
            utils.roots('3',0,0)
    
    def test_integrate(self):
        self.assertEqual(utils.integrate('x**2',0,1),1/2)
        self.assertNotEqual(utils.integrate('x**2',0,-1),1/2)
        with self.assertRaises(TypeError):
            utils.integrate(3,2,4)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
