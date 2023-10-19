import unittest
from datetime import date
from battery.spindler_battery import SplinderBattery

class TestSplinderBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-05-08")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service)
    
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-05-08")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service)