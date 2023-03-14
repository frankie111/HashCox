import customtkinter

from ui.Widgets.IntSpinbox import IntSpinbox
from ui.colors import colors
from ui.fonts import fonts


class LabeledSpinbox(customtkinter.CTkFrame):
    def __init__(self, master: any, label_text="label text", label_font=fonts.DESCRIPTION_LABEL, default_value=0,
                 min_value=-100,
                 max_value=100, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=colors.GRAY16)
        self.label_text = label_text
        self.label_font = label_font

        self.label = customtkinter.CTkLabel(self, text=self.label_text, font=self.label_font)
        self.label.grid(column=0, row=0, padx=(0, 10))

        self.spinbox = IntSpinbox(master=self, default_value=default_value, min_value=min_value, max_value=max_value)
        self.spinbox.grid(column=1, row=0)

    def enable(self):
        self.label.configure(state=customtkinter.NORMAL)
        self.spinbox.enable()

    def disable(self):
        self.label.configure(state=customtkinter.DISABLED)
        self.spinbox.disable()
