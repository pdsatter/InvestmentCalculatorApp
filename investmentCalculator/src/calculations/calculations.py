from  .calculator_factory import CalculatorFactory

def calculate(initialFunds, annualContribution, contributionType, yearsContributing, returnRate):
    calculator = CalculatorFactory.get_calculator(contributionType)

    return calculator.calculate_data(initialFunds, annualContribution, yearsContributing, returnRate)
