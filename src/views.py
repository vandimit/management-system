import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkinter.font import Font
from typing import Dict, Any, List, Optional, Callable

class ModernUI:
    """Custom colour scheme and styling constants"""
    # Colour palette
    PRIMARY = "#2962ff"       # Primary blue
    PRIMARY_DARK = "#0039cb"  # Darker blue for hover states
    PRIMARY_LIGHT = "#768fff" # Lighter blue for accents
    SUCCESS = "#43a047"       # Green for success actions
    DANGER = "#e53935"        # Red for delete/cancel actions
    WARNING = "#ff9800"       # Orange for warnings
    BG_LIGHT = "#f5f5f5"      # Light background
    BG_DARK = "#e0e0e0"       # Slightly darker background for contrast
    TEXT_PRIMARY = "#212121"  # Primary text colour (dark grey)
    TEXT_SECONDARY = "#757575" # Secondary text colour (medium grey)
    TEXT_LIGHT = "#ffffff"    # Light text for dark backgrounds
    BORDER = "#bdbdbd"        # Border colour

    # Padding and spacing
    PADDING_SMALL = 5
    PADDING_MEDIUM = 10
    PADDING_LARGE = 15

    # Font sizes
    FONT_SMALL = 9
    FONT_MEDIUM = 10
    FONT_LARGE = 12
    FONT_XL = 14

    # Border radius (simulated in some widgets)
    BORDER_RADIUS = 4


