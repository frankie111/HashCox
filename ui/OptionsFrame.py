import customtkinter


class OptionsFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.options_title_label = customtkinter.CTkLabel(self, text="Options", font=("Roboto", 18, "bold"))
        self.options_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.device_type_selector = customtkinter.CTkOptionMenu(self, values=["1 - CPU", "2 - GPU",
                                                                              "3 - FPGA, DSP, Co-Processor"],
                                                                command=self.change_device_type_event)
        self.device_type_selector.grid(column=0, row=1)

    def change_device_type_event(self, selection):
        print(selection)
