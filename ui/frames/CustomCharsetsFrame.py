import customtkinter

from ui.Widgets.LabeledEntry import LabeledEntry
from ui.colors import colors


class CustomCharsetsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color=colors.GRAY16, border_width=2)

        self.entries = []
        for i in range(0, 4):
            self.entries.append(LabeledEntry(master=self,
                                             label_text=f"Charset #{i + 1}",
                                             fg_color=colors.GRAY16,
                                             placeholder="123abc?!"))
            self.entries[i].grid(column=0, row=i)

        self.disable()

    def enable(self):
        for entry in self.entries:
            entry.enable()

    def disable(self):
        for entry in self.entries:
            entry.disable()
