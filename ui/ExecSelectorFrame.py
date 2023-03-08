# Frame for selecting hashcat executable
from tkinter import filedialog

import customtkinter

from ui.FileExplorer import FileExplorer
from ui.fonts import fonts


class ExecSelectorFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        # self.exec_file = ""
        self.check_var = customtkinter.IntVar(value=1)

        self.exec_title_label = customtkinter.CTkLabel(self, text="Hashcat Location",
                                                       font=("Roboto", 18, "bold"))
        self.exec_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.exec_file_explorer = FileExplorer(master=self, label_text="Hashcat Executable:",
                                               label_font=fonts.DESCRIPTION_LABEL,
                                               placeholder_text="Path to hashcat executable",
                                               initial_dir="D:\\kit\\hashcat",
                                               dialog_title="Select the hashcat executable",
                                               file_types=(("executables", "*.exe"), ("all files", "*.*")))
        self.exec_file_explorer.grid(column=0, row=1, columnspan=4, padx=(10, 0), pady=10)

        # self.exec_description_label = customtkinter.CTkLabel(self, text="Hashcat Executable:",
        #                                                      font=("Roboto", 14))
        # self.exec_description_label.grid(column=0, row=1, padx=(10, 5))
        #
        # self.exec_entry = customtkinter.CTkEntry(self, width=300, placeholder_text="Path to hashcat "
        #                                                                            "executable...")
        # self.exec_entry.grid(column=1, row=1, padx=10)
        #
        # self.exec_browse_button = customtkinter.CTkButton(self, command=self.open_file_explorer_exec,
        #                                                   text="Browse...")
        # self.exec_browse_button.grid(column=2, row=1)

        self.exec_save_checkbox = customtkinter.CTkCheckBox(self, text="Remember Location", variable=self.check_var,
                                                            onvalue=1, offvalue=0)
        self.exec_save_checkbox.grid(column=3, row=2, padx=(10, 0))

    # def open_file_explorer_exec(self):
    #     self.exec_browse_button.focus()
    #     self.exec_file = filedialog.askopenfilename(initialdir="D:\\kit\\hashcat",
    #                                                 title="Select the hashcat executable",
    #                                                 filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    #     if self.exec_file != "":
    #         self.exec_entry.insert(0, self.exec_file)
