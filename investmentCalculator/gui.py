from tkinter import StringVar, OptionMenu
import tkinter as tk

from tk_canvas import CanvasDrawer
from tk_table import Table

from calculations.calculations import calculate

from theme_selector import set_theme, highlight

canvas_width = 800
canvas_height = 400

def theme(root, darkmode_enabled):
    set_theme(root, darkmode_enabled)
    gui(root)

def get_list_of_pages(table):
    pages = list(range(1, table.get_number_of_pages() + 1))

    if len(pages) == 0: return [1]
    return pages

def update_page_ui_select(table, page_menu, page_menu_variable):
    pages = get_list_of_pages(table)
   
    page_menu_variable.set(str(pages[0]))

    page_menu['menu'].delete(0, 'end')
    
    for page in pages:
        page = str(page)
        page_menu['menu'].add_command(label=page, command=lambda value=page: update_page_number(table, value, page_menu_variable))

    page_menu.update()

def submit(table, page_menu, canvas_drawer, page_menu_variable, initialFunds, annualContribution, yearsContributing, returnRate):
    calculate_data(table, canvas_drawer, initialFunds, annualContribution, yearsContributing, returnRate)

    update_page_ui_select(table, page_menu, page_menu_variable)

def update_page_size(table, page_size, page_size_menu_variable, page_menu, page_menu_variable):
    table.set_page_size(str(page_size))
    page_size_menu_variable.set(page_size)

    update_page_ui_select(table, page_menu, page_menu_variable)

def update_page_number(table, page_number, page_menu_variable):
    table.set_page(str(page_number))
    page_menu_variable.set(page_number)

def calculate_data(table, canvas_drawer, initialFunds,  annualContribution, yearsContributing, returnRate):
    data = calculate(initialFunds, annualContribution, yearsContributing, returnRate)

    table.set_data(data)
    table.update()

    generate_graph(data, canvas_drawer)

def generate_graph(data, canvas_drawer):
    canvas_drawer.draw_years(data)

def generate_left_input_frame(left_input_frame, table, page_menu, canvas_drawer, page_menu_variable):
    initialFundsLabel = tk.Label(left_input_frame, text="Initial Funds ($): ", anchor="w")
    initialFundsLabel.grid(row=1, column=0, sticky="nsew")
    initialFundsEntry = tk.Entry(left_input_frame)
    initialFundsEntry.insert(0, "0")
    initialFundsEntry.grid(row=1, column=1, columnspan=1, sticky="nsew")

    annualContributionLabel = tk.Label(left_input_frame, text="Annual Contribution ($): ", anchor="w")
    annualContributionLabel.grid(row=2, column=0, sticky="nsew")
    annualContributionEntry = tk.Entry(left_input_frame)
    annualContributionEntry.insert(0, "0")
    annualContributionEntry.grid(row=2, column=1, columnspan=1, sticky="nsew")

    yearsContributingLabel = tk.Label(left_input_frame, text="Years Contributing (years): ", anchor="w")
    yearsContributingLabel.grid(row=3, column=0, sticky="nsew")
    yearsContributingEntry = tk.Entry(left_input_frame)
    yearsContributingEntry.insert(0, "30")
    yearsContributingEntry.grid(row=3, column=1, columnspan=1, sticky="nsew")

    returnRateLabel = tk.Label(left_input_frame, text="Return Rate (%): ", anchor="w")
    returnRateLabel.grid(row=4, column=0, sticky="nsew")
    returnRateEntry = tk.Entry(left_input_frame)
    returnRateEntry.insert(0, "6.0")
    returnRateEntry.grid(row=4, column=1, columnspan=1, sticky="nsew")

    submitButton = tk.Button(left_input_frame, text="Submit", command=lambda: submit(table, page_menu, canvas_drawer, page_menu_variable,
                                                                                     initialFunds=float(initialFundsEntry.get()), annualContribution=float(annualContributionEntry.get()), 
                                                                                     yearsContributing=float(yearsContributingEntry.get()), returnRate=float(returnRateEntry.get())/100))
    submitButton.grid(row=6, column=0, sticky="nsew")

