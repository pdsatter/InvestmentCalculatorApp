from theme.darkmode import DarkMode
from theme.lightmode import LightMode

def theme(darkmode_enabled):
    return DarkMode if darkmode_enabled else LightMode

def set_theme(root, darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    
    root.option_add("*Frame*Background", selected_theme.widget())
    root.option_add("*Frame*Foreground", selected_theme.text())
    root.option_add("*Frame*Outline", selected_theme.highlight())

    root.option_add("*Button*Background", selected_theme.button())
    root.option_add("*Button*Foreground", selected_theme.button_click())

def background(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.background()

def text(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.text()

def widget(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.widget()

def button(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.button()

def button_click(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.button_click(darkmode_enabled)

def highlight(darkmode_enabled):
    selected_theme = theme(darkmode_enabled)
    return selected_theme.highlight()
