import tkinter.ttk

import customtkinter

from data import cleanData
from ui.colors import colors


class HashTypeWindow(customtkinter.CTkToplevel):
    def __init__(self, width=600, height=400, selection_callback=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selection_callback = selection_callback
        self.hash_type_selection = 0
        self.data = cleanData.get_data_as_list_tuple()

        self.width = width
        self.height = height
        self.geometry(f"{self.width}x{self.height}")
        self.title("Choose Hash Type")

        self.table = tkinter.ttk.Treeview(self, columns=("mode", "name", "category"), show="headings",
                                          selectmode="browse")

        style = tkinter.ttk.Style(self.table)
        style.theme_use("clam")
        style.configure("Treeview", background=colors.DARK_GRAY3, fieldbackground="black", foreground=colors.LIGHT_GRAY)
        style.configure("Treeview.Heading", background=colors.DARK_GRAY2, foreground=colors.LIGHT_GRAY)

        self.table.heading("mode", text="Hash Mode")
        self.table.heading("name", text="Hash Name")
        self.table.heading("category", text="Hash Category")
        self.table.pack(fill="both", expand=True)

        for mode, name, category in self.data:
            self.table.insert(parent='', index=customtkinter.END, values=(mode, name, category))

        # events
        def item_select(_):
            for i in self.table.selection():
                self.hash_type_selection = self.table.item(i)["values"]

            if selection_callback is not None:
                selection_callback()

        def item_double_click(_):
            self.destroy()

        self.table.bind('<<TreeviewSelect>>', item_select)
        self.table.bind('<Double-1>', item_double_click)