def generate_right_input_frame(right_input_frame, table):
    pages = get_list_of_pages(table)
    page_menu_variable = StringVar(right_input_frame)
    page_menu_variable.set(pages[0])

    pageLabel = tk.Label(right_input_frame, text="Select Tables Page:", anchor="w")
    pageLabel.grid(row=1, column=2, sticky="nsew")
    
    page_menu = OptionMenu(right_input_frame, page_menu_variable, *(pages), command=lambda page: update_page_number(table, page, page_menu_variable))
    page_menu.grid(row=1, column=4, sticky="nsew")

    pageSize = ['10', '30', '50']
    page_size_menu_variable = StringVar(right_input_frame)
    page_size_menu_variable.set(pageSize[1])

    pageSizeLabel = tk.Label(right_input_frame, text="Select Page Size:", anchor="w")
    pageSizeLabel.grid(row=2, column=2, sticky="nsew")
    
    pageSizeMenu = OptionMenu(right_input_frame, page_size_menu_variable, *(pageSize), command=lambda pageSize: update_page_size(table, pageSize, page_size_menu_variable, page_menu, page_menu_variable))
    pageSizeMenu.grid(row=2, column=4, sticky="e")

    return [page_menu, page_menu_variable]

def create_frames(root):
    main_frame = tk.Frame(root).grid()

    topBarFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    topBarFrame.grid(row=0, column=0, columnspan=2, sticky="nsew")

    canvasFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    canvasFrame.grid(row=1, column=0, sticky="nsew")

    tableFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    tableFrame.grid(row=1, column=1, rowspan=3, sticky="nsew")

    inputFrame = tk.Frame(main_frame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    inputFrame.grid(row=2, column=0, sticky="nesw")

    inputFrame.grid_columnconfigure(0, weight=1)

    leftInputFrame = tk.Frame(inputFrame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    leftInputFrame.grid(row=1, column=0, sticky="nsew")

    rightInputFrame = tk.Frame(inputFrame, borderwidth = 1, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    rightInputFrame.grid(row=1, column=1, sticky="nesw")

    return [topBarFrame, canvasFrame, tableFrame, leftInputFrame, rightInputFrame]

def preferences(frame):
    preferencesLabel = tk.Label(frame, text="Preferences (refreshes gui): ")
    preferencesLabel.grid(row=0, column=1, sticky="nsew")

    dark_mode_check_box = tk.Checkbutton(frame, text='Darkmode',variable=darkmode_enabled, onvalue=True, offvalue=False, command=lambda: theme(root, darkmode_enabled.get()))
    dark_mode_check_box.grid(row=0, column=2, sticky="e")

def gui(root):

    [topBarFrame, canvasFrame, tableFrame, leftInputFrame, rightInputFrame] = create_frames(root)

    canvas = tk.Canvas(canvasFrame, width=canvas_width, height=canvas_height, highlightthickness=0.5, highlightbackground=highlight(darkmode_enabled.get()))
    canvas.pack(side="top")

    canvas_drawer = CanvasDrawer(canvas, width=canvas_width, height=canvas_height)

    table = Table(root=tableFrame, startRow=0, startCol=2)

    [page_menu, page_menu_variable] = generate_right_input_frame(rightInputFrame, table)

    generate_left_input_frame(leftInputFrame, table, page_menu, canvas_drawer, page_menu_variable)

    dark_mode_check_box = tk.Checkbutton(topBarFrame, text='Darkmode',variable=darkmode_enabled, onvalue=True, offvalue=False, command=lambda: theme(root, darkmode_enabled.get()))
    dark_mode_check_box.grid(row=0, column=2, sticky="e")

    preferences(topBarFrame)   

if __name__ == "__main__":

    root = tk.Tk()
    root.grid()

    root.title("Investment Calculator")
    root.geometry(f'{1450}x{(800)}')

    root.winfo_screenwidth()
    root.winfo_screenheight()

    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(2, weight=1)

    darkmode_enabled = tk.BooleanVar(value=False)

    theme(root, darkmode_enabled.get())

    gui(root)

    root.mainloop()
