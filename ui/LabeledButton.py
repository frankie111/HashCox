import customtkinter


class LabeledButton(customtkinter.CTkFrame):
    def __init__(self, master: any, label_text, label_font, button_text="", button_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.button_var = customtkinter.StringVar(value=button_text)
        self.label_text = label_text
        self.label_font = label_font
        self.button_callback = button_callback
        self.description_label = customtkinter.CTkLabel(self, text=self.label_text, font=self.label_font)
        self.description_label.grid(column=0, row=0, padx=(10, 5))

        self.button = customtkinter.CTkButton(self, command=self.button_callback, textvariable=self.button_var)
        self.button.grid(column=1, row=0)
