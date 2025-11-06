#########################
### MySummerSaveSlots ###
## App for MySummerCar ##
#########################

# Modules
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
import os

# Variables

# Functions

# Classes
class Main:
    def __init__(self):
        print("MySummerSaveSlots console debug")
        print("Welcome! Version: v0.0.1-dev")

        Status, Path = self.AttemptToFindUserLocalLow()
        if Status:
            print(f"Found automatically: {Path}")
            self.Path = Path
        else:
            print("Failed to find path, asking manually...")
            Status, Path = self.AskForPathManually()
            if Status:
                print(f"Got path manually at {Path}")
                self.Path = Path
            else:
                print("Failed 2/2 chances, exiting.")
                exit()

        self.SetupWindow()

    def AttemptToFindUserLocalLow(self):
        # Construct the path
        LocalLowPath = os.path.join(os.getenv("USERPROFILE"), "AppData", "LocalLow", "Amistech", "My Summer Car")
        
        # Check for validity
        if os.path.exists(LocalLowPath):
            return True, LocalLowPath
        else:
            return False, None

    def AskForPathManually(self):
        GivenPath = filedialog.askdirectory(title="Open the My Summer Car folder in AppData", mustexist=True)

        if GivenPath and os.path.exists(GivenPath):
            return True, GivenPath
        else:
            return False, None
        
    def ManuallyAutoFind(self):
        Status, Path = self.AttemptToFindUserLocalLow()
        if Status:
            msgbox.showinfo("MySummerSaveSlots", "Attached to folder successfully!")
            self.Path = Path
        else:
            msgbox.showerror("MySummerSaveSlots", "Failed to attach to folder!")
            Status, Path = self.AskForPathManually()

            if Status and Path:
                msgbox.showinfo("MySummerCarSaveSlots", "Attached to folder manually!")

    def SetupWindow(self):
        self.WindowRoot = tk.Tk()

        self.WindowRoot.title("MySummerSaveSlots | v0.0.1a")
        self.WindowRoot.geometry("500x400")
        self.WindowRoot.minsize(width=500, height=400)

        for x in range(4):
            self.WindowRoot.grid_rowconfigure(x, weight=1)
        for y in range(5):
            self.WindowRoot.grid_columnconfigure(y, weight=1)

        # Menu setup!!11!!
        self.WindowMenu = tk.Menu(master=self.WindowRoot)
        self.FileMenu = tk.Menu(self.WindowMenu, tearoff=0)

        self.WindowMenu.add_cascade(label="File", menu=self.FileMenu)
        self.FileMenu.add_command(label="Find MSC AppData folder (auto)", command=self.ManuallyAutoFind)
        self.FileMenu.add_command(label="Find MSC AppData folder (manual)", command=self.AskForPathManually)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit safely", command=exit)

        # Table shit
        columns = ("Name", "Save time", "Size")
        self.SaveTreeView = ttk.Treeview(self.WindowRoot, columns=columns, show="headings", selectmode="browse")

        for col in columns:
            self.SaveTreeView.heading(col, text=col)
            self.SaveTreeView.column(col, width=100)
        
        Scrollbar = ttk.Scrollbar(self.WindowRoot, orient="vertical", command=self.SaveTreeView.yview)
        self.SaveTreeView.config(yscrollcommand=Scrollbar.set)

        Scrollbar.pack(side="right", fill="y")
        self.SaveTreeView.pack(side="left", fill="both", expand=True)

        #for i in range(50):
            #self.SaveTreeView.insert("", "end", values=(i, f"Name {i}", str(20 + i % 10) + "kB"))

        self.WindowRoot.config(menu=self.WindowMenu)
        self.WindowRoot.mainloop()

Main()
