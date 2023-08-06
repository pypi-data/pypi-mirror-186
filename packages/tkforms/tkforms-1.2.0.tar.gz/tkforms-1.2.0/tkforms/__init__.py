import clr
clr.AddReference("System.Drawing")
from System.Drawing import Point, Size, Color, Font

from tkinter import Frame


class Widget(Frame):
    def __init__(self, *args, width=100, height=30, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        self._init_widget()
        self.bind("<Configure>", self._configure_widget)
        self.bind("<Map>", self._map)
        self.bind("<Unmap>", self._unmap)
        self.tk_forms(self, self._widget)
        self._widget.Visible = False

    def widget(self):
        return self._widget

    def click(self, func):
        self._widget.Click += func

    def double_click(self, func):
        self._widget.DoubleClick += func

    def enter(self, func):
        self._widget.MouseEnter += func

    def leave(self, func):
        self._widget.MouseLeave += func

    def buttondown(self, func):
        self._widget.MouseDown += func

    def buttonup(self, func):
        self._widget.MouseUp += func

    def tk_forms(self, parent, child):  # 将Winform组件添加入Tkinter组件
        from ctypes import windll
        windll.user32.SetParent(int(str(child.Handle)),
                                windll.user32.GetParent(parent.winfo_id()))  # 调用win32设置winform组件的父组件

    def forms_tk(self, parent, child):  # 将Winform组件添加入Tkinter组件
        from ctypes import windll
        windll.user32.SetParent(windll.user32.GetParent(child.winfo_id()),
                                int(str(parent.Handle)))  # 调用win32设置tkinter组件的父组件

    @property
    def fill(self):
        return self._widget.FillColor.ToArgb()

    @fill.setter
    def fill(self, color=[255, 255, 255, 255]):
        self._widget.FillColor = Color.FromArgb(color[0], color[1], color[2], color[3])

    @property
    def rect(self):
        return self._widget.RectColor.ToArgb()

    @rect.setter
    def rect(self, color=[255, 255, 255, 255]):
        self._widget.RectColor = Color.FromArgb(color[0], color[1], color[2], color[3])

    def font(self, name: str = "Sego UI", size: int = 9):
        try:
            font = Font(name, size)
        except TypeError:
            pass
        else:
            self._widget.Font = font

    def _map(self, _=None):
        self._widget.Visible = True

    def _unmap(self, _=None):
        self._widget.Visible = False

    def _configure_widget(self, _=None):
        self._widget.Location = Point(self.winfo_x(), self.winfo_y())
        self._widget.Size = Size(self.winfo_width(), self.winfo_height())

    def _init_widget(self):
        _widget = None


from tkforms.metroframework import MetroUI as tkmetro
from tkforms.gunaui2 import GunaUI2 as tkguna