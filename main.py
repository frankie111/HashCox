import customtkinter

from ui.ExecSelectorFrame import ExecSelectorFrame
from ui.OptionsFrame import OptionsFrame

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    width = 800
    height = 600

    def __init__(self):
        super().__init__()

        # configure window
        self.title("HashCox - hashcat GUI")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.exec_selector_frame = ExecSelectorFrame(master=self, border_width=2)
        self.exec_selector_frame.grid(column=0, row=0, ipadx=10, ipady=5)

        self.options_frame = OptionsFrame(master=self, border_width=2)
        self.options_frame.grid(column=0, row=1, ipadx=10, ipady=5, pady=10)


if __name__ == '__main__':
    app = App()
    app.mainloop()
