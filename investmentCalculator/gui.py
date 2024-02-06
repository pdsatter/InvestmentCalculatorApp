import tkinter as tk

from tk_canvas import CanvasDrawer
from tk_table import Table

from calculations.calculations import calculate

canvas_width = 800
canvas_height = 400

def calculate_data(table, initialFunds, annualContribution, yearsContributing, returnRate):
    data = calculate(initialFunds, annualContribution, yearsContributing, returnRate)
    
    table.clear_frame()
    table.set_data(data)
    table.generate()

    generate_graph(data)

def generate_graph(data):
    canvas_drawer.draw_years(data)

if __name__ == "__main__":

    root = tk.Tk()
    root.grid()

    root.title("Investment Calculator")
    root.geometry(f'{1450}x{(800)}')

    root.winfo_screenwidth()
    root.winfo_screenheight()

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)

    # Create frames
    main_frame = tk.Frame(root).grid()

    canvasFrame = tk.Frame(main_frame, borderwidth = 1, highlightbackground="black", highlightthickness=1)
    canvasFrame.grid(row=0, column=0, sticky="new")
    canvas = tk.Canvas(canvasFrame, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack(side="top")

    canvas_drawer = CanvasDrawer(canvas, width=canvas_width, height=canvas_height)
    
    tableFrame = tk.Frame(main_frame, borderwidth = 1, highlightbackground="black", highlightthickness=1)
    tableFrame.grid(row=0, column=1, rowspan=3, sticky="nsew")
    table = Table(root=tableFrame, data=None, startRow=0, startCol=2)

    inputFrame = tk.Frame(main_frame, borderwidth = 1, highlightbackground="black", highlightthickness=1)
    inputFrame.grid(row=1, column=0, sticky="nesw")

    emptyFrame = tk.Frame(main_frame)
    emptyFrame.grid(row=2, column=0, sticky="nesw")


    # Fill input frame
    initialFundsLabel = tk.Label(inputFrame, text="Initial Funds ($): ", anchor="w")
    initialFundsLabel.grid(row=11, column=0, sticky="nsew")
    initialFundsEntry = tk.Entry(inputFrame)
    initialFundsEntry.insert(0, "0")
    initialFundsEntry.grid(row=11, column=1, columnspan=1, sticky="nsew")

    annualContributionLabel = tk.Label(inputFrame, text="Annual Contribution ($): ", anchor="w")
    annualContributionLabel.grid(row=12, column=0, sticky="nsew")
    annualContributionEntry = tk.Entry(inputFrame)
    annualContributionEntry.insert(0, "0")
    annualContributionEntry.grid(row=12, column=1, columnspan=1, sticky="nsew")

    yearsContributingLabel = tk.Label(inputFrame, text="Years Contributing (years): ", anchor="w")
    yearsContributingLabel.grid(row=13, column=0, sticky="nsew")
    yearsContributingEntry = tk.Entry(inputFrame)
    yearsContributingEntry.insert(0, "30")
    yearsContributingEntry.grid(row=13, column=1, columnspan=1, sticky="nsew")

    returnRateLabel = tk.Label(inputFrame, text="Return Rate (%): ", anchor="w")
    returnRateLabel.grid(row=14, column=0, sticky="nsew")
    returnRateEntry = tk.Entry(inputFrame)
    returnRateEntry.insert(0, "6.0")
    returnRateEntry.grid(row=14, column=1, columnspan=1, sticky="nsew")

    submitButton = tk.Button(inputFrame, text="Submit", command=lambda: calculate_data(table, float(initialFundsEntry.get()), float(annualContributionEntry.get()), 
                                                                            int(yearsContributingEntry.get()), float(returnRateEntry.get())/100))
    submitButton.grid(row=16, column=0, sticky="nsew")

    


    root.mainloop()