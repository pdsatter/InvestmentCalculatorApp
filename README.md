# InvestmentCalculatorApp

## Disclaimer
This app should not be used as financial advice. It is a tool for information purposes and the user is responsible for understanding how it works. I am not held responsible for any financial decisions based off of this model.

## Contact Me
Contact me if you need help or additional features. View my profile for information on contacting me.

## How to run
### To run Windows build
1. [Download zip](https://github.com/pdsatter/InvestmentCalculatorApp/archive/refs/heads/main.zip)
2. Go to "windows_distribution" folder
3. Open "gui" file
4. Thats it :D



## Current Features

* Calculates interest over time. Shows interest earned as green and contributed funds in blue
* Displays in both Table and Graphical form
* Displays Cumulative Interest, Yearly Interest, Contributed Funds, and Total Balance for each year.
* User can adjust average return rate, years contributing, annual contribution, and initial balance
* Dark mode
* Dynamic resizing
* Change when the funds are invested

## Planned features (as time permits / per request)
* Monthly contribution (instead of yearly)
* Can increase contributions by percentage every year
* User Preferences
  * Graph color
  * Font

## For programers
Run the gui.py file in VSCode or python interpreter
### Compile new GUI
Use PyInstaller Module  

```
py -m PyInstaller gui.py
```

### Run Unit tests
In root directory run:
```
py -m unittest
```

## Needed modules
```
py -m pip install tkinter
```

```
py -m pip install PyInstaller
```
