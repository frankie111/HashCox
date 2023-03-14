import customtkinter

from ui.colors import colors
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
        self.entry.grid(column=1, row=0)

    def enable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.NORMAL)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_ACTIVE)

    def disable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.DISABLED)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
