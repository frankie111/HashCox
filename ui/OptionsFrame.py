import customtkinter

from ui.FileExplorer import FileExplorer
from ui.HashTypeWindow import HashTypeWindow
from ui.LabeledButton import LabeledButton
from ui.LabeledOptionMenu import LabeledOptionMenu
from ui.fonts import fonts


class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.hash_window = None
        self.device_type_var = customtkinter.StringVar(value="1 - CPU")
        self.workload_profile_var = customtkinter.StringVar(value="2 - Default")

        self.options_title_label = customtkinter.CTkLabel(self, text="Options", font=fonts.SECTION_TITLE)
        self.options_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.device_type_menu = LabeledOptionMenu(master=self, label_text="Device Type:",
                                                  label_font=fonts.DESCRIPTION_LABEL,
                                                  menu_values=["1 - CPU", "2 - GPU",
                                                               "3 - FPGA, DSP, Co-Processor"],
                                                  menu_default="1 - CPU",
                                                  menu_callback=self.device_type_menu_callback)
        self.device_type_menu.grid(column=0, row=1, sticky="w", padx=(10, 0))

        self.workload_profile_menu = LabeledOptionMenu(master=self,
                                                       label_text="Workload Profile:",
                                                       label_font=fonts.DESCRIPTION_LABEL,
                                                       menu_values=["1 - Low", "2 - Default", "3 - High",
                                                                    "4 - Nightmare"],
                                                       menu_default="2 - Default",
                                                       menu_callback=self.workload_profile_menu_callback)
        self.workload_profile_menu.grid(column=1, row=1, sticky="e", padx=(10, 0))

        self.hash_type_button = LabeledButton(master=self,
                                              label_text="Hash Type:",
                                              label_font=fonts.DESCRIPTION_LABEL,
                                              button_text="MD5",
                                              button_callback=self.open_hash_type_window)
        self.hash_type_button.grid(column=2, row=1, sticky="e", padx=(10, 0))

        self.hash_file_explorer = FileExplorer(master=self, label_text="Hash/Hash File",
                                               label_font=fonts.DESCRIPTION_LABEL,
                                               placeholder_text="Hash/Path to hash file",
                                               initial_dir="D:\\kit\\hashcat", dialog_title="Select Hash file",
                                               file_types=(("text files", "*.txt"), ("all files", "*.*")))
        self.hash_file_explorer.grid(column=0, row=2, columnspan=3, pady=10, padx=(10, 0))

    def device_type_menu_callback(self, selection):
        print(selection)

    def workload_profile_menu_callback(self, selection):
        print(selection)

    def open_hash_type_window(self):
        if self.hash_window is None or not self.hash_window.winfo_exists():
            self.hash_window = HashTypeWindow(
                selection_callback=self.change_button_text)  # create window if its None or destroyed

        self.hash_window.grab_set()  # Keep the window in focus

    def change_button_text(self):
        button_text_threshold = 16
        text = self.hash_window.hash_type_selection[1]
        trimmed_text = text[:button_text_threshold] if len(text) > button_text_threshold else text
        self.hash_type_button.button_var.set(trimmed_text)
