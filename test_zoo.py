import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price0(self):
        self.assertEqual(self.zoo.get_ticket_price(-4), "your mom dead")
       
    def test_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(7), 50)

    def test_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)

    def test_child_ticket_price3(self):
        self.assertEqual(self.zoo.get_ticket_price(57), 150)

    def test_child_ticket_price4(self):
        self.assertEqual(self.zoo.get_ticket_price(80), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()