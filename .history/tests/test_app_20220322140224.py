import unittest
from app import sum

class test_app(unittest.TestCase):

    def test_list_int(self):
            data = [1, 2, 3, 4, 5]
            result = sum(data)
            self.assertEqual(result, 15)

    def test_lisf_float(self):
        data = [1.2, 2.4, 2.7, 0.5, 1.8]  
        result = sum(data)
        self.assertEqual(result, 8.6) 