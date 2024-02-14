from ..src.calculations.calculations import calculate
import unittest

class TestCalculations(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_calculations_error_with_none_contributions_type(self):
        self.assertRaises(Exception, calculate, 0, 0, None, 0, 0)

    def test_calculations_error_with_empty_contributions_type(self):
        self.assertRaises(Exception, calculate, 0, 0, '', 0, 0)

    def test_year_start_calculations_with_zero(self):
        data = calculate(0, 0, 'Year Start', 5, 0)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(first_year.finalTotalFunds, 0)
        self.assertEqual(last_year.finalTotalFunds, 0)

    def test_year_end_calculations_with_zero(self):
        data = calculate(0, 0, 'Year End', 5, 0)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(first_year.finalTotalFunds, 0)
        self.assertEqual(last_year.finalTotalFunds, 0)

    def test_year_start_calculations_with_initial_contributions(self):
        data = calculate(500, 0, 'Year Start', 20, 0.06)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 530.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 1603.57)

    def test_year_end_calculations_with_initial_contributions(self):
        data = calculate(500, 0, 'Year End', 20, 0.06)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 530.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 1603.57)

    def test_year_start_calculations_with_annual_contributions(self):
        data = calculate(0, 700, 'Year Start', 20, 0.06)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 742.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 27294.91)

    def test_year_end_calculations_with_annual_contributions(self):
        data = calculate(0, 700, 'Year End', 20, 0.06)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 700.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 25749.91)

    def test_year_start_calculations_with_all_fields(self):
        data = calculate(2000, 700, 'Year Start', 20, 0.08)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 2916.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 43917.96)

    def test_year_end_calculations_with_all_fields(self):
        data = calculate(2000, 700, 'Year End', 20, 0.08)

        first_year = data[0]
        last_year = data[-1]

        self.assertEqual(round(first_year.finalTotalFunds, 2), 2860.00)
        self.assertEqual(round(last_year.finalTotalFunds, 2), 41355.29)



if __name__ == '__main__':
    unittest.main()