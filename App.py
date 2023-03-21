import customtkinter

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
        self.title("HashCox - hashcat GUI")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(True, True)

        self.exec_selector_frame = ExecSelectorFrame(master=self, border_width=2)
        self.exec_selector_frame.grid(column=0, row=0, ipadx=10, ipady=5)

        self.options_frame = OptionsFrame(master=self, border_width=2)
        self.options_frame.grid(column=0, row=1, ipadx=10, ipady=5, pady=5, sticky="e")

        self.run_frame = RunFrame(master=self, run_callback=self.run_callback)
        self.run_frame.grid(column=0, row=2)

    def run_callback(self):
        hashcat_location = self.exec_selector_frame.exec_file_explorer.file_text_variable.get()
        hash_path = self.options_frame.hash_file_explorer.file_text_variable.get()
        hash_type = self.options_frame.hash_type
        device_type = self.options_frame.device_type_var.get()
        workload_profile = self.options_frame.workload_profile_var.get()

        print(hashcat_location)
        print(hash_type)
        print(hash_path)
        print(device_type)
        print(workload_profile)
        pass


if __name__ == '__main__':
    app = App()
    app.mainloop()
