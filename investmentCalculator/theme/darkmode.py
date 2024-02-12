from theme.theme import Theme
from theme.colors import DARK, WHITE, TEFLON, CLOONEY

class DarkMode(Theme):
    def background():
        return DARK

    def text():
        return WHITE

    def widget():
        return TEFLON

    def button():
        return DarkMode.widget()

    def button_click():
        return DarkMode.text()

    def highlight():
        return CLOONEY
