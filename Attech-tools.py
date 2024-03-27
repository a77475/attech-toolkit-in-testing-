#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser
from ttkthemes import ThemedStyle
from geopy.geocoders import Nominatim

class AttackToolkit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AtTech Toolkit")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")

        self.load_logo()
        self.create_topbar_menu()

    def load_logo(self):
        logo_path = "logo.png"  # Adjust the file path as needed
        if os.path.exists(logo_path):
            self.logo = Image.open(logo_path)
            self.logo = self.logo.resize((200, 100), Image.ANTIALIAS)
            self.logo = ImageTk.PhotoImage(self.logo)
            label_logo = ttk.Label(self, image=self.logo, background="#f0f0f0")
            label_logo.pack(pady=20, padx=10)
        else:
            print("Logo file not found.")

    def create_topbar_menu(self):
        topbar_frame = tk.Frame(self, bg="#333")
        topbar_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        ttk.Button(topbar_frame, text="DDoS", command=self.open_ddos, style="Topbar.TButton").pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(topbar_frame, text="Brute Force", command=self.open_brute_force, style="Topbar.TButton").pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(topbar_frame, text="IP to Location", command=self.open_ip_to_location, style="Topbar.TButton").pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(topbar_frame, text="Settings", command=self.open_settings, style="Topbar.TButton").pack(side=tk.RIGHT, padx=10, pady=10)

    def open_ddos(self):
        ddos_window = DDoSWindow(self)

    def open_brute_force(self):
        brute_force_window = BruteForceWindow(self)

    def open_ip_to_location(self):
        ip_to_location_window = IPToLocationWindow(self)

    def open_settings(self):
        settings_window = SettingsWindow(self)

class DDoSWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("DDoS Tool")
        self.geometry("400x250")
        self.configure(bg="#f0f0f0")

        ttk.Label(self, text="DDoS Tool", font=("Helvetica", 20), background="#f0f0f0").pack(pady=20)

        self.entry_ip = self.create_entry("Target IP:")
        self.entry_port = self.create_entry("Target Port:", pady=(10, 0))
        self.entry_duration = self.create_entry("Duration (seconds):", pady=(10, 0))

        ttk.Button(self, text="Start DDoS", command=self.start_ddos, style="Main.TButton").pack(pady=(20,10), fill=tk.X)

    def create_entry(self, label_text, **kwargs):
        frame = ttk.Frame(self, padding=(50, 0), style="Main.TFrame")
        frame.pack(fill=tk.X, **kwargs)
        ttk.Label(frame, text=label_text, background="#f0f0f0").pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        return entry

    def start_ddos(self):
        target_ip = self.entry_ip.get()
        target_port = int(self.entry_port.get())
        duration = int(self.entry_duration.get())
        # Call your ddos function here

class BruteForceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Brute Force Tool")
        self.geometry("400x250")
        self.configure(bg="#f0f0f0")

        ttk.Label(self, text="Brute Force Tool", font=("Helvetica", 20), background="#f0f0f0").pack(pady=20)

        self.entry_url = self.create_entry("URL:")

    def create_entry(self, label_text, **kwargs):
        frame = ttk.Frame(self, padding=(50, 0), style="Main.TFrame")
        frame.pack(fill=tk.X, **kwargs)
        ttk.Label(frame, text=label_text, background="#f0f0f0").pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

class IPToLocationWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("IP to Location Tool")
        self.geometry("400x400")
        self.configure(bg="#f0f0f0")

      ttk.Label(self, text="IP to Location Tool", font=("Helvetica", 20), background="#f0f0f0").pack(pady=20)

