import clr
from tkforms.gunaui2 import gunaui2_lib
clr.AddReference(gunaui2_lib)
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
import pythonnet
from Guna.UI2.WinForms import Guna2Button, Guna2ComboBox, \
    Guna2Chip, Guna2CircleButton, \
    Guna2ControlBox, Guna2GradientButton, \
    Guna2TrackBar
from Guna.UI2.WinForms.Enums import TextBoxStyle
from System.Drawing import Color
from tkforms import Widget

DEFAULT = "default"
MATERIAL = "material"


__all__ = [
    "Button",
    "Chip",
    "CircleButton",
    "ComboBox",
    "ControlBox",
    "GradientButton",
    "TrackBar",
    "GunaBase"
]


class GunaBase(Widget):
    @property
    def auto_rounded(self):
        return self._widget.AutoRoundedCorners

    @auto_rounded.setter
    def auto_rounded(self, boolean: bool):
        self._widget.AutoRoundedCorners = boolean

    @property
    def animated(self):
        return self._widget.Animated

    @animated.setter
    def animated(self, boolean: bool):
        self._widget.Animated = boolean

    @property
    def border(self):
        return self._widget.BorderRadius

    @border.setter
    def border(self, radius: int):
        self._widget.BorderRadius = radius

    @property
    def fill(self):
        return self._widget.FillColor.ToArgb()

    @fill.setter
    def fill(self, color=[255, 255, 255, 255]):
        self._widget.FillColor = Color.FromArgb(color[0], color[1], color[2], color[3])

    @property
    def fill2(self):
        return self._widget.FillColor.ToArgb()

    @fill2.setter
    def fill2(self, color=[255, 255, 255, 255]):
        self._widget.FillColor2 = Color.FromArgb(color[0], color[1], color[2], color[3])

    @property
    def style(self):
        style = self._widget.Style
        if style == TextBoxStyle.Material:
            return "material"
        elif style == TextBoxStyle.Default:
            return "default"

    @style.setter
    def style(self, style: str):
        if style == "material":
            self._widget.Style = TextBoxStyle.Material
        elif style == "default":
            self._widget.Style = TextBoxStyle.Default


class Button(GunaBase):
    def __init__(self, *args, width=100, height=30, text="GunaUI2.Button", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = Guna2Button()

    @property
    def text(self):
        return self._widget.Text

    @text.setter
    def text(self, text: str):
        self._widget.Text = text


class Chip(Button):
    def _init_widget(self):
        self._widget = Guna2Chip()


class CircleButton(Button):
    def _init_widget(self):
        self._widget = Guna2CircleButton()


class ComboBox(GunaBase):
    def __init__(self, *args, width=100, height=30, text="MetroControl.ComboBox", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = Guna2ComboBox()

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


class ControlBox(Button):
    def _init_widget(self):
        self._widget = Guna2ControlBox()


class GradientButton(Button):
    def _init_widget(self):
        self._widget = Guna2GradientButton()


class TrackBar(GunaBase):
    def _init_widget(self):
        self._widget = Guna2TrackBar()

    def value_changed(self, func):
        self._widget.ValueChanged += func

    @property
    def value(self):
        return self._widget.Value

    @value.setter
    def value(self, value):
        self._widget.Value = value

    @property
    def maximum(self):
        return self._widget.Value

    @maximum.setter
    def maximum(self, value):
        self._widget.Maximum = value

    @property
    def minimum(self):
        return self._widget.Minimum

    @minimum.setter
    def minimum(self, value):
        self._widget.Minimum = value


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()

    def func1(_1, _2):
        print("click")

    btn1 = GradientButton()
    btn1.click(func1)
    btn1.animated = True
    btn1.pack(fill="x", ipadx=5, ipady=5, padx=5, pady=5)

    def func2(_1, _2):
        print(tbar1.value)

    tbar1 = TrackBar()
    tbar1.value_changed(func2)
    tbar1.minimum = -50
    tbar1.maximum = 50
    tbar1.value = 0

    tbar1.pack(fill="x", ipadx=5, ipady=5, padx=5, pady=5)

    root.mainloop()