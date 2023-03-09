import tkinter.ttk

import customtkinter


class HashTypeWindow(customtkinter.CTkToplevel):
    def __init__(self, width=600, height=400, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")
        self.title("Choose Hash Type")

        self.table = tkinter.ttk.Treeview(self, columns=("mode", "name", "category"), show="headings")
        self.table.heading("mode", text="Hash Mode")
        self.table.heading("name", text="Hash Name")
        self.table.heading("category", text="Hash Category")
        self.table.pack(fill="both", expand=True)


