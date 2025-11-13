import customtkinter as ctk

from ui.sections.tabs.weapon_tab import WeaponTab

class InputSection(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.add("Weapon")
        self.add("Gear")
        self.add("Magical Power")
        self.add("Miscellaneous")

        self.weapon_tab = WeaponTab(self.tab("Weapon"))
        self.weapon_tab.grid(row=0, column=0)
