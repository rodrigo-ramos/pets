import unittest
import pet
import re

class TestStringMethods(unittest.TestCase):

	
	def testealo(self):
		n = 'Tete esta contento'
		self.assertNotEqual (len(pet.hello(n)), 1)
		
	def testealo2(self):
		n = 'Tete esta contento'
		m = re.compile('Tete')
		self.assertRegex (pet.hello(n),m)
		
if __name__ == '__main__':
    unittest.main()

