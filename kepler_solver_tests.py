from pylab import *

import unittest
from kepler_solver import E_from_t

class TestKnownValues(unittest.TestCase):
    def setUp(self):
        self.P = 1.24253
        self.e = 0.728

    def test_zero(self):
        self.assertAlmostEqual(E_from_t(0, self.P, self.e), 0.0)

class TestRandomValues(unittest.TestCase):
    def setUp(self):
        self.P = rand()
        self.e = rand()

    def test_random(self):
        t = self.P*rand()
        E = E_from_t(t, self.P, self.e)
        self.assertAlmostEqual(E - self.e*sin(E) - 2*pi*t/self.P, 0.0)

if __name__ == '__main__':
    unittest.main()
