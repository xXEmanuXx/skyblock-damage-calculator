import customtkinter as ctk

import utils.helper as helper

class OutputSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text="Damage and stats display", font=helper.FONTS["small"])
        label.grid(row=0, column=0, padx=20, sticky="nsew")

        textbox = ctk.CTkTextbox(self)
        textbox.insert("0.0", "ciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\n")
        textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")