import customtkinter


class LabeledOptionMenu(customtkinter.CTkFrame):
    def __init__(self, label_text, label_font, menu_values, menu_default, menu_callback, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.menu_var = customtkinter.StringVar(value=menu_default)
        self.menu_callback = menu_callback

        self.label = customtkinter.CTkLabel(self, text=label_text, font=label_font)
        self.label.grid(column=0, row=0, padx=(0, 10))

        self.menu = customtkinter.CTkOptionMenu(self, values=menu_values, variable=self.menu_var,
                                                command=self.menu_callback)
        self.menu.grid(column=1, row=0)
