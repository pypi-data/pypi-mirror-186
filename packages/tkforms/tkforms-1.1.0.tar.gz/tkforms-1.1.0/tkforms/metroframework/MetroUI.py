import clr
from tkforms.metroframework import metro_lib, metro_fonts_lib, metro_design_lib
clr.AddReference(metro_lib)
clr.AddReference(metro_fonts_lib)
clr.AddReference(metro_design_lib)
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from MetroFramework.Controls import MetroButton, MetroComboBox, MetroLabel, MetroPanel, MetroTextBox
from MetroFramework import MetroThemeStyle
from System.Drawing import Point, Size
from tkforms import Widget


__all__ = [
    "LIGHT",
    "DARK",
    "MetroBase",
    "Button",
    "ComboBox",
    "Label",
    "Panel",
    "Text",
]

LIGHT = "light"
DARK = "dark"


class MetroBase(Widget):
    @property
    def theme(self):
        style = self._widget.Theme
        if style == MetroThemeStyle.Light:
            return "light"
        elif style == MetroThemeStyle.Dark:
            return "dark"

    @theme.setter
    def theme(self, style):
        if style == "light":
            self._widget.Theme = MetroThemeStyle.Light
        elif style == "dark":
            self._widget.Theme = MetroThemeStyle.Dark


class Button(MetroBase):
    def __init__(self, *args, width=100, height=30, text="MetroControl.Button", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = MetroButton()

    @property
    def text(self):
        return self._widget.Text

    @text.setter
    def text(self, text: str):
        self._widget.Text = text


class ComboBox(MetroBase):
    def __init__(self, *args, width=100, height=30, text="MetroControl.ComboBox", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = MetroComboBox()

    @property
    def item_height(self):
        return self._widget.ItemHeight

    @item_height.setter
    def item_height(self, height):
        self._widget.ItemHeight = height

    def add(self, item: str):
        self._widget.Items.Add(item)

    def add_items(self, items: tuple):
        self._widget.Items.AddRange(items)

    def clear(self):
        self._widget.Items.Clear()

    def insert(self, index: int, item: str):
        self._widget.Items.Insert(index, item)

    def remove(self, item: str):
        self._widget.Items.Remove(item)

    def remove_at(self, index: int):
        self._widget.Items.RemoveAt(index)

    def count(self):
        return self._widget.Items.Count

    def index(self, item: str):
        return self._widget.Items.IndexOf(item)

    @property
    def text(self):
        return self._widget.PromptText

    @text.setter
    def text(self, text: str):
        self._widget.PromptText = text


class Label(MetroBase):
    def __init__(self, *args, width=100, height=30, text="MetroControl.Label", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = MetroLabel()

    @property
    def text(self):
        return self._widget.Text

    @text.setter
    def text(self, text: str):
        self._widget.Text = text


class Text(MetroBase):
    def __init__(self, *args, width=100, height=30, text="MetroControl.Label", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = MetroTextBox()

    @property
    def multiline(self):
        return self._widget.Multiline

    @multiline.setter
    def multiline(self, boolean):
        self._widget.Multiline = boolean

    @property
    def text(self):
        return self._widget.Text

    @text.setter
    def text(self, text: str):
        self._widget.Text = text


class Panel(MetroBase):
    def __init__(self, *args, width=100, height=30, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

    def _init_widget(self):
        self._widget = MetroPanel()


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()

    btn1 = Button(root, text="button1")
    btn1.pack(fill="both", expand="yes", padx=10, pady=10)

    btn2 = Button(root, text="button2")
    btn2.theme = 'dark'
    btn2.pack(fill="both", expand="yes", padx=10, pady=10)

    cbb1 = ComboBox(root)
    cbb1.add_items({"Item1", "Item2"})
    cbb1.clear()
    cbb1.add_items({"Item3", "Item4"})
    cbb1.insert(1, "Item5")
    cbb1.remove("Item5")
    cbb1.remove_at(1)
    cbb1.pack(fill="both", expand="yes", padx=10, pady=10)

    cbb2 = ComboBox(root)
    cbb2.theme = "dark"
    cbb2.add_items({"Item1", "Item2", "Item3", "Item4"})
    cbb2.pack(fill="both", expand="yes", padx=10, pady=10)

    text1 = Text(root)
    text1.multiline = True
    text1.pack(fill="both", expand="yes", padx=10, pady=10)

    root.mainloop()