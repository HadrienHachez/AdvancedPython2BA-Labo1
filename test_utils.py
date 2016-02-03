# test_utils.py
# Author: Hadrien Hachez
# Version: February 3, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertNotEqual(utils.fact(0),0)
        with self.assertRaises(ValueError):
            utils.fact(-5)
    
    def test_roots(self):
        self.assertEqual(utils.roots(0,0,1),())
        self.assertEqual(utils.roots(0,1,0),(0))
        self.assertEqual(utils.roots(2,0,-2),(-1,1))
        self.assertNotEqual(utils.roots(0,5,0),(2))
    
    def test_integrate(self):
        self.assertAlmostEqual(utils.integrate('x**2',0,1),1/3,places=3)
        self.assertNotAlmostEqual(utils.integrate('x**2',0,-1),1/3,places=3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
