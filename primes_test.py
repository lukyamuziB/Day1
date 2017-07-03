import unittest

from prime_numbers import prime

class prime_test(unittest.TestCase):
	def test_for_prime_works(self):
		self.assertEqual(prime(10),[3,5,7,9])
	def test_for_a_string_passed_in(self):
		self.assertRaises(TypeError, prime,"ben")
	def test_for_numbers_less_than_2(self):
		self.assertRaises(ValueError,prime,2)
	

   
if __name__ == '__main__':
    unittest.main()
	
