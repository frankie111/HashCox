import customtkinter


class RunFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.text_var = customtkinter.StringVar(master=self, value="")

        self.log = customtkinter.CTkEntry(master=self, width=600, textvariable=self.text_var)
        self.log.grid(column=0, row=0, padx=5)

        self.run_button = customtkinter.CTkButton(master=self, text="Run", )
        self.run_button.grid(column=1, row=0)
