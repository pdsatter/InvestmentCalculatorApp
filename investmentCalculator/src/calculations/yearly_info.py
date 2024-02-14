class YearlyInfo():
    def __init__(self, startingContributedFunds, startingInterestFunds, year=1):
        self.startingContributedFunds = startingContributedFunds
        self.startingInterestFunds = startingInterestFunds
        self.startingTotalFunds = startingContributedFunds + startingInterestFunds

        self.finalContributedFunds = None
        self.finalInterestFunds = None
        self.finalTotalFunds = None
        self.year = year
