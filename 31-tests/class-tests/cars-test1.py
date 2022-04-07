# XUSUSIYATLARNI TEST QILISH

import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def test_create(self):
        # avto1 obyektini km va narxini bermasdan yaratamiz
        avto1 = Car('toyota','camry',2020)
        # assertIsNotNone() qiymat mavjudligini tekshiradi
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        # assertIsNone qiymat mavjud emasligini tekshiradi
        self.assertIsNone(avto1.price)
        # assertEquals qiymatlar tengligini tekshiradi
        self.assertEqual(0,avto1.get_km())
        # Yangi obyekt yaratamiz va narxini ham ko'rsatamiz
        avto2 = Car("toyota","camry","2020",price=75000)
        self.assertEqual(75000,avto2.price)

unittest.main() 