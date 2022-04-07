import unittest
from matn import get_full_name

class MatnTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('shahzod','rahimberdiyev')
        self.assertEqual(formatted_name, 'Shahzod Rahimberdiyev')
        
unittest.main()

        