class RecordManagementGUI(tk.Tk):
    """View component for Record Management System."""
    
    def __init__(self, client_controller=None, airline_controller=None, flight_controller=None):
        """Initialize the GUI with optional controllers."""
        super().__init__()
        self.title("✈️ Flight Record Management System")
        self.geometry("950x700")
        self.minsize(850, 650)
        
        # Store controllers
        self.client_controller = client_controller
        self.airline_controller = airline_controller
        self.flight_controller = flight_controller
        
        # Configure UI colours and fonts
        self.ui = ModernUI()
        self.configure(bg=self.ui.BG_LIGHT)
        
        # Load custom fonts
        self.title_font = Font(family="Segoe UI", size=self.ui.FONT_XL, weight="bold")
        self.header_font = Font(family="Segoe UI", size=self.ui.FONT_LARGE, weight="bold")
        self.normal_font = Font(family="Segoe UI", size=self.ui.FONT_MEDIUM)
        self.small_font = Font(family="Segoe UI", size=self.ui.FONT_SMALL)
        
        self.set_styles()
        self.create_widgets()
        
        # Bind the window close event to our on_closing method
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Slight transparency (if supported)
        try:
            self.attributes("-alpha", 0.97)
        except Exception:
            pass

    def on_closing(self):
        """Handle window closing event."""
        # Perform any cleanup here if necessary
        self.destroy()

    def set_styles(self):
        """Set up the ttk styles for widgets."""
        style = ttk.Style(self)
        style.theme_use('clam')
        
        # Frame styles
        style.configure("TFrame", background=self.ui.BG_LIGHT)
        style.configure("Card.TFrame", background=self.ui.BG_LIGHT, relief="raised", borderwidth=1)
        
        # Label styles
        style.configure("TLabel", background=self.ui.BG_LIGHT, foreground=self.ui.TEXT_PRIMARY, font=self.normal_font)
        style.configure("Header.TLabel", font=self.header_font, foreground=self.ui.PRIMARY)
        style.configure("Title.TLabel", font=self.title_font, foreground=self.ui.PRIMARY)
        
        # Button styles
        style.configure("TButton", background=self.ui.PRIMARY, foreground=self.ui.TEXT_LIGHT,
                        font=self.normal_font, borderwidth=0)
        style.map("TButton", background=[('active', self.ui.PRIMARY_DARK), ('pressed', self.ui.PRIMARY_DARK)],
                  relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
        style.configure("Success.TButton", background=self.ui.SUCCESS)
        style.map("Success.TButton", background=[('active', '#2e7d32'), ('pressed', '#2e7d32')])
        style.configure("Danger.TButton", background=self.ui.DANGER)
        style.map("Danger.TButton", background=[('active', '#c62828'), ('pressed', '#c62828')])
        style.configure("Warning.TButton", background=self.ui.WARNING)
        style.map("Warning.TButton", background=[('active', '#ef6c00'), ('pressed', '#ef6c00')])
        
        # Notebook styles
        style.configure("TNotebook", background=self.ui.BG_LIGHT, borderwidth=0)
        style.configure("TNotebook.Tab", background=self.ui.BG_DARK, foreground=self.ui.TEXT_PRIMARY,
                        font=self.normal_font, padding=[15, 5], borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", self.ui.PRIMARY)],
                  foreground=[("selected", self.ui.TEXT_LIGHT)])
        
        # Entry styles
        style.configure("TEntry", foreground=self.ui.TEXT_PRIMARY, fieldbackground=self.ui.BG_LIGHT,
                        borderwidth=1, font=self.normal_font)
        
        # Labelframe styles
        style.configure("TLabelframe", background=self.ui.BG_LIGHT, borderwidth=1)
        style.configure("TLabelframe.Label", background=self.ui.BG_LIGHT, foreground=self.ui.PRIMARY,
                        font=self.header_font)
        
        # Treeview styles
        style.configure("Treeview", background=self.ui.BG_LIGHT, foreground=self.ui.TEXT_PRIMARY,
                        rowheight=25, fieldbackground=self.ui.BG_LIGHT, font=self.normal_font, borderwidth=0)
        style.configure("Treeview.Heading", background=self.ui.PRIMARY, foreground=self.ui.TEXT_LIGHT,
                        font=self.normal_font, relief="flat")
        style.map("Treeview", background=[('selected', self.ui.PRIMARY_LIGHT)],
                  foreground=[('selected', self.ui.TEXT_LIGHT)])
        style.map("Treeview.Heading", background=[('active', self.ui.PRIMARY_DARK)])

    def create_widgets(self):
        """Create the main application widgets."""
        # Header section with logo and title
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", padx=self.ui.PADDING_MEDIUM, pady=(self.ui.PADDING_MEDIUM, 0))
        
        # Logo (using text as a placeholder)
        logo_text = ttk.Label(header_frame, text="✈️", font=Font(size=24))
        logo_text.pack(side="left", padx=(0, self.ui.PADDING_SMALL))
        
        # Title label
        title = ttk.Label(header_frame, text="Flight Record Management System", style="Title.TLabel")
        title.pack(side="left", padx=self.ui.PADDING_SMALL)
        
        # Main container for content
        main_container = ttk.Frame(self)
        main_container.pack(expand=True, fill="both", padx=self.ui.PADDING_MEDIUM, pady=self.ui.PADDING_MEDIUM)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(expand=True, fill="both")
        
        # Create tab frames with a card-like style
        self.client_frame = ttk.Frame(self.notebook, style="Card.TFrame")
        self.airline_frame = ttk.Frame(self.notebook, style="Card.TFrame")
        self.flight_frame = ttk.Frame(self.notebook, style="Card.TFrame")
        
        self.notebook.add(self.client_frame, text="👥 Clients")
        self.notebook.add(self.airline_frame, text="✈️ Airlines")
        self.notebook.add(self.flight_frame, text="🛫 Flights")
        
        # Build tab contents
        self.build_client_frame()
        self.build_airline_frame()
        self.build_flight_frame()
        
        # Status bar at the bottom
        status_frame = ttk.Frame(self)
        status_frame.pack(fill="x", padx=self.ui.PADDING_MEDIUM, pady=(0, self.ui.PADDING_SMALL))
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(status_frame, textvariable=self.status_var, font=self.small_font, 
                                foreground=self.ui.TEXT_SECONDARY)
        status_label.pack(side="left")
        version_label = ttk.Label(status_frame, text="v1.0.0", font=self.small_font, 
                                 foreground=self.ui.TEXT_SECONDARY)
        version_label.pack(side="right")

    def create_form_entry(self, parent, label, row, column, span=1, required=False):
        """Create a labeled form entry field."""
        field_frame = ttk.Frame(parent)
        field_frame.grid(row=row, column=column, columnspan=span, sticky="ew", 
                       padx=self.ui.PADDING_SMALL, pady=self.ui.PADDING_SMALL)
        
        label_text = f"{label}{'*' if required else ''}"
        field_label = ttk.Label(field_frame, text=label_text)
        field_label.pack(fill="x", anchor="w")
        
        entry = ttk.Entry(field_frame)
        entry.pack(fill="x", ipady=2)
        return entry

    def create_button(self, parent, text, command, style="TButton", width=None, **kwargs):
        """Create a styled button."""
        btn = ttk.Button(parent, text=text, command=command, style=style, width=width, **kwargs)
        return btn

    # ------------------------------
    # Client tab methods
    # ------------------------------
    def build_client_frame(self):
        """Build the client management tab."""
        frame = self.client_frame
        
        header = ttk.Label(frame, text="Client Management", style="Header.TLabel")
        header.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=self.ui.PADDING_MEDIUM)
        
        desc = ttk.Label(frame, text="Create and manage client records in the system.", 
                         foreground=self.ui.TEXT_SECONDARY)
        desc.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=(0, self.ui.PADDING_MEDIUM))
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(expand=True, fill="both", padx=self.ui.PADDING_MEDIUM)
        
        # Form section (left)
        form_section = ttk.Frame(content_frame)
        form_section.pack(side="left", fill="y", padx=(0, self.ui.PADDING_MEDIUM))
        
        form_frame = ttk.LabelFrame(form_section, text="Client Details")
        form_frame.pack(fill="x", pady=(0, self.ui.PADDING_MEDIUM))
        
        self.client_entries = {}
        self.client_entries["ID"] = self.create_form_entry(form_frame, "ID", 0, 0, required=True)
        self.client_entries["Type"] = self.create_form_entry(form_frame, "Type", 1, 0)
        self.client_entries["Name"] = self.create_form_entry(form_frame, "Name", 2, 0, required=True)
        self.client_entries["Phone Number"] = self.create_form_entry(form_frame, "Phone Number", 3, 0)
        self.client_entries["Country"] = self.create_form_entry(form_frame, "Country", 4, 0)
        self.client_entries["Address Line 1"] = self.create_form_entry(form_frame, "Address Line 1", 0, 1)
        self.client_entries["City"] = self.create_form_entry(form_frame, "City", 1, 1)
        self.client_entries["State"] = self.create_form_entry(form_frame, "State", 2, 1)
        self.client_entries["Zip Code"] = self.create_form_entry(form_frame, "Zip Code", 3, 1)
        
        button_frame = ttk.Frame(form_section)
        button_frame.pack(fill="x", pady=self.ui.PADDING_MEDIUM)
        self.create_button(button_frame, "➕ Create", self.create_client_record, style="Success.TButton")\
            .pack(side="left", padx=(0, self.ui.PADDING_SMALL))
        self.create_button(button_frame, "🔄 Update", self.update_client_record)\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "❌ Delete", self.delete_client_record, style="Danger.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "🔍 Search", self.search_client_record, style="Warning.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        
        # Table section (right)
        table_section = ttk.Frame(content_frame)
        table_section.pack(side="right", expand=True, fill="both")
        table_header = ttk.Frame(table_section)
        table_header.pack(fill="x", pady=(0, self.ui.PADDING_SMALL))
        ttk.Label(table_header, text="Client Records", style="Header.TLabel").pack(side="left")
        refresh_btn = self.create_button(table_header, "🔄 Refresh", self.display_client_records, width=10)
        refresh_btn.pack(side="right")
        
        tree_frame = ttk.Frame(table_section)
        tree_frame.pack(expand=True, fill="both")
        columns = ["ID", "Type", "Name", "Address Line 1", "City", "State", "Country", "Phone Number"]
        self.client_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.client_tree.heading(col, text=col)
            width = 70 if col in ["ID", "Type"] else 120
            self.client_tree.column(col, width=width, minwidth=50)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.client_tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.client_tree.xview)
        self.client_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.client_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        self.client_tree.bind("<<TreeviewSelect>>", self.on_client_select)
        
        # Load initial data if controller is available
        if self.client_controller:
            self.display_client_records()
            
    def create_client_record(self):
        """Create a new client record using controller."""
        if not self.client_controller:
            messagebox.showinfo("Action", "Client controller not available.")
            return
            
        # Get form data
        client_data = {}
        for field, entry in self.client_entries.items():
            client_data[field] = entry.get()
            
        # Call controller
        success = self.client_controller.create_client(client_data)
        
        if success:
            messagebox.showinfo("Success", "Client record created successfully.")
            self.display_client_records()
            self.clear_client_form()
        else:
            print(f"hello")
            messagebox.showerror("Error", "Failed to create client record. Please check the data and try again.")
    
    def update_client_record(self):
        """Update an existing client record using controller."""
        if not self.client_controller:
            messagebox.showinfo("Action", "Client controller not available.")
            return
            
        # Check if a client is selected
        selected_items = self.client_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select a client to update.")
            return
            
        # Get form data
        client_data = {}
        for field, entry in self.client_entries.items():
            client_data[field] = entry.get()
            
        # Get client ID
        client_id = client_data["ID"]
        
        # Call controller
        success = self.client_controller.update_client(client_id, client_data)
        
        if success:
            messagebox.showinfo("Success", "Client record updated successfully.")
            self.display_client_records()
        else:
            messagebox.showerror("Error", "Failed to update client record. Please check the data and try again.")
    
    def delete_client_record(self):
        """Delete a client record using controller."""
        if not self.client_controller:
            messagebox.showinfo("Action", "Client controller not available.")
            return
            
        # Check if a client is selected
        selected_items = self.client_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select a client to delete.")
            return
            
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this client record?")
        if not confirm:
            return
            
        # Get client ID
        item = selected_items[0]
        values = self.client_tree.item(item, "values")
        client_id = values[0]
        
        # Call controller
        success = self.client_controller.delete_client(client_id)
        
        if success:
            messagebox.showinfo("Success", "Client record deleted successfully.")
            self.display_client_records()
            self.clear_client_form()
        else:
            messagebox.showerror("Error", "Failed to delete client record.")
    
    def search_client_record(self):
        """Search for client records using controller."""
        if not self.client_controller:
            messagebox.showinfo("Action", "Client controller not available.")
            return
            
        # Get search term
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if not search_term:
            return
            
        # Call controller
        results = self.client_controller.search_clients(search_term)
        
        # Display results
        self.display_client_records(results)
        self.status_var.set(f"Found {len(results)} clients matching '{search_term}'")
    
    def display_client_records(self, clients=None):
        """Display client records in the treeview."""
        # Clear existing records
        for item in self.client_tree.get_children():
            self.client_tree.delete(item)
            
        # Get records from controller if not provided
        if clients is None and self.client_controller:
            clients = self.client_controller.get_all_clients()
            
        # If no controller and no clients provided, show sample data
        if clients is None:
            self.populate_sample_clients()
            return
            
        # Display records
        for client in clients:
            values = (
                client.get("ID", ""),
                client.get("Type", ""),
                client.get("Name", ""),
                client.get("Address Line 1", ""),
                client.get("City", ""),
                client.get("State", ""),
                client.get("Country", ""),
                client.get("Phone Number", "")
            )
            self.client_tree.insert("", "end", values=values)
            
        self.status_var.set(f"Displaying {len(clients)} client records")
    
    def populate_sample_clients(self):
        """Add sample client data to the treeview for demo purposes."""
        for item in self.client_tree.get_children():
            self.client_tree.delete(item)
        self.client_tree.insert("", "end", values=("1", "Regular", "John Doe", "123 Main St", "London", "Greater London", "UK", "0123456789"))
        self.client_tree.insert("", "end", values=("2", "Premium", "Jane Smith", "456 Side Ave", "Manchester", "Greater Manchester", "UK", "0987654321"))
    
    def on_client_select(self, event):
        """Handle client selection in treeview."""
        selected_items = self.client_tree.selection()
        if not selected_items:
            return
        item = selected_items[0]
        values = self.client_tree.item(item, "values")
        
        # Clear form
        self.clear_client_form()
        
        # Populate form with selected client data
        columns = ["ID", "Type", "Name", "Address Line 1", "City", "State", "Country", "Phone Number"]
        for i, col in enumerate(columns):
            if col in self.client_entries and i < len(values):
                self.client_entries[col].insert(0, values[i])
                
        self.status_var.set(f"Selected client: {values[2]}")
    
    def clear_client_form(self):
        """Clear all form fields."""
        for entry in self.client_entries.values():
            entry.delete(0, tk.END)
    
    # ------------------------------
    # Airline tab methods
    # ------------------------------
    def build_airline_frame(self):
        """Build the airline management tab."""
        frame = self.airline_frame
        
        header = ttk.Label(frame, text="Airline Management", style="Header.TLabel")
        header.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=self.ui.PADDING_MEDIUM)
        desc = ttk.Label(frame, text="Create and manage airline records in the system.", 
                         foreground=self.ui.TEXT_SECONDARY)
        desc.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=(0, self.ui.PADDING_MEDIUM))
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(expand=True, fill="both", padx=self.ui.PADDING_MEDIUM)
        form_section = ttk.Frame(content_frame)
        form_section.pack(side="left", fill="y", padx=(0, self.ui.PADDING_MEDIUM))
        
        form_frame = ttk.LabelFrame(form_section, text="Airline Details")
        form_frame.pack(fill="x", pady=(0, self.ui.PADDING_MEDIUM))
        
        self.airline_entries = {}
        self.airline_entries["ID"] = self.create_form_entry(form_frame, "ID", 0, 0, required=True)
        self.airline_entries["Type"] = self.create_form_entry(form_frame, "Type", 1, 0)
        self.airline_entries["Company Name"] = self.create_form_entry(form_frame, "Company Name", 2, 0, required=True)
        self.airline_entries["Country"] = self.create_form_entry(form_frame, "Country", 3, 0)
        self.airline_entries["IATA Code"] = self.create_form_entry(form_frame, "IATA Code", 4, 0)
        
        button_frame = ttk.Frame(form_section)
        button_frame.pack(fill="x", pady=self.ui.PADDING_MEDIUM)
        self.create_button(button_frame, "➕ Create", self.create_airline_record, style="Success.TButton")\
            .pack(side="left", padx=(0, self.ui.PADDING_SMALL))
        self.create_button(button_frame, "🔄 Update", self.update_airline_record)\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "❌ Delete", self.delete_airline_record, style="Danger.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "🔍 Search", self.search_airline_record, style="Warning.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        
        table_section = ttk.Frame(content_frame)
        table_section.pack(side="right", expand=True, fill="both")
        table_header = ttk.Frame(table_section)
        table_header.pack(fill="x", pady=(0, self.ui.PADDING_SMALL))
        ttk.Label(table_header, text="Airline Records", style="Header.TLabel").pack(side="left")
        refresh_btn = self.create_button(table_header, "🔄 Refresh", self.display_airline_records, width=10)
        refresh_btn.pack(side="right")
        
        tree_frame = ttk.Frame(table_section)
        tree_frame.pack(expand=True, fill="both")
        columns = ["ID", "Type", "Company Name", "Country", "IATA Code"]
        self.airline_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.airline_tree.heading(col, text=col)
            width = 70 if col in ["ID", "Type", "IATA Code"] else 150
            self.airline_tree.column(col, width=width, minwidth=50)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.airline_tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.airline_tree.xview)
        self.airline_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.airline_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        self.airline_tree.bind("<<TreeviewSelect>>", self.on_airline_select)
        
        # Load initial data if controller is available
        if self.airline_controller:
            self.display_airline_records()
            
    def create_airline_record(self):
        """Create a new airline record using controller."""
        if not self.airline_controller:
            messagebox.showinfo("Action", "Airline controller not available.")
            return
            
        # Get form data
        airline_data = {}
        for field, entry in self.airline_entries.items():
            airline_data[field] = entry.get()
            
        # Call controller
        success = self.airline_controller.create_airline(airline_data)
        
        if success:
            messagebox.showinfo("Success", "Airline record created successfully.")
            self.display_airline_records()
            self.clear_airline_form()
        else:
            messagebox.showerror("Error", "Failed to create airline record. Please check the data and try again.")
    
    def update_airline_record(self):
        """Update an existing airline record using controller."""
        if not self.airline_controller:
            messagebox.showinfo("Action", "Airline controller not available.")
            return
            
        # Check if an airline is selected
        selected_items = self.airline_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select an airline to update.")
            return
            
        # Get form data
        airline_data = {}
        for field, entry in self.airline_entries.items():
            airline_data[field] = entry.get()
            
        # Get airline ID
        airline_id = airline_data["ID"]
        
        # Call controller
        success = self.airline_controller.update_airline(airline_id, airline_data)
        
        if success:
            messagebox.showinfo("Success", "Airline record updated successfully.")
            self.display_airline_records()
        else:
            messagebox.showerror("Error", "Failed to update airline record. Please check the data and try again.")
    
    def delete_airline_record(self):
        """Delete an airline record using controller."""
        if not self.airline_controller:
            messagebox.showinfo("Action", "Airline controller not available.")
            return
            
        # Check if an airline is selected
        selected_items = self.airline_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select an airline to delete.")
            return
            
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this airline record?")
        if not confirm:
            return
            
        # Get airline ID
        item = selected_items[0]
        values = self.airline_tree.item(item, "values")
        airline_id = values[0]
        
        # Call controller
        success = self.airline_controller.delete_airline(airline_id)
        
        if success:
            messagebox.showinfo("Success", "Airline record deleted successfully.")
            self.display_airline_records()
            self.clear_airline_form()
        else:
            messagebox.showerror("Error", "Failed to delete airline record.")
    
    def search_airline_record(self):
        """Search for airline records using controller."""
        if not self.airline_controller:
            messagebox.showinfo("Action", "Airline controller not available.")
            return
            
        # Get search term
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if not search_term:
            return
            
        # Call controller
        results = self.airline_controller.search_airlines(search_term)
        
        # Display results
        self.display_airline_records(results)
        self.status_var.set(f"Found {len(results)} airlines matching '{search_term}'")
    
    def display_airline_records(self, airlines=None):
        """Display airline records in the treeview."""
        # Clear existing records
        for item in self.airline_tree.get_children():
            self.airline_tree.delete(item)
            
        # Get records from controller if not provided
        if airlines is None and self.airline_controller:
            airlines = self.airline_controller.get_all_airlines()
            
        # If no controller and no airlines provided, show sample data
        if airlines is None:
            self.populate_sample_airlines()
            return
            
        # Display records
        for airline in airlines:
            values = (
                airline.get("ID", ""),
                airline.get("Type", ""),
                airline.get("Company Name", ""),
                airline.get("Country", ""),
                airline.get("IATA Code", "")
            )
            self.airline_tree.insert("", "end", values=values)
            
        self.status_var.set(f"Displaying {len(airlines)} airline records")
    
    def populate_sample_airlines(self):
        """Add sample airline data to the treeview for demo purposes."""
        for item in self.airline_tree.get_children():
            self.airline_tree.delete(item)
        self.airline_tree.insert("", "end", values=("101", "International", "Global Airlines", "USA", "GA"))
        self.airline_tree.insert("", "end", values=("102", "Domestic", "Local Wings", "UK", "LW"))
    
    def on_airline_select(self, event):
        """Handle airline selection in treeview."""
        selected_items = self.airline_tree.selection()
        if not selected_items:
            return
        item = selected_items[0]
        values = self.airline_tree.item(item, "values")
        
        # Clear form
        self.clear_airline_form()
        
        # Populate form with selected airline data
        columns = ["ID", "Type", "Company Name", "Country", "IATA Code"]
        for i, col in enumerate(columns):
            if col in self.airline_entries and i < len(values):
                self.airline_entries[col].insert(0, values[i])
                
        self.status_var.set(f"Selected airline: {values[2]}")
    
    def clear_airline_form(self):
        """Clear all form fields."""
        for entry in self.airline_entries.values():
            entry.delete(0, tk.END)
            
    # ------------------------------
    # Flight tab methods
    # ------------------------------
    def build_flight_frame(self):
        """Build the flight management tab."""
        frame = self.flight_frame
        
        header = ttk.Label(frame, text="Flight Management", style="Header.TLabel")
        header.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=self.ui.PADDING_MEDIUM)
        desc = ttk.Label(frame, text="Create and manage flight bookings in the system.", 
                         foreground=self.ui.TEXT_SECONDARY)
        desc.pack(anchor="w", padx=self.ui.PADDING_LARGE, pady=(0, self.ui.PADDING_MEDIUM))
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(expand=True, fill="both", padx=self.ui.PADDING_MEDIUM)
        form_section = ttk.Frame(content_frame)
        form_section.pack(side="left", fill="y", padx=(0, self.ui.PADDING_MEDIUM))
        
        form_frame = ttk.LabelFrame(form_section, text="Flight Details")
        form_frame.pack(fill="x", pady=(0, self.ui.PADDING_MEDIUM))
        
        self.flight_entries = {}
        self.flight_entries["Flight ID"] = self.create_form_entry(form_frame, "Flight ID", 0, 0, required=True)
        self.flight_entries["Client ID"] = self.create_form_entry(form_frame, "Client ID", 1, 0, required=True)
        self.flight_entries["Airline ID"] = self.create_form_entry(form_frame, "Airline ID", 2, 0, required=True)
        self.flight_entries["Date"] = self.create_form_entry(form_frame, "Date (YYYY-MM-DD)", 3, 0, required=True)
        self.flight_entries["Departure"] = self.create_form_entry(form_frame, "Departure City", 4, 0, required=True)
        self.flight_entries["Arrival"] = self.create_form_entry(form_frame, "Arrival City", 5, 0, required=True)
        self.flight_entries["Status"] = self.create_form_entry(form_frame, "Status", 6, 0)
        
        button_frame = ttk.Frame(form_section)
        button_frame.pack(fill="x", pady=self.ui.PADDING_MEDIUM)
        self.create_button(button_frame, "➕ Create", self.create_flight_record, style="Success.TButton")\
            .pack(side="left", padx=(0, self.ui.PADDING_SMALL))
        self.create_button(button_frame, "🔄 Update", self.update_flight_record)\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "❌ Delete", self.delete_flight_record, style="Danger.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        self.create_button(button_frame, "🔍 Search", self.search_flight_record, style="Warning.TButton")\
            .pack(side="left", padx=self.ui.PADDING_SMALL)
        
        table_section = ttk.Frame(content_frame)
        table_section.pack(side="right", expand=True, fill="both")
        table_header = ttk.Frame(table_section)
        table_header.pack(fill="x", pady=(0, self.ui.PADDING_SMALL))
        ttk.Label(table_header, text="Flight Records", style="Header.TLabel").pack(side="left")
        refresh_btn = self.create_button(table_header, "🔄 Refresh", self.display_flight_records, width=10)
        refresh_btn.pack(side="right")
        
        tree_frame = ttk.Frame(table_section)
        tree_frame.pack(expand=True, fill="both")
        columns = ["Flight ID", "Client ID", "Airline ID", "Date", "Departure", "Arrival", "Status"]
        self.flight_tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.flight_tree.heading(col, text=col)
            width = 80 if "ID" in col else 100
            self.flight_tree.column(col, width=width, minwidth=50)
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.flight_tree.yview)
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.flight_tree.xview)
        self.flight_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.flight_tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        tree_frame.rowconfigure(0, weight=1)
        tree_frame.columnconfigure(0, weight=1)
        self.flight_tree.bind("<<TreeviewSelect>>", self.on_flight_select)
        
        # Load initial data if controller is available
        if self.flight_controller:
            self.display_flight_records()
            
    def create_flight_record(self):
        """Create a new flight record using controller."""
        if not self.flight_controller:
            messagebox.showinfo("Action", "Flight controller not available.")
            return
            
        # Get form data
        flight_data = {}
        for field, entry in self.flight_entries.items():
            flight_data[field] = entry.get()
            
        # Call controller
        success = self.flight_controller.create_flight(flight_data)
        
        if success:
            messagebox.showinfo("Success", "Flight record created successfully.")
            self.display_flight_records()
            self.clear_flight_form()
        else:
            messagebox.showerror("Error", "Failed to create flight record. Please check the data and try again.")
    
    def update_flight_record(self):
        """Update an existing flight record using controller."""
        if not self.flight_controller:
            messagebox.showinfo("Action", "Flight controller not available.")
            return
            
        # Check if a flight is selected
        selected_items = self.flight_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select a flight to update.")
            return
            
        # Get form data
        flight_data = {}
        for field, entry in self.flight_entries.items():
            flight_data[field] = entry.get()
            
        # Get flight ID
        flight_id = flight_data["Flight ID"]
        
        # Call controller
        success = self.flight_controller.update_flight(flight_id, flight_data)
        
        if success:
            messagebox.showinfo("Success", "Flight record updated successfully.")
            self.display_flight_records()
        else:
            messagebox.showerror("Error", "Failed to update flight record. Please check the data and try again.")
    
    def delete_flight_record(self):
        """Delete a flight record using controller."""
        if not self.flight_controller:
            messagebox.showinfo("Action", "Flight controller not available.")
            return
            
        # Check if a flight is selected
        selected_items = self.flight_tree.selection()
        if not selected_items:
            messagebox.showinfo("Info", "Please select a flight to delete.")
            return
            
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this flight record?")
        if not confirm:
            return
            
        # Get flight ID
        item = selected_items[0]
        values = self.flight_tree.item(item, "values")
        flight_id = values[0]
        
        # Call controller
        success = self.flight_controller.delete_flight(flight_id)
        
        if success:
            messagebox.showinfo("Success", "Flight record deleted successfully.")
            self.display_flight_records()
            self.clear_flight_form()
        else:
            messagebox.showerror("Error", "Failed to delete flight record.")
    
    def search_flight_record(self):
        """Search for flight records using controller."""
        if not self.flight_controller:
            messagebox.showinfo("Action", "Flight controller not available.")
            return
            
        # Get search term
        search_term = simpledialog.askstring("Search", "Enter search term:")
        if not search_term:
            return
            
        # Call controller
        results = self.flight_controller.search_flights(search_term)
        
        # Display results
        self.display_flight_records(results)
        self.status_var.set(f"Found {len(results)} flights matching '{search_term}'")
    
    def display_flight_records(self, flights=None):
        """Display flight records in the treeview."""
        # Clear existing records
        for item in self.flight_tree.get_children():
            self.flight_tree.delete(item)
            
        # Get records from controller if not provided
        if flights is None and self.flight_controller:
            flights = self.flight_controller.get_all_flights()
            
        # If no controller and no flights provided, show sample data
        if flights is None:
            self.populate_sample_flights()
            return
            
        # Display records
        for flight in flights:
            values = (
                flight.get("Flight ID", ""),
                flight.get("Client ID", ""),
                flight.get("Airline ID", ""),
                flight.get("Date", ""),
                flight.get("Departure", ""),
                flight.get("Arrival", ""),
                flight.get("Status", "")
            )
            self.flight_tree.insert("", "end", values=values)
            
        self.status_var.set(f"Displaying {len(flights)} flight records")
    
    def populate_sample_flights(self):
        """Add sample flight data to the treeview for demo purposes."""
        for item in self.flight_tree.get_children():
            self.flight_tree.delete(item)
        self.flight_tree.insert("", "end", values=("F001", "1", "101", "2025-03-05", "London", "Paris", "Confirmed"))
        self.flight_tree.insert("", "end", values=("F002", "2", "102", "2025-04-10", "Manchester", "New York", "Pending"))
    
    def on_flight_select(self, event):
        """Handle flight selection in treeview."""
        selected_items = self.flight_tree.selection()
        if not selected_items:
            return
        item = selected_items[0]
        values = self.flight_tree.item(item, "values")
        
        # Clear form
        self.clear_flight_form()
        
        # Populate form with selected flight data
        columns = ["Flight ID", "Client ID", "Airline ID", "Date", "Departure", "Arrival", "Status"]
        for i, col in enumerate(columns):
            if col in self.flight_entries and i < len(values):
                self.flight_entries[col].insert(0, values[i])
                
        self.status_var.set(f"Selected flight: {values[0]}")
    
    def clear_flight_form(self):
        """Clear all form fields."""
        for entry in self.flight_entries.values():
            entry.delete(0, tk.END)