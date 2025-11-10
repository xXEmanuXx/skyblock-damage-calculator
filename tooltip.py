import tkinter as tk
import customtkinter as ctk

class Tooltip:
    def __init__(self, widget: ctk.CTkBaseClass, text: str, delay: int = 500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tip_window = None
        self.after_id = None

        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)

    def on_enter(self, event=None):
        self.after_id = self.widget.after(self.delay, self.show_tip)

    def on_leave(self, event=None):
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

        self.hide_tip()

    def show_tip(self):
        if self.tip_window or not self.text:
            return
        
        x = self.widget.winfo_rootx() + self.widget.winfo_width() + 5
        y = self.widget.winfo_rooty()

        tw = tk.Toplevel(self.widget)
        self.tip_window = tw
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")

        mode = ctk.get_appearance_mode()
        fg_color = "white" if mode == "Light" else "#333333"
        text_color = "black" if mode == "Light" else "white"

        label = ctk.CTkLabel(tw, text=self.text, fg_color=fg_color, text_color=text_color, font=ctk.CTkFont(size=12), corner_radius=5)
        label.pack()

    def hide_tip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None