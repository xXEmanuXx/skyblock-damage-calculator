import customtkinter as ctk

class SearchableComboBox(ctk.CTkFrame):
    def __init__(self, master, label_text, values, command=None, width=300, height=100):
        super().__init__(master, fg_color="transparent")
        self.values = values
        self.command = command
        self.filtered_values = list(values)
        self.width = width
        self.height = height
        self._after_id = None
        self._last_value = ""
        self._selected_index = None

        self.label = ctk.CTkLabel(self, text=label_text)
        self.label.pack()

        self.entry_var = ctk.StringVar()
        self.entry = ctk.CTkEntry(self, textvariable=self.entry_var, width=self.width + 15, corner_radius=0)
        self.entry.bind("<KeyRelease>", self._on_keyrelease)
        self.entry.bind("<Button-1>", self.toggle_dropdown)
        self.entry.bind("<Up>", self._on_arrow)
        self.entry.bind("<Down>", self._on_arrow)
        self.entry.bind("<Return>", self._on_enter)
        self.entry.pack(fill="x", padx=2, pady=0)

        self.dropdown = ctk.CTkScrollableFrame(self, width=self.width, height=self.height, corner_radius=0, fg_color=("#ffffff", "#252525"))
        self.dropdown_visible = False

        self.populate_dropdown(self.filtered_values)

    def _on_keyrelease(self, event):
        if event.keysym == "Return":
            return
        
        if event.keysym == "Escape":
            self._disable_dropdown()
            return
        
        current_value = self.entry_var.get()
        if current_value != self._last_value:
            self._last_value = current_value
            if self._after_id:
                self.after_cancel(self._after_id)   

            self._after_id = self.after(50, self.filter_values)

    def _on_enter(self, event=None):
        if self._selected_index is not None:
            self.select_value(self.filtered_values[self._selected_index])
            self._selected_index = None
        elif self.dropdown_visible and len(self.filtered_values) == 1:
            self.select_value(self.filtered_values[0])

    def _on_arrow(self, event):
        n = len(self.filtered_values)
        
        if not self.dropdown_visible or n == 0:
            return
        
        if self._selected_index == None:
            self._selected_index = 0 if event.keysym == "Down" else n - 1
        else:
            if event.keysym == "Down":
                self._selected_index = (self._selected_index + 1) % n
            else:
                self._selected_index = (self._selected_index - 1) % n

        self._highlight_selection()

    def _highlight_selection(self):
        for i, btn in enumerate(self.dropdown.winfo_children()):
            if isinstance(btn, ctk.CTkButton):
                if i == self._selected_index:
                    btn.configure(fg_color="gray50")
                else:
                    btn.configure(fg_color="transparent")

    def _enable_dropdown(self):
        self.dropdown.pack(fill="both", expand=True)
        self.dropdown_visible = True

    def _disable_dropdown(self):
        self.dropdown.pack_forget()
        self.dropdown_visible = False

    def toggle_dropdown(self, event=None):
        if self.dropdown_visible:
            self._disable_dropdown()
        else:
            self._enable_dropdown()

    def filter_values(self):
        self._enable_dropdown()
        typed = self.entry_var.get().strip().lower()

        if typed == "":
            self.filtered_values = self.values
        else:
            self.filtered_values = [v for v in self.values if typed in v.lower()]

        self._selected_index = None
        self.populate_dropdown(self.filtered_values)       

    def populate_dropdown(self, items):
        for widget in self.dropdown.winfo_children():
            widget.destroy()

        for value in items:
            btn = ctk.CTkButton(self.dropdown, text=value, fg_color="transparent", text_color=("black", "white"), height=26,
                                hover_color=("gray85", "gray25"), anchor="w",
                                command=lambda v=value: self.select_value(v))
            btn.pack(fill="x", padx=2, pady=1)

        self.dropdown._parent_canvas.yview_moveto(0)

    def select_value(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, value)
        self.toggle_dropdown()
        if self.command:
            self.command(value)
