# Frame for selecting hashcat executable

import customtkinter

from configuration.config import HASHCAT_HOME
from ui.Widgets.FileExplorerWidget import FileExplorerWidget
from ui.fonts import fonts


class ExecSelectorFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        # self.exec_file = ""
        self.check_var = customtkinter.IntVar(value=1)

        self.exec_title_label = customtkinter.CTkLabel(self, text="Hashcat Location",
                                                       font=("Roboto", 18, "bold"))
        self.exec_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.exec_file_explorer = FileExplorerWidget(master=self, label_text="Hashcat Executable:",
                                                     label_font=fonts.DESCRIPTION_LABEL,
                                                     placeholder_text="Path to hashcat executable",
                                                     initial_dir=HASHCAT_HOME,
                                                     dialog_title="Select the hashcat executable",
                                                     file_types=(("executables", "*.exe"), ("all files", "*.*")))
        self.exec_file_explorer.grid(column=0, row=1, columnspan=4, padx=(10, 0), pady=10)

        self.exec_save_checkbox = customtkinter.CTkCheckBox(self, text="Remember Location", variable=self.check_var,
                                                            onvalue=1, offvalue=0)
        self.exec_save_checkbox.grid(column=3, row=2, padx=(10, 0))
