class YearlyInfo():
    def __init__(self, startingContributedFunds, startingInterestFunds, year=1):
        self.startingContributedFunds = startingContributedFunds
        self.startingInterestFunds = startingInterestFunds
        self.startingTotalFunds = startingContributedFunds + startingInterestFunds

        self.finalContributedFunds = None
        self.finalInterestFunds = None
        self.finalTotalFunds = None
        self.year = year

def calculate(initialFunds, annualContribution, contributionType, yearsContributing, returnRate):
    calculator = CalculatorFactory.get_calculator(contributionType)

    return calculator.calculate_data(initialFunds, annualContribution, yearsContributing, returnRate)

class YearStartCalculator():    
    def calculate_data(self, initialFunds, annualContribution, yearsContributing, returnRate):
        first_year = YearlyInfo(initialFunds, 0)
        self.calculateYear(first_year, annualContribution, returnRate)

        return self.recursive_calculate_yearly_data([first_year], annualContribution, returnRate, yearsContributing-1)

    def recursive_calculate_yearly_data(self, yearly_data, annualContribution, returnRate, yearsLeft):
        if (yearsLeft <= 0): return yearly_data

        pastYear = yearly_data[-1]

        currentYear = YearlyInfo(pastYear.finalContributedFunds, pastYear.finalInterestFunds, pastYear.year+1)
        self.calculateYear(currentYear, annualContribution, returnRate)

        yearly_data.append(currentYear)
        
        return self.recursive_calculate_yearly_data(yearly_data, annualContribution, returnRate, yearsLeft-1)
    
    def calculateYear(self, year, annualContribution, returnRate):
        year.finalContributedFunds = year.startingContributedFunds + annualContribution

        yearStartFunds = year.finalContributedFunds + year.startingInterestFunds
        year.finalInterestFunds = year.startingInterestFunds + returnRate * yearStartFunds

        year.finalTotalFunds = year.finalInterestFunds + year.finalContributedFunds

class YearEndCalculator():
    def calculate_data(self, initialFunds, annualContribution, yearsContributing, returnRate):
        first_year = YearlyInfo(initialFunds, 0)
        self.calculateYear(first_year, annualContribution, returnRate)

        return self.recursive_calculate_yearly_data([first_year], annualContribution, returnRate, yearsContributing-1)

    def recursive_calculate_yearly_data(self, yearly_data, annualContribution, returnRate, yearsLeft):
        if (yearsLeft <= 0): return yearly_data

        pastYear = yearly_data[-1]

        currentYear = YearlyInfo(pastYear.finalContributedFunds, pastYear.finalInterestFunds, pastYear.year+1)
        self.calculateYear(currentYear, annualContribution, returnRate)

        yearly_data.append(currentYear)
        
        return self.recursive_calculate_yearly_data(yearly_data, annualContribution, returnRate, yearsLeft-1)
    
    def calculateYear(self, year, annualContribution, returnRate):
        year.finalContributedFunds = year.startingContributedFunds + annualContribution

        yearStartFunds = year.startingContributedFunds + year.startingInterestFunds
        year.finalInterestFunds = year.startingInterestFunds + returnRate * yearStartFunds

        year.finalTotalFunds = year.finalInterestFunds + year.finalContributedFunds

class CalculatorFactory():
    def get_calculator(type):
        if type == 'Year Start':
            return YearStartCalculator()
        elif type =='Year End':
            return YearEndCalculator()
        else: Exception('Calculator Not found')