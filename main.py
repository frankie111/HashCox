import tkinter
from tkinter import filedialog, LEFT, TOP, CENTER

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self):
        super().__init__()

        # configure window
        self.title("HashCox - hashcat GUI")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.exec_selector_frame = ExecSelectorFrame(master=self, border_width=2)
        self.exec_selector_frame.grid(column=0, row=0, ipadx=10, ipady=5)


# Frame for selecting hashcat executable
class ExecSelectorFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.exec_file = None

        self.exec_title_label = customtkinter.CTkLabel(self, text="Hashcat Location",
                                                       font=("Roboto", 18, "bold"))
        self.exec_title_label.grid(column=0, row=0, columnspan=4, pady=5)

        self.exec_description_label = customtkinter.CTkLabel(self, text="Hashcat Executable:",
                                                             font=("Roboto", 14))
        self.exec_description_label.grid(column=0, row=1, padx=(10, 5))

        self.exec_entry = customtkinter.CTkEntry(self, width=300, placeholder_text="Path to hashcat "
                                                                                   "executable...")
        self.exec_entry.grid(column=1, row=1, padx=10)

        self.exec_browse_button = customtkinter.CTkButton(self, command=self.open_file_explorer_exec,
                                                          text="Browse...")
        self.exec_browse_button.grid(column=2, row=1)

        self.exec_save_checkbox = customtkinter.CTkCheckBox(self, text="Save Location")
        self.exec_save_checkbox.grid(column=3, row=1, padx=(10, 0))

    def open_file_explorer_exec(self):
        self.exec_browse_button.focus()
        self.exec_file = filedialog.askopenfilename(initialdir="D:\\kit\\hashcat",
                                                    title="Select the hashcat executable",
                                                    filetypes=(("executables", "*.exe"), ("all files", "*.*")))
        if self.exec_file != "":
            self.exec_entry.insert(0, self.exec_file)


if __name__ == '__main__':
    app = App()
    app.mainloop()
