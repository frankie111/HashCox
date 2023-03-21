import customtkinter

from ui.fonts import fonts


class LabeledOptionMenu(customtkinter.CTkFrame):
    def __init__(self, label_text, menu_values, menu_default, menu_callback, master: any,
                 label_font=fonts.DESCRIPTION_LABEL, **kwargs):
        super().__init__(master, **kwargs)
        self.menu_var = customtkinter.StringVar(value=menu_default)
        self.menu_callback = menu_callback

        self.label = customtkinter.CTkLabel(self, text=label_text, font=label_font)
        self.label.grid(column=0, row=0, padx=(0, 10))

        self.menu = customtkinter.CTkOptionMenu(self, dynamic_resizing=False, values=menu_values, variable=self.menu_var,
                                                command=self.menu_callback)
        self.menu.grid(column=1, row=0)
