import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    print('setUpClass')

  @classmethod
  def tearDownClass(cls):
    print('tearDownClass')	

  def setUp(self):
    print('setup')
    self.emp_1 = Employee('Dhruv','Goel',500000)
    self.emp_2 = Employee('Rohit','Sharma',60000)
	
  def tearDown(self):
    print('tearDown\n')

  def test_email(self):
    print('test_mail')
    self.assertEqual(self.emp_1.email,'Dhruv.Goel@gmail.com')
    self.assertEqual(self.emp_2.email,'Rohit.Sharma@gmail.com')

    self.emp_1.first = 'Shushant'
    self.emp_2.first = 'Rahul'

    self.assertEqual(self.emp_1.email,'Shushant.Goel@gmail.com')
    self.assertEqual(self.emp_2.email,'Rahul.Sharma@gmail.com')

  def test_fullname(self):
    print('test_fullname')
    self.assertEqual(self.emp_1.fullname,'Dhruv Goel')
    self.assertEqual(self.emp_2.fullname,'Rohit Sharma')

    self.emp_1.first = 'Shushant'
    self.emp_2.first = 'Rahul'

    self.assertEqual(self.emp_1.fullname,'Shushant Goel')
    self.assertEqual(self.emp_2.fullname,'Rahul Sharma')

  def test_apply_raise(self):
    print('test_apply_raise')
    self.emp_1.apply_raise()
    self.emp_2.apply_raise()

    self.assertEqual(self.emp_1.pay,525000)
    self.assertEqual(self.emp_2.pay,63000)

if __name__ == '__main__':
    unittest.main()
