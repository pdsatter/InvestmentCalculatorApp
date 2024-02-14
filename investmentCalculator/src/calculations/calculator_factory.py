from .year_start_calculator import YearStartCalculator
from .year_end_calculator import YearEndCalculator

class CalculatorFactory():
    def get_calculator(type):
        if type == 'Year Start':
            return YearStartCalculator()
        elif type =='Year End':
            return YearEndCalculator()
        else: Exception('Calculator Not found')
