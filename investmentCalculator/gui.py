
from tkinter import StringVar, OptionMenu
import tkinter as tk

from tk_canvas import CanvasDrawer
from tk_table import Table

from calculations.calculations import calculate

from theme_selector import darkmode, highlight

canvas_width = 800
canvas_height = 400

darkmode_enabled = False

def get_list_of_pages(table):
    pages = list(range(1, table.get_number_of_pages() + 1))

    if len(pages) == 0: return [1]
    return pages

def update_page_ui_select(table, page_menu):
    pages = get_list_of_pages(table)
   
    page_menu_variable.set(str(pages[0]))

    page_menu['menu'].delete(0, 'end')
    
    for page in pages:
        page = str(page)
        page_menu['menu'].add_command(label=page, command=lambda value=page: update_page_number(table, value, page_menu_variable))

    page_menu.update()

def submit(table, get_input_data, page_menu):
    calculate_data(table, get_input_data)

    update_page_ui_select(table, page_menu)

def update_page_size(table, page_size, page_size_menu_variable, page_menu):
    table.set_page_size(str(page_size))
    page_size_menu_variable.set(page_size)

    update_page_ui_select(table, page_menu)

def update_page_number(table, page_number, page_menu_variable):
    table.set_page(str(page_number))
    page_menu_variable.set(page_number)

def calculate_data(table, get_input_data):
    input_data = get_input_data()
    data = calculate(*input_data)

    table.set_data(data)
    table.update()

    generate_graph(data)

def generate_graph(data):
    canvas_drawer.draw_years(data)

def get_input_data():
    initialFunds = initialFundsEntry.get()
    annualContribution = annualContributionEntry.get()
    yearsContributing = yearsContributingEntry.get()
    returnRate = returnRateEntry.get()

    initialFunds = float(initialFunds) if initialFunds != '' else 0
    annualContribution = float(annualContribution) if annualContribution != '' else 0
    yearsContributing = int(yearsContributing) if annualContribution != '' else 0
    returnRate = float(returnRate)/100 if returnRate != '' else 0

    return [initialFunds, annualContribution, yearsContributing, returnRate]

if __name__ == "__main__":

    root = tk.Tk()
    root.grid()

    root.title("Investment Calculator")
    root.geometry(f'{1450}x{(800)}')

    root.winfo_screenwidth()
    root.winfo_screenheight()

    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)

    darkmode(root, darkmode_enabled)
    
    # Create frames
    main_frame = tk.Frame(root).grid()

    canvasFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    canvasFrame.grid(row=0, column=0, sticky="nsew")
    canvas = tk.Canvas(canvasFrame, width=canvas_width, height=canvas_height, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    canvas.pack(side="top")

    canvas_drawer = CanvasDrawer(canvas, width=canvas_width, height=canvas_height)
    
    tableFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    tableFrame.grid(row=0, column=1, rowspan=3, sticky="nsew")
    table = Table(root=tableFrame, startRow=0, startCol=2)

    inputFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    inputFrame.grid(row=1, column=0, sticky="nesw")

    inputFrame.grid_columnconfigure(0, weight=1)

    leftInputFrame = tk.Frame(inputFrame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    leftInputFrame.grid(row=1, column=0, sticky="nsew")

    rightInputFrame = tk.Frame(inputFrame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled))
    rightInputFrame.grid(row=1, column=1, sticky="nesw")

    # Fill left input frame
    initialFundsLabel = tk.Label(leftInputFrame, text="Initial Funds ($): ", anchor="w")
    initialFundsLabel.grid(row=1, column=0, sticky="nsew")
    initialFundsEntry = tk.Entry(leftInputFrame)
    initialFundsEntry.insert(0, "0")
    initialFundsEntry.grid(row=1, column=1, columnspan=1, sticky="nsew")

    annualContributionLabel = tk.Label(leftInputFrame, text="Annual Contribution ($): ", anchor="w")
    annualContributionLabel.grid(row=2, column=0, sticky="nsew")
    annualContributionEntry = tk.Entry(leftInputFrame)
    annualContributionEntry.insert(0, "0")
    annualContributionEntry.grid(row=2, column=1, columnspan=1, sticky="nsew")

    yearsContributingLabel = tk.Label(leftInputFrame, text="Years Contributing (years): ", anchor="w")
    yearsContributingLabel.grid(row=3, column=0, sticky="nsew")
    yearsContributingEntry = tk.Entry(leftInputFrame)
    yearsContributingEntry.insert(0, "30")
    yearsContributingEntry.grid(row=3, column=1, columnspan=1, sticky="nsew")

    returnRateLabel = tk.Label(leftInputFrame, text="Return Rate (%): ", anchor="w")
    returnRateLabel.grid(row=4, column=0, sticky="nsew")
    returnRateEntry = tk.Entry(leftInputFrame)
    returnRateEntry.insert(0, "6.0")
    returnRateEntry.grid(row=4, column=1, columnspan=1, sticky="nsew")

    submitButton = tk.Button(leftInputFrame, text="Submit", command=lambda: submit(table, get_input_data, page_menu))
    submitButton.grid(row=6, column=0, sticky="nsew")

    # Fill right input frame
    # Pages
    pages = get_list_of_pages(table)
    page_menu_variable = StringVar(rightInputFrame)
    page_menu_variable.set(pages[0])

    pageLabel = tk.Label(rightInputFrame, text="Select Tables Page:", anchor="w")
    pageLabel.grid(row=1, column=2, sticky="nsew")
    
    page_menu = OptionMenu(rightInputFrame, page_menu_variable, *(pages), command=lambda page: update_page_number(table, page, page_menu_variable))
    page_menu.grid(row=1, column=4, sticky="nsew")

    pageSize = ['10', '30', '50']
    page_size_menu_variable = StringVar(rightInputFrame)
    page_size_menu_variable.set(pageSize[1])

    pageSizeLabel = tk.Label(rightInputFrame, text="Select Page Size:", anchor="w")
    pageSizeLabel.grid(row=2, column=2, sticky="nsew")
    
    pageSizeMenu = OptionMenu(rightInputFrame, page_size_menu_variable, *(pageSize), command=lambda pageSize: update_page_size(table, pageSize, page_size_menu_variable, page_menu))
    pageSizeMenu.grid(row=2, column=4, sticky="e")

    root.mainloop()