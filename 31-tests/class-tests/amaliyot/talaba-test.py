import unittest
from talaba import Shaxs

class ShaxsTest(unittest.TestCase):
    """Shaxs klassini tekshirish uchun test"""
    def setUp(self):
        ism = "Shahzod"
        familiya = "Rahimberdiyev"
        passport = "FD2233441"
        tyil = 1998
        self.shaxs1 = Shaxs(ism,familiya,passport,tyil)
        
    def test_create(self):
        # Qiymatlar mavjudligini tekshiramiz
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        
    def test_get_info(self):
        shaxs1_info = "Shahzod Rahimberdiyev, Passport:FD2233441, 1998-yilda tug'ilgan"
        self.assertEqual(shaxs1_info,self.shaxs1.get_info())
        
unittest.main()