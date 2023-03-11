import customtkinter

from ui.Widgets.LabeledEntry import LabeledEntry


class CustomCharsetsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.entry1 = LabeledEntry(master=self, label_text="Charset #1")
        self.entry1.grid(column=0, row=0)
        self.entry2 = LabeledEntry(master=self, label_text="Charset #2")
        self.entry1.grid(column=0, row=1)
        self.entry3 = LabeledEntry(master=self, label_text="Charset #3")
        self.entry1.grid(column=0, row=2)
        self.entry4 = LabeledEntry(master=self, label_text="Charset #4")
        self.entry1.grid(column=0, row=3)
