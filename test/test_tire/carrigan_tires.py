import unittest

from tires.carrigan import CarriganTire

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_tear = [0.1,0.3,0.4,0.2]
        array = CarriganTire(wear_tear)
        self.assertTrue(array.needs_service)
    
    def test_needs_service_false(self):
        wear_tear = [0.1,0.1,0.1,0.2]
        array = CarriganTire(wear_tear)
        self.assertFalse(array.needs_service)
