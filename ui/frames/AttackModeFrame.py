import customtkinter

from configuration.config import HASHCAT_HOME
from ui.fonts import fonts
from ui.frames.BruteForceFrame import BruteForceFrame
from ui.Widgets.FileExplorerWidget import FileExplorerWidget
from ui.colors import colors


class AttackModeFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.radio_var = customtkinter.IntVar(value=1)

        self.title_label = customtkinter.CTkLabel(self, text="Attack Mode", font=fonts.SECTION_TITLE)
        self.title_label.grid(column=0, row=0, pady=5)

        self.dict_radiobutton = customtkinter.CTkRadioButton(self, text="Dictionary", variable=self.radio_var,
                                                             value=1, command=self.dict_radio_callback)
        self.dict_radiobutton.grid(column=0, row=1, sticky="w", pady=10, padx=10)

        self.dict_file_explorer = FileExplorerWidget(master=self,
                                                     label_text="Dictionary File:",
                                                     placeholder_text="Path to dictionary file",
                                                     initial_dir=HASHCAT_HOME,
                                                     dialog_title="Select dictionary file",
                                                     file_types=(("text files", "*.txt"), ("all files", "*.*")),
                                                     fg_color=colors.GRAY16
                                                     )
        self.dict_file_explorer.grid(column=0, row=2, pady=10, padx=10)

        self.brute_radiobutton = customtkinter.CTkRadioButton(master=self, text="Brute-Force", variable=self.radio_var,
                                                              value=2, command=self.brute_radio_callback)
        self.brute_radiobutton.grid(column=0, row=3, sticky="w", pady=10, padx=10)

        self.brute_force_frame = BruteForceFrame(master=self, fg_color=colors.GRAY16)
        self.brute_force_frame.disable()
        self.brute_force_frame.grid(column=0, row=4, sticky="w", padx=10)

    def dict_radio_callback(self):
        self.dict_file_explorer.enable()
        self.brute_force_frame.disable()

    def brute_radio_callback(self):
        self.dict_file_explorer.disable()
        self.brute_force_frame.enable()
