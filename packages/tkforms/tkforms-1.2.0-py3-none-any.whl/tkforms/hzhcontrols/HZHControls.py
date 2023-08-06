import clr
from tkforms.hzhcontrols import hzh_controls_lib
clr.AddReference(hzh_controls_lib)
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from HZH_Controls.Controls import UCBtnExt
from System.Drawing import Color
from tkforms import Widget


class Button(Widget):
    def __init__(self, *args, width=100, height=30, text="HZHControls.Button", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = UCBtnExt()

    @property
    def text(self):
        return self._widget.BtnText

    @text.setter
    def text(self, text: str):
        self._widget.BtnText = text


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()

    btn1 = Button()
    btn1.fill = (255, 105, 231, 255)
    btn1.rect = (255, 105, 231, 255)
    btn1.pack(fill="x", ipadx=5, ipady=5, padx=5, pady=5)

    root.mainloop()