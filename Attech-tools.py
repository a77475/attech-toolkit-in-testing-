import tkinter as tk

class MultiuseToolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiuse Tool")
        self.master.geometry("800x600")

        self.create_menu()
        self.create_settings_option()
        self.create_ip_to_location_map()

    def create_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="DDoS")
        file_menu.add_command(label="Bruteforce")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        menu.add_cascade(label="Tools", menu=file_menu)

    def create_settings_option(self):
        settings_frame = tk.Frame(self.master, width=200, height=100, bg="lightgray")
        settings_frame.place(x=10, y=490)

        settings_label = tk.Label(settings_frame, text="Settings", bg="lightgray")
        settings_label.pack()

        themes_option = tk.OptionMenu(settings_frame, tk.StringVar(), "Theme 1", "Theme 2", "Theme 3")
        themes_option.pack()

    def create_ip_to_location_map(self):
        map_canvas = tk.Canvas(self.master, width=600, height=400, bg="white")
        map_canvas.place(x=200, y=50)

        # Add code here to show the IP to location on the map using a suitable library

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiuseToolGUI(root)
    root.mainloop()
