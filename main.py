import customtkinter as ctk

from ui.content import MainContent
from ui.sidebar import Sidebar
import utils.helper as helper

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hypixel Skyblock Damage Calculator")
        self.geometry(f"{helper.WIDTH}x{helper.HEIGHT}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.sidebar = Sidebar(self, self.show_content, self.change_appearance_mode)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.divider = ctk.CTkFrame(self, width=5, corner_radius=0, fg_color=("#c8ccd2", "#2c2c2c"))
        self.divider.grid(row=0, column=1, sticky="ns")

        self.contents = {
            "melee": self.create_content_frame(),
            "magic": self.create_content_frame(),
        }

        self.current_content = None
        self.show_content("melee")

    def change_appearance_mode(self, value):
        ctk.set_appearance_mode(value)

    def create_content_frame(self):
        frame = MainContent(self)
        
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
