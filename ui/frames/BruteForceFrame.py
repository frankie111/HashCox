from tkinter import LEFT

import customtkinter
from custom_hovertip import CustomTooltipLabel

from ui.Widgets.LabeledSpinbox import LabeledSpinbox
from ui.colors import colors
from ui.fonts import fonts
from ui.frames.CustomCharsetsFrame import CustomCharsetsFrame


class BruteForceFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.min_password_len = 1
        self.max_password_len = 40

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

        self.min_len_spinbox = LabeledSpinbox(master=self, label_text="min password length:", default_value=6,
                                              min_value=self.min_password_len,
                                              max_value=self.max_password_len)
        self.min_len_spinbox.grid(column=0, row=5, rowspan=2, sticky="w", padx=(10, 20), pady=10)

        self.max_len_spinbox = LabeledSpinbox(master=self, label_text="max password length:", default_value=8,
                                              min_value=self.min_password_len,
                                              max_value=self.max_password_len)
        self.max_len_spinbox.grid(column=1, row=5, rowspan=2, sticky="w", pady=10)

    def alpha_lower_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED, state=customtkinter.DISABLED)
        self.custom_charsets_frame.disable()

    def alpha_upper_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED, state=customtkinter.DISABLED)
        self.custom_charsets_frame.disable()

    def numeric_radio_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED, state=customtkinter.DISABLED)
        self.custom_charsets_frame.disable()

    def custom_mask_radio_callback(self):
        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_ACTIVE, state=customtkinter.NORMAL)
        self.custom_charsets_frame.enable()

    def enable(self):
        for radio_button in self.alpha_upper_radiobutton, \
                self.alpha_lower_radiobutton, \
                self.numeric_radiobutton, \
                self.custom_mask_radiobutton:
            radio_button.configure(state='normal')

        if self.radio_var.get() == 4:
            self.mask_entry.configure(state=customtkinter.NORMAL, fg_color=colors.GRAY_ENTRY_ACTIVE)
            self.custom_charsets_frame.enable()
        else:
            self.mask_entry.configure(state=customtkinter.DISABLED, fg_color=colors.GRAY_ENTRY_DISABLED)
            self.custom_charsets_frame.disable()

        self.min_len_spinbox.enable()
        self.max_len_spinbox.enable()

    def disable(self):
        for radio_button in self.alpha_upper_radiobutton, \
                self.alpha_lower_radiobutton, \
                self.numeric_radiobutton, \
                self.custom_mask_radiobutton:
            radio_button.configure(state='disabled')

        self.mask_entry.configure(fg_color=colors.GRAY_ENTRY_DISABLED,
                                  state='disabled')
        self.custom_charsets_frame.disable()
        self.min_len_spinbox.disable()
        self.max_len_spinbox.disable()
