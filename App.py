import os

import customtkinter

from logic import commandBuilder
from repo import PreferencesRepo
from ui.frames.ExecSelectorFrame import ExecSelectorFrame
from ui.frames.OptionsFrame import OptionsFrame
from ui.frames.RunFrame import RunFrame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    width = 800
    height = 660

    def __init__(self):
        super().__init__()

        # configure window
        self.preferences = PreferencesRepo.load()
        self.title("HashCox - hashcat GUI")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(True, True)

        self.exec_selector_frame = ExecSelectorFrame(master=self, preferences=self.preferences,
                                                     border_width=2)
        self.exec_selector_frame.grid(column=0, row=0, ipadx=10, ipady=5)

        self.options_frame = OptionsFrame(master=self, border_width=2)
        self.options_frame.grid(column=0, row=1, ipadx=10, ipady=5, pady=5, sticky="e")

        self.run_frame = RunFrame(master=self, run_callback=self.run_callback)
        self.run_frame.grid(column=0, row=2)

        self.potfile_check_var = customtkinter.IntVar(value=0)
        self.disable_potfile_checkbox = customtkinter.CTkCheckBox(self, text="Disable Potfile",
                                                                  variable=self.potfile_check_var,
                                                                  onvalue=1, offvalue=0)

        self.disable_potfile_checkbox.grid(column=0, row=3, sticky="e", padx=(0, 35), pady=(5, 0))
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.exec_selector_frame.on_closing()
        PreferencesRepo.save(self.preferences)
        self.destroy()

    def run_callback(self):
        command = commandBuilder.build_command(self)
        os.system(f'start cmd /k "{command}"')


if __name__ == '__main__':
    app = App()
    app.mainloop()
