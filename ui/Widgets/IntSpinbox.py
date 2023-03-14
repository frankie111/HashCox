from typing import Callable, Union

import customtkinter

from ui.colors import colors


class IntSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int = 1,
                 command: Callable = None,
                 default_value: int = 0,
                 min_value: int = -100,
                 max_value: int = 100,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command
        self.min_value = min_value
        self.max_value = max_value

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height - 6, height=height - 6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width - (2 * height), height=height - 6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height - 6, height=height - 6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, str(default_value))

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        if int(self.entry.get()) != self.max_value:
            try:
                value = int(self.entry.get()) + self.step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
            except ValueError:
                return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        if int(self.entry.get()) != self.min_value:
            try:
                value = int(self.entry.get()) - self.step_size
                self.entry.delete(0, "end")
                self.entry.insert(0, value)
            except ValueError:
                return

    def get(self) -> Union[int, None]:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))

    def enable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.NORMAL)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_ACTIVE)

    def disable(self):
        for child in self.winfo_children():
            child.configure(state=customtkinter.DISABLED)
        self.entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
