import customtkinter

from ui.FileExplorer import FileExplorer
from ui.LabeledOptionMenu import LabeledOptionMenu
from ui.fonts import fonts


class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
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
        self.workload_profile_menu.grid(column=1, row=1, sticky="e")

        # self.workload_label = customtkinter.CTkLabel(self, text="Workload Profile:", font=fonts.DESCRIPTION_LABEL)
        # self.workload_label.grid(column=2, row=1, padx=5, sticky="e")
        # self.workload_profile_menu = customtkinter.CTkOptionMenu(self, values=["1 - Low", "2 - Default", "3 - High",
        #                                                                        "4 - Nightmare"],
        #                                                          variable=self.workload_profile_var,
        #                                                          command=self.change_workload_profile_event)
        # self.workload_profile_menu.grid(column=3, row=1, sticky="w")

        self.hash_file_explorer = FileExplorer(master=self, label_text="Hash/Hash File",
                                               label_font=fonts.DESCRIPTION_LABEL,
                                               placeholder_text="Hash/Path to hash file",
                                               initial_dir="D:\\kit\\hashcat", dialog_title="Select Hash file",
                                               file_types=(("text files", "*.txt"), ("all files", "*.*")))
        self.hash_file_explorer.grid(column=0, row=2, columnspan=2, pady=10, padx=(10, 0), sticky="w")

    def device_type_menu_callback(self, selection):
        print(selection)

    def workload_profile_menu_callback(self, selection):
        print(selection)
