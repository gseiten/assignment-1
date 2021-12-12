import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_minimum_cost(self):
        expected_output = {
            'output': [
                {'region': 'Delhi',
                 'total_cost': 1770,
                 'boxes': [('XL', 6), ('M', 1)]},
                {'region': 'Mumbai',
                 'total_cost': 1642.6,
                 'boxes': [('XL', 6), ('M', 1)]},
                {'region': 'Koltata',
                 'total_cost': 1496,
                 'boxes': [('XL', 6), ('S', 2)]}]
        }
        self.assertEqual(calc.minimum_cost(0, 0), None)
        self.assertEqual(calc.minimum_cost(0, 2), None)
        self.assertEqual(calc.minimum_cost(6, 0), None)
        self.assertEqual(calc.minimum_cost(1000, 2), expected_output)

    def test_calculate(self):
        region_costs = [('XL', 140), ('XXL', 282), ('L', 77.4),
                        ('M', 45), ('S', 23), ('XS', 12)]
        expected_output = {'region': 'Delhi', 'total_cost': 1015,
                           'boxes': [('XL', 7), ('S', 1), ('XS', 1)]}
        self.assertEqual(calc.calculate(
            1150, 1, 'Delhi', region_costs), expected_output)


if __name__ == '__main__':
    unittest.main()
