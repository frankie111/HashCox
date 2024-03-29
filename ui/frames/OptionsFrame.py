import customtkinter

from configuration.config import HASHCAT_HOME
from ui.Widgets.FileExplorerWidget import FileExplorerWidget
from ui.Widgets.LabeledButton import LabeledButton
from ui.Widgets.LabeledOptionMenu import LabeledOptionMenu
from ui.fonts import fonts
from ui.frames.AttackModeFrame import AttackModeFrame
from ui.windows.HashTypeWindow import HashTypeWindow


class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.hash_type = 0
        self.hash_window = None
        self.device_type_var = customtkinter.StringVar(value="1 - CPU")
        self.workload_profile_var = customtkinter.StringVar(value="2 - Default")

        self.title_label = customtkinter.CTkLabel(self, text="Options", font=fonts.SECTION_TITLE)
        self.title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.device_type_menu = LabeledOptionMenu(master=self, label_text="Device Type:",
                                                  menu_values=["1 - CPU", "2 - GPU",
                                                               "3 - FPGA, DSP, Co-Processor"],
                                                  menu_default="1 - CPU",
                                                  menu_callback=self.device_type_menu_callback,
                                                  )
        self.device_type_menu.grid(column=0, row=1, padx=(10, 0))

        self.workload_profile_menu = LabeledOptionMenu(master=self,
                                                       label_text="Workload Profile:",
                                                       menu_values=["1 - Low", "2 - Default", "3 - High",
                                                                    "4 - Nightmare"],
                                                       menu_default="2 - Default",
                                                       menu_callback=self.workload_profile_menu_callback)
        self.workload_profile_menu.grid(column=1, row=1, padx=(10, 0))

        self.hash_type_button = LabeledButton(master=self,
                                              label_text="Hash Type:",
                                              button_text="MD5",
                                              button_callback=self.open_hash_type_window)
        self.hash_type_button.grid(column=2, row=1, padx=(10, 0))

        self.hash_file_explorer = FileExplorerWidget(master=self, label_text="Hash/Hash File:",
                                                     placeholder_text="Hash/Path to hash file",
                                                     initial_dir=HASHCAT_HOME,
                                                     dialog_title="Select Hash file",
                                                     file_types=(("text files", "*.txt"), ("all files", "*.*")))
        self.hash_file_explorer.grid(column=0, row=2, columnspan=3, pady=10, padx=(20, 0))

        self.attack_mode_frame = AttackModeFrame(self, border_width=2)
        self.attack_mode_frame.grid(column=0, row=3, columnspan=3, padx=10, ipadx=10, ipady=10)

    def device_type_menu_callback(self, selection):
        self.device_type_var.set(selection)

    def workload_profile_menu_callback(self, selection):
        self.workload_profile_var.set(selection)

    def open_hash_type_window(self):
        if self.hash_window is None or not self.hash_window.winfo_exists():
            self.hash_window = HashTypeWindow(
                selection_callback=self.change_button_text)  # create window if its None or destroyed

        self.hash_window.grab_set()  # Keep the window in focus

    def change_button_text(self):
        self.hash_type = self.hash_window.hash_type_selection[0]
        button_text_threshold = 16
        text = self.hash_window.hash_type_selection[1]
        trimmed_text = text[:button_text_threshold] if len(text) > button_text_threshold else text
        self.hash_type_button.button_var.set(trimmed_text)
