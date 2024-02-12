from theme.darkmode import DarkMode
from theme.lightmode import LightMode

def darkmode(root, darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    
    root.option_add("*Frame*Background", theme.widget())
    root.option_add("*Frame*Foreground", theme.text())
    root.option_add("*Frame*Outline", theme.highlight())

    root.option_add("*Button*Background", theme.button())
    root.option_add("*Button*Foreground", theme.button_click())

def background(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.background()

def text(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.text()

def widget(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.widget()

def button(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.button()

def button_click(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.button_click(darkmode_enabled)

def highlight(darkmode_enabled):
    theme = DarkMode if darkmode_enabled else LightMode
    return theme.highlight()
