from tkinter import filedialog

import customtkinter


class FileExplorer(customtkinter.CTkFrame):
    def __init__(self, label_text, label_font, placeholder_text, initial_dir, dialog_title, file_types, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.file = ""
        self.initial_dir = initial_dir
        self.dialog_title = dialog_title
        self.file_types = file_types
        self.description_label = customtkinter.CTkLabel(self, text=label_text, font=label_font)
        self.description_label.grid(column=0, row=0, padx=(10, 5))

        self.entry = customtkinter.CTkEntry(self, width=300, placeholder_text=placeholder_text)
        self.entry.grid(column=1, row=0, padx=10)

        self.browse_button = customtkinter.CTkButton(self, command=self.button_callback, text="Browse...")
        self.browse_button.grid(column=2, row=0)

    def button_callback(self):
        self.browse_button.focus()
        self.file = filedialog.askopenfilename(initialdir=self.initial_dir, title=self.dialog_title,
                                               filetypes=self.file_types)
        if self.file != "":
            self.entry.insert(0, self.file)
