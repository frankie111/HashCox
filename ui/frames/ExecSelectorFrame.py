# Frame for selecting hashcat executable

import customtkinter

from configuration.config import HASHCAT_HOME
from ui.Widgets.FileExplorerWidget import FileExplorerWidget
from ui.fonts import fonts


class ExecSelectorFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, preferences, **kwargs):
        super().__init__(master, **kwargs)

        self.preferences = preferences
        self.save_check_var = customtkinter.IntVar(value=1)

        self.exec_title_label = customtkinter.CTkLabel(self, text="Hashcat Location",
                                                       font=("Roboto", 18, "bold"))
        self.exec_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.exec_file_explorer = FileExplorerWidget(master=self, label_text="Hashcat Executable:",
                                                     label_font=fonts.DESCRIPTION_LABEL,
                                                     placeholder_text="Path to hashcat executable",
                                                     initial_dir=HASHCAT_HOME,
                                                     dialog_title="Select the hashcat executable",
                                                     file_types=(("executables", "*.exe"), ("all files", "*.*")))
        self.exec_file_explorer.file_text_variable.set(self.preferences.exec_location)
        self.exec_file_explorer.grid(column=0, row=1, columnspan=4, padx=(10, 0), pady=5)

        self.exec_save_checkbox = customtkinter.CTkCheckBox(self, text="Remember Location",
                                                            variable=self.save_check_var,
                                                            onvalue=1, offvalue=0)
        self.exec_save_checkbox.grid(column=3, row=2, sticky="e")

    def on_closing(self):
        # Save exec location if option is checked
        if self.save_check_var.get() and len(self.exec_file_explorer.file_text_variable.get()) != 0:
            self.preferences.exec_location = self.exec_file_explorer.file_text_variable.get()
