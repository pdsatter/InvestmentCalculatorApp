class YearlyInfo():
    def __init__(self, startingContributedFunds, startingInterestFunds, year=1):
        self.startingContributedFunds = startingContributedFunds
        self.startingInterestFunds = startingInterestFunds
        self.startingTotalFunds = startingContributedFunds + startingInterestFunds

        self.finalContributedFunds = None
        self.finalInterestFunds = None
        self.finalTotalFunds = None
        self.year = year

    def calculateYear(self, annualContribution, returnRate):
        self.finalContributedFunds = self.startingContributedFunds + annualContribution

        yearStartFunds = self.finalContributedFunds + self.startingInterestFunds
        self.finalInterestFunds = self.startingInterestFunds + returnRate * yearStartFunds

        self.finalTotalFunds = self.finalInterestFunds + self.finalContributedFunds

def calculate(initialFunds, annualContribution, contributionTime, yearsContributing, returnRate):
    firstYear = YearlyInfo(initialFunds, 0)
    firstYear.calculateYear(annualContribution, returnRate)

    yearly_data = [firstYear]

    print(contributionTime)
    return recursive_calculate_yearly_data(yearly_data, annualContribution, returnRate, yearsContributing-1)

def recursive_calculate_yearly_data(yearly_data, annualContribution, returnRate, yearsLeft):
    if (yearsLeft <= 0): return yearly_data

    pastYear = yearly_data[-1]

    currentYear = YearlyInfo(pastYear.finalContributedFunds, pastYear.finalInterestFunds, pastYear.year+1)
    currentYear.calculateYear(annualContribution, returnRate)

    yearly_data.append(currentYear)
    
    return recursive_calculate_yearly_data(yearly_data, annualContribution, returnRate, yearsLeft-1)
