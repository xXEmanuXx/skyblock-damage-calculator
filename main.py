import customtkinter as ctk

from tooltip import Tooltip 
from combobox import SearchableComboBox
import utils

WIDTH, HEIGHT = 1200, 700


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.fonts = {
            "big": ctk.CTkFont("Segoe UI", 18, "bold"),
            "small": ctk.CTkFont("Segoe UI", 13, "bold")
        }

        
        
        self.title("Hypixel Skyblock Damage Calculator")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform="main")  # sidebar (1/6)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=5, uniform="main")  # content_melee (5/6)

        self.sidebar = ctk.CTkFrame(self, corner_radius=0, fg_color=("#E7E9EC", "#141414"))
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.sidebar.grid_rowconfigure(4, weight=1)
        self.sidebar.grid_columnconfigure(0, weight=1)

        self.sidebar_title = ctk.CTkLabel(self.sidebar, text="Settings", font=self.fonts["big"])
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=(20, 70))

        self.sidebar_melee_button = ctk.CTkButton(self.sidebar, text="Melee Damage", command=lambda: self.show_content("melee"))
        self.sidebar_melee_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_magic_button = ctk.CTkButton(self.sidebar, text="Magic Damage", command=lambda: self.show_content("magic"))
        self.sidebar_magic_button.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_help_button = ctk.CTkButton(self.sidebar, text="Help", command=lambda: self.show_content("help"))
        self.sidebar_help_button.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar, text="Appearance Mode")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 5))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(5, 70))
        self.appearance_mode_optionmenu.set(ctk.get_appearance_mode())

        self.divider = ctk.CTkFrame(self, width=5, corner_radius=0, fg_color=("#C8CCD2", "#2c2c2c"))
        self.divider.grid(row=0, column=1, sticky="ns")

        self.weapons = utils.fetch_weapons()

        self.contents = {
            "melee": self.create_content_frame(),
            "magic": self.create_content_frame(),
        }

        self.current_content = None
        self.show_content("melee")

    def change_appearance_mode(self, value):
        ctk.set_appearance_mode(value)

    def create_content_frame(self):
        frame = ctk.CTkFrame(self, corner_radius=0, fg_color=("#ffffff", "#1e1e1e"))
        frame.grid_rowconfigure(0, weight=2)
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure((0, 1, 2), weight=1)

        input_tabview = ctk.CTkTabview(frame, corner_radius=0)
        input_tabview.add("Weapon")
        input_tabview.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")
        input_tabview.tab("Weapon").grid_columnconfigure((0, 1, 2), weight=1)

        weapon_names = [w["name"] for w in self.weapons]
        weapon_combobox = SearchableComboBox(input_tabview.tab("Weapon"), "Weapon", weapon_names)
        weapon_combobox.grid(row=0, column=0, padx=20, pady=20)
        label_text = ctk.CTkLabel(input_tabview.tab("Weapon"), text="ciao")
        label_text.grid(row=0, column=1)

        control_frame = ctk.CTkFrame(frame, corner_radius=0)
        control_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        control_frame.grid_rowconfigure(0, weight=0)
        control_frame.grid_rowconfigure((1, 2, 3), weight=0)
        control_frame.grid_rowconfigure(5, weight=1)
        control_frame.grid_columnconfigure((0, 1), weight=1)

        control_label = ctk.CTkLabel(control_frame, text="Controls", font=self.fonts["small"])
        control_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        dps_checkbox = ctk.CTkCheckBox(control_frame, text="DPS") # show dps damage?
        dps_checkbox.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        Tooltip(dps_checkbox, "Whether or not show dps in damage calculations")

        non_crit_checkbox = ctk.CTkCheckBox(control_frame, text="Non Crit") # show non crits damage? Disabled if 100%+ crit chance or sting weapon
        non_crit_checkbox.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        Tooltip(non_crit_checkbox, "Whether or not show non critical damage")

        stats_button = ctk.CTkButton(control_frame, corner_radius=0, text="Update Stats")
        stats_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        damage_button = ctk.CTkButton(control_frame, text="Calculate Damage")
        damage_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20, ipadx=20, ipady=20)

        display_frame = ctk.CTkFrame(frame, corner_radius=0)
        display_frame.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")
        display_frame.grid_rowconfigure(0, weight=1)
        display_frame.grid_rowconfigure(1, weight=4)
        display_frame.grid_columnconfigure(0, weight=1)

        label_display_frame = ctk.CTkLabel(display_frame, text="Damage and stats display", font=self.fonts["small"])
        label_display_frame.grid(row=0, column=0, padx=20, sticky="nsew")
        textbox = ctk.CTkTextbox(display_frame)
        textbox.insert("0.0", "ciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\nciao\n\nciaociao\n")
        textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        

        return frame
    
    def show_content(self, name):
        if self.current_content:
            self.current_content.grid_remove()

        frame = self.contents[name]
        frame.grid(row=0, column=2, sticky="nsew")
        self.current_content = frame

if __name__ == "__main__":
    app = App()
    app.mainloop()
