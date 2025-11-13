import customtkinter as ctk

from utils.tooltip import Tooltip
from utils.combobox import SearchableComboBox
import utils.helper as helper

class WeaponTab(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

        first_frame = ctk.CTkFrame(self, corner_radius=0)
        first_frame.grid_rowconfigure(5, minsize=15)
        first_frame.grid(row=0, column=0, padx=20, pady=5, sticky="nsew")

        second_frame = ctk.CTkFrame(self, corner_radius=0)
        second_frame.grid(row=0, column=1, padx=20, pady=5, sticky="nsew")

        third_frame = ctk.CTkFrame(self, corner_radius=0)
        third_frame.grid(row=0, column=2, padx=20, pady=5, sticky="nsew")

        weapon_names = [w["name"] for w in helper.fetch_weapons()]
        weapon_combobox = SearchableComboBox(first_frame, "Weapon", weapon_names)
        weapon_combobox.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        reforge_combobox = SearchableComboBox(first_frame, "Reforge", values=["negro", "spicy", "fabled"])
        reforge_combobox.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        hpb_checkbox = ctk.CTkCheckBox(first_frame, corner_radius=0, text="Hot Potato Books")
        hpb_checkbox.grid(row=2, column=0, padx=20, pady=5, sticky="nw")
        Tooltip(hpb_checkbox, "Only check if max hot potato books")

        fpb_checkbox = ctk.CTkCheckBox(first_frame, corner_radius=0, text="Fuming Potato Books")
        fpb_checkbox.grid(row=3, column=0, padx=20, pady=5, sticky="nw")
        Tooltip(fpb_checkbox, "Only check if max fuming potato books")

        aow_checkbox = ctk.CTkCheckBox(first_frame, corner_radius=0, text="The Art Of War")
        aow_checkbox.grid(row=4, column=0, padx=20, pady=5, sticky="nw")

        recomb_checkbox = ctk.CTkCheckBox(first_frame, corner_radius=0, text="Recombobulator 3000")
        recomb_checkbox.grid(row=6, column=0, padx=20, pady=5, sticky="nw")

        enchant_name = SearchableComboBox(second_frame, "Enchant Name", values=["Sharpness", "Smite", "and", "the", "fucking", "rest"], width=128)
        enchant_name.grid(row=0, column=1, padx=10, pady=10, sticky="n")
        enchant_level = SearchableComboBox(second_frame, "Enchant Level", values=["1", "2", "3", "4", "5", "6"], width=128)
        enchant_level.grid(row=0, column=2, padx=10, pady=10, sticky="n")
        ultimate_enchant_name = SearchableComboBox(second_frame, "Ultimate Enchant Name", values=["Chimera", "Ultimate Wise", "Combo", "Nigger"], width=170)
        ultimate_enchant_name.grid(row=1, column=1, padx=10, pady=10, sticky="n")
        ultimate_enchant_level = SearchableComboBox(second_frame, "Ultimate Enchant Level", values=["1", "2", "3", "4", "5"], width=170)
        ultimate_enchant_level.grid(row=1, column=2, padx=10, pady=10, sticky="n")

        enchant_label = ctk.CTkLabel(second_frame, text="Enchantment List", font=helper.FONTS["small"])
        enchant_label.grid(row=2, column=1, columnspan=2, padx=20, pady=(10, 5), sticky="new")
        enchants_list = ctk.CTkTextbox(second_frame, corner_radius=0, font=helper.FONTS["small"])
        enchants_list.grid(row=3, column=1, rowspan=3, columnspan=2, padx=20, pady=10, sticky="nsew")
        enchants_list.tag_config("center", justify="center")
        enchants_list.insert("1.0", "Normal enchants\n\n", "center")
        enchants_list.insert("3.0", "Ultimate enchant", "center")

        clear_last_enchant_button = ctk.CTkButton(second_frame, text="Remove last enchant", corner_radius=0, width=200)
        clear_last_enchant_button.grid(row=3, column=3, padx=20, sticky="w")
        clear_enchants_button = ctk.CTkButton(second_frame, text="Clear all enchants ", corner_radius=0, width=200)
        clear_enchants_button.grid(row=4, column=3, padx=20, sticky="w")
        clear_ultimate_enchant_button = ctk.CTkButton(second_frame, text="Clear ultimate enchant", corner_radius=0, width=200)
        clear_ultimate_enchant_button.grid(row=5, column=3, padx=20, sticky="w")

        stars_combobox = SearchableComboBox(third_frame, "Stars", values=["1", "2", "3", "4"], width=100)
        stars_combobox.grid(row=0, column=0, columnspan=3, padx=20, pady=10, sticky="n")
        master_stars_combobox = SearchableComboBox(third_frame, "Master Stars", values=["1", "2", "3", "4"], width=100)
        master_stars_combobox.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky="n")

        gemstone_label = ctk.CTkLabel(third_frame, text="Gemstones", corner_radius=0)
        gemstone_label.grid(row=3, column=0, columnspan=3, padx=20, pady=20, sticky="new")
        slot1_label = ctk.CTkLabel(third_frame, text="Slot 1", corner_radius=0)
        slot1_label.grid(row=4, column=0, padx=20, pady=25, sticky="nw")
        gemstone_type_combobox = SearchableComboBox(third_frame, "Gemstone Type", values=["Jasper", "Onyx"], width=100)
        gemstone_type_combobox.grid(row=4, column=1, padx=20, pady=10, sticky="n")
        gemstone_tier_combobox = SearchableComboBox(third_frame, "Gemstone Tier", values=["Rough", "Flawed", "Fine", "Flawless", "Perfect"], width=100)
        gemstone_tier_combobox.grid(row=4, column=2, padx=20, pady=10, sticky="n")
        slot2_label = ctk.CTkLabel(third_frame, text="Slot 2", corner_radius=0)
        slot2_label.grid(row=5, column=0, columnspan=2, padx=20, pady=25, sticky="nw")
        gemstone_type_2_combobox = SearchableComboBox(third_frame, "Gemstone Type", values=["Jasper", "Onyx"], width=100)
        gemstone_type_2_combobox.grid(row=5, column=1, padx=20, pady=10, sticky="n")
        gemstone_tier_2_combobox = SearchableComboBox(third_frame, "Gemstone Tier", values=["Rough", "Flawed", "Fine", "Flawless", "Perfect"], width=100)
        gemstone_tier_2_combobox.grid(row=5, column=2, padx=20, pady=10, sticky="n")