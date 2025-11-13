import customtkinter as ctk
import utils.helper as helper

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, on_show_content, on_change_appearance):
        super().__init__(master, fg_color=("#e7e9ec", "#141414"), width=300, corner_radius=0)
        self.on_show_content = on_show_content
        self.on_change_appearance = on_change_appearance

        self.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_propagate(False)

        self.sidebar_title = ctk.CTkLabel(self, text="Settings", font=helper.FONTS["big"])
        self.sidebar_title.grid(row=0, column=0, padx=20, pady=(20, 70))

        self.sidebar_melee_button = ctk.CTkButton(self, text="Melee Damage", command=lambda: self.on_show_content("melee"))
        self.sidebar_melee_button.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_magic_button = ctk.CTkButton(self, text="Magic Damage", command=lambda: self.on_show_content("magic"))
        self.sidebar_magic_button.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_help_button = ctk.CTkButton(self, text="Help", command=lambda: self.on_show_content("help"))
        self.sidebar_help_button.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 5))
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"], command=self.on_change_appearance)
        self.appearance_mode_optionmenu.set(ctk.get_appearance_mode())
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(5, 70))
