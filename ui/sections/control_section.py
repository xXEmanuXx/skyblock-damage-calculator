import customtkinter as ctk

from utils.tooltip import Tooltip
import utils.helper as helper

class ControlSection(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        control_label = ctk.CTkLabel(self, text="Controls", font=helper.FONTS["small"])
        control_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        dps_checkbox = ctk.CTkCheckBox(self, text="DPS", corner_radius=0)
        dps_checkbox.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        Tooltip(dps_checkbox, "Whether or not show dps in damage calculations")

        non_crit_checkbox = ctk.CTkCheckBox(self, text="Non Crit", corner_radius=0)
        non_crit_checkbox.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        Tooltip(non_crit_checkbox, "Whether or not show non critical damage")

        dungeon_checkbox = ctk.CTkCheckBox(self, text="Dungeon", corner_radius=0)
        dungeon_checkbox.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        Tooltip(dungeon_checkbox, "Whether damage is calculated inside dungeons")

        stats_button = ctk.CTkButton(self, text="Update Stats", corner_radius=0)
        stats_button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        damage_button = ctk.CTkButton(self, text="Calculate Damage", corner_radius=0)
        damage_button.grid(row=6, column=0, columnspan=2, padx=20, pady=20, ipadx=20, ipady=20)