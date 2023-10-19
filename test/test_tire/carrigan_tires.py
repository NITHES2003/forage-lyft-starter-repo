import unittest

from tires.carrigan import CarriganTire

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        array = [0.1,0.3,0.4,0.2]
        array = CarriganTire(array)
        self.assertTrue(tire.needs_service())
    
    def test_needs_service_false(self):
        array = [0.1,0.1,0.1,0.2]
        array = CarriganTire(array)
        self.assertFalse(tire.needs_service())