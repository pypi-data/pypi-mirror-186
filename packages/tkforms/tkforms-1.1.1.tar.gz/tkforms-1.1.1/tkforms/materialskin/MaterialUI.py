import clr
from tkforms.materialskin import material_lib
clr.AddReference(material_lib)
clr.AddReference("System.Windows.Forms")
from MaterialSkin.Controls import MaterialButton
from tkforms import Widget


class Button(Widget):
    def __init__(self, *args, width=100, height=30, text="MaterialControl.Button", **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self.text = text

    def _init_widget(self):
        self._widget = MaterialButton()

    @property
    def text(self):
        return self._widget.Text

    @text.setter
    def text(self, text: str):
        self._widget.Text = text


if __name__ == '__main__':
    from tkinter import Tk
    root = Tk()
    btn1 = Button(root)
    btn1.pack(fill="both", expand="yes", padx=10, pady=10)
    btn2 = Button(root)
    btn2.pack(fill="both", expand="yes", padx=10, pady=10)
    root.mainloop()