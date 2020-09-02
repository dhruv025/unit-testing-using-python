import unittest
import calc

class TestCalc(unittest.TestCase):
	def test_add(self):
		res1 = calc.add(2,5)
		self.assertEqual(res1,7)

		res2 = calc.add(-1,1)
		self.assertEqual(res2,0)
	
		res3 = calc.add(-1,-1)
		self.assertEqual(res3,-2)

	def test_subtract(self):
		self.assertEqual(calc.subtract(5,2),3)
		self.assertEqual(calc.subtract(-1,1),-2)
		self.assertEqual(calc.subtract(-1,-1),0)
	
	def test_multiply(self):
		self.assertEqual(calc.multiply(5,2),10)
		self.assertEqual(calc.multiply(-1,1),-1)
		self.assertEqual(calc.multiply(-1,-1),1)

	def test_divide(self):
		self.assertEqual(calc.divide(5,2),2.5)
		self.assertEqual(calc.divide(-1,1),-1)
		self.assertEqual(calc.divide(-1,-1),1)
		self.assertRaises(ValueError,calc.divide,5,0)
		
		with self.assertRaises(ValueError):
			calc.divide(10,0)
	
if __name__ == '__main__':
	unittest.main()
