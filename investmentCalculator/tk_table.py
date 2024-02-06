import tkinter as tk

def get_widgets_for_year_data(root, year_data, row, col, startRow):
    year = row - startRow

    yearLabel = tk.Label(root, text=f"{year_data.year}", anchor="w")
    contributedFundsLabel = tk.Label(root, text=f"${year_data.finalContributedFunds:,.2f}", anchor="w")
    cumulativeInterestEarnedLabel = tk.Label(root, text=f"${year_data.finalInterestFunds:,.2f}", anchor="w")
    interestEarnedLabel = tk.Label(root, text=f" ${year_data.finalInterestFunds - year_data.startingInterestFunds:,.2f}", anchor="w")
    totalFundsLabel = tk.Label(root, text=f"${year_data.finalTotalFunds:,.2f}", anchor="w")

    yearLabel.grid(row=row, column=0+col, sticky="nsew")
    contributedFundsLabel.grid(row=row, column=1+col, sticky="nsew")
    cumulativeInterestEarnedLabel.grid(row=row, column=2+col, sticky="nsew")
    interestEarnedLabel.grid(row=row, column=3+col, sticky="nsew")
    totalFundsLabel.grid(row=row, column=4+col, sticky="nsew")

    return [contributedFundsLabel, cumulativeInterestEarnedLabel, interestEarnedLabel, totalFundsLabel]
    
def get_widgets_for_year_headers(root, row, col):
    yearHeader = tk.Label(root, text="Year ", anchor="w", font='bold')
    contributedFundsHeader = tk.Label(root, text="Contributed Funds ", anchor="w", font='bold')
    cumulativeInterestEarnedHeader = tk.Label(root, text="Cumulative Interest ", anchor="w", font='bold')
    interestEarnedHeader = tk.Label(root, text="Yearly Interest ", anchor="w", font='bold')
    totalFundsHeader = tk.Label(root, text="Total Balance ", anchor="w", font='bold')

    yearHeader.grid(row=row, column=0+col, sticky="nsew")
    contributedFundsHeader.grid(row=row, column=1+col, sticky="nsew")
    cumulativeInterestEarnedHeader.grid(row=row, column=2+col, sticky="nsew")
    interestEarnedHeader.grid(row=row, column=3+col, sticky="nsew")
    totalFundsHeader.grid(row=row, column=4+col, sticky="nsew")

    return [contributedFundsHeader, cumulativeInterestEarnedHeader, interestEarnedHeader, totalFundsHeader]

class Table():
    def __init__(self, root, data, startRow, startCol):
        self.root = root
        self.data = data
        self.startRow = startRow
        self.startCol = startCol

    def set_data(self, data):
        self.data = data
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def generate(self, get_widgets_from_data=get_widgets_for_year_data, get_widgets_for_headers=get_widgets_for_year_headers):
        rows = len(self.data)

        headers = get_widgets_for_headers(self. root, self.startRow, self.startCol)
        self._widgets = [headers]

        for r in range(rows):
            widgets_in_row = get_widgets_from_data(self.root, self.data[r], 
                                                   row=(r+self.startRow+1), 
                                                   col=self.startCol,
                                                   startRow=self.startRow)
            
            self._widgets.append(widgets_in_row)

    def get_widgets(self):
        return self._widgets



