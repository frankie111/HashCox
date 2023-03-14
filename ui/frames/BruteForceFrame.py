from tkinter import LEFT

import customtkinter
from custom_hovertip import CustomTooltipLabel

from ui.colors import colors
from ui.fonts import fonts
from ui.frames.CustomCharsetsFrame import CustomCharsetsFrame


class BruteForceFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.radio_var = customtkinter.IntVar(value=1)

        self.alpha_lower_radiobutton = customtkinter.CTkRadioButton(master=self,
                                                                    text="Lower Alpha (a..z)",
                                                                    variable=self.radio_var,
                                                                    value=1,
                                                                    command=self.alpha_lower_callback)
        self.alpha_lower_radiobutton.grid(column=0, row=0, sticky="w")

        self.alpha_upper_radiobutton = customtkinter.CTkRadioButton(master=self,
                                                                    text="Upper Alpha (A..Z)",
                                                                    variable=self.radio_var,
                                                                    value=2,
                                                                    command=self.alpha_upper_callback)
        self.alpha_upper_radiobutton.grid(column=0, row=1, sticky="w")

        self.numeric_radiobutton = customtkinter.CTkRadioButton(master=self,
                                                                text="Numeric (0..9)",
                                                                variable=self.radio_var,
                                                                value=3,
                                                                command=self.numeric_radio_callback)
        self.numeric_radiobutton.grid(column=0, row=2, sticky="w")

        self.custom_mask_radiobutton = customtkinter.CTkRadioButton(master=self,
                                                                    text="Custom Mask",
                                                                    variable=self.radio_var,
                                                                    value=4,
                                                                    command=self.custom_mask_radio_callback)
        self.custom_mask_radiobutton.grid(column=0, row=3, sticky="w")

        self.mask_tooltip = CustomTooltipLabel(anchor_widget=self.custom_mask_radiobutton,
                                               text="l = a-z\nu = A-Z\nd = 0-9\n"
                                                    "h = 0-9,a-f\nH = 0-9,A-F\n"
                                                    "s = !\"#$%&'()*+,~ ...\n"
                                                    "a = l,u,d,s",
                                               background=colors.GRAY_ENTRY_ACTIVE,
                                               foreground=colors.WHITE,
                                               width=18,
                                               justify=LEFT,
                                               font=fonts.TOOLTIP)

        self.mask_entry = customtkinter.CTkEntry(master=self,
                                                 width=200,
                                                 placeholder_text="?d" * 8)
        self.mask_entry.grid(column=0, row=4, sticky="w", padx=(25, 0))

        self.custom_charsets_frame = CustomCharsetsFrame(master=self)
        self.custom_charsets_frame.grid(column=1, row=0, rowspan=4)

    def alpha_lower_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
        self.mask_entry.configure(state=customtkinter.DISABLED)

    def alpha_upper_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
        self.mask_entry.configure(state=customtkinter.DISABLED)

    def numeric_radio_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
        self.mask_entry.configure(state=customtkinter.DISABLED)

    def custom_mask_radio_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_ACTIVE)
        self.mask_entry.configure(state=customtkinter.NORMAL)

    def enable(self):
        for child in self.winfo_children():
            if child.widgetName != 'frame':  # frame has no state, so skip
                child.configure(state='normal')

        self.custom_charsets_frame.enable()

        if self.radio_var != 4:
            self.mask_entry.configure(state=customtkinter.DISABLED, fg_color=colors.GRAY_ENTRY_DISABLED)
        else:
            self.mask_entry.configure(state=customtkinter.NORMAL, fg_color=colors.GRAY_ENTRY_ACTIVE)

    def disable(self):
        for child in self.winfo_children():
            if child.widgetName != 'frame':  # frame has no state, so skip
                child.configure(state='disabled')
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED)
        self.custom_charsets_frame.disable()
