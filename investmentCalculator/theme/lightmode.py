from theme.theme import Theme
from theme.colors import DARK, CLOONEY, MEDIUM, LIGHT

class LightMode(Theme):
    def background():
        return CLOONEY

    def text():
        return DARK

    def widget():
        return LIGHT

    def button():
        return LightMode.widget()

    def button_click():
        return LightMode.text()

    def highlight():
        return MEDIUM
    