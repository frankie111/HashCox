from tkinter import filedialog

import customtkinter

from ui.colors import colors
from ui.fonts import fonts


class FileExplorerWidget(customtkinter.CTkFrame):
    def __init__(self, label_text, placeholder_text, initial_dir, dialog_title,
                 file_types, master: any, label_font=fonts.DESCRIPTION_LABEL,
                 fg_color=colors.GRAY13,
                 **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=fg_color)
        self.file_text_variable = customtkinter.StringVar(value="")
        self.initial_dir = initial_dir
        self.dialog_title = dialog_title
        self.file_types = file_types
        self.description_label = customtkinter.CTkLabel(self, text=label_text, font=label_font)
        self.description_label.grid(column=0, row=0, padx=(10, 5))

        self.entry = customtkinter.CTkEntry(self, width=300, placeholder_text=placeholder_text,
                                            textvariable=self.file_text_variable)
        self.entry.grid(column=1, row=0, padx=10)

        self.browse_button = customtkinter.CTkButton(self, command=self.button_callback, text="Browse...")
        self.browse_button.grid(column=2, row=0)

    def button_callback(self):
        self.browse_button.focus()
        self.file_text_variable.set(filedialog.askopenfilename(initialdir=self.initial_dir, title=self.dialog_title,
                                                               filetypes=self.file_types))

        # if self.file_text_variable.get() == "":
        #     self.entry.insert(0, self.file)

    def enable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.NORMAL)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_ACTIVE)

    def disable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.DISABLED)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
