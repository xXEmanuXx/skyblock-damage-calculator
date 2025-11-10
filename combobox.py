import customtkinter as ctk

class SearchableComboBox(ctk.CTkFrame):
    def __init__(self, master, label_text, values, command=None, width=200, height=100):
        super().__init__(master)
        self.values = values
        self.command = command
        self.filtered_values = list(values)
        self.width = width
        self.height = height

        self.label = ctk.CTkLabel(self, text=label_text)
        self.label.pack(fill="x", padx=2, pady=(2, 0))

        self.entry_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, corner_radius=0)
        self.entry.bind("<KeyRelease>", self.filter_values)
        self.entry.bind("<Button-1>", self.toggle_dropdown)
        self.entry.pack(fill="x", padx=2, pady=2)

        self.dropdown = ctk.CTkScrollableFrame(self, width=self.width, height=self.height, corner_radius=0)
        self.dropdown_visible = False

        self.populate_dropdown(self.filtered_values)

    def filter_values(self, event=None):
        typed = self.entry_var.get().strip().lower()

        if typed == "":
            self.filtered_values = self.values
        else:
            self.filtered_values = [v for v in self.values if typed in v.lower()]

        if len(self.filtered_values) < 30:
            self.populate_dropdown(self.filtered_values)
        else:
            self.populate_dropdown(self.filtered_values[:30])

    def toggle_dropdown(self, event=None):
        if self.dropdown_visible:
            self.dropdown.pack_forget()
        else:
            self.dropdown.pack(fill="both", expand=True)

        self.dropdown_visible = not self.dropdown_visible

    def populate_dropdown(self, items):
        for widget in self.dropdown.winfo_children():
            widget.destroy()

        for value in items:
            btn = ctk.CTkButton(self.dropdown, text=value, fg_color="transparent", text_color=("black", "white"), height=26,
                                hover_color=("gray85", "gray25"), anchor="w",
                                command=lambda v=value: self.select_value(v))
            btn.pack(fill="x", padx=2, pady=1)

    def select_value(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, value)
        self.toggle_dropdown()
        if self.command:
            self.command(value)
