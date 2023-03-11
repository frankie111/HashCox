import customtkinter

from ui.fonts import fonts


class LabeledEntry(customtkinter.CTkFrame):
    def __init__(self, master: any, label_text, placeholder="", label_font=fonts.DESCRIPTION_LABEL, entry_width=200,
                 **kwargs):
        super().__init__(master, **kwargs)
        self.label_text = label_text
        self.label_font = label_font
        self.placeholder = placeholder
        self.label = customtkinter.CTkLabel(self, text=label_text, font=self.label_font)
        self.label.grid(column=0, row=0, padx=(10, 5))

        self.entry = customtkinter.CTkEntry(self, width=entry_width, placeholder_text=placeholder)
