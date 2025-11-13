import customtkinter as ctk

from ui.sections.input_section import InputSection
from ui.sections.control_section import ControlSection
from ui.sections.output_section import OutputSection

class MainContent(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=("#ffffff", "#1e1e1e"), corner_radius=0)

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        input_section = InputSection(self)
        input_section.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="nsew")

        control_section = ControlSection(self)
        control_section.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        output_section = OutputSection(self)
        output_section.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

