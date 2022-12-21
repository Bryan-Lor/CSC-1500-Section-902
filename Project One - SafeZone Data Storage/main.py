# Bryan Lor - Project One --------------------------------------
import tkinter as tk
import data.library.eula as eula
import data.library.database as db

# Global Variables
PROGRAM_NAME = "SafeZone©"
BRAND = "Forestview"
BG_COLOR = "#112233"
BG_COLOR2 = "#101c2f"
FG_COLOR = "#Ffffff"

# Main Program Tkinter Window --------------------------------------
class Program(tk.Tk):
    def __init__(self):
        super().__init__()

        # Program Members
        self.programSizeX = 1680
        self.programSizeY = 920
        self.filePath = ""

        # Root Window Configuration
        self.geometry(str(self.programSizeX)+"x"+str(self.programSizeY))
        self.minsize(self.programSizeX, self.programSizeY)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight= 1)
        self.rowconfigure(2, weight=0)
        self.title(PROGRAM_NAME)
        self.configure(bg=BG_COLOR)
        #self.resizable(False, False) 

        # Create a frame to display and align info
        # 'nsew' represents the directions North, South, East, West
        frame = tk.Frame(self)
        frame.configure(bg=BG_COLOR)
        frame.grid(row = 1, column=0, sticky='nsew')
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        
        # Program Member Functions ---------------------------------------------------------------------------------------

        # On click, open file
        def openFile():
            self.filePath = db.askOpenFile()
            readFile()
            db.resetCustomer()

        # Read the file and store it
        def readFile():
            if ".xlsx" in self.filePath:
                try:
                    data = db.readExcel(self.filePath)
                    db.writeToTextField(resultField, data)
                except:
                    db.writeToTextField(resultField, "An issue occured with file reading.")
            else:
                db.writeToTextField(resultField, "Could not open file. Please make sure excel file is selected.")

        # On click, save file
        def saveData():
            db.saveExcel(resultField,self.filePath)

        # Writes to text field based on option
        def optionSelect(selection):
            if self.filePath != "":
                value = False
            else:
                value = True
            db.resetCustomer()

            # Select Option
            if db.OPTIONS[0] == str(selection):
                if self.filePath == "":
                    db.writeToTextField(resultField, "Import/Create Data", value)
                else:
                    readFile()                    
                    db.displayDatabase(resultField, db.CUSTOMERS)
                    db.toggleDataTypeWidget(dataTypeDrop)

            # Add Customer
            elif db.OPTIONS[1] == str(selection):
                db.toggleDataTypeWidget(dataTypeDrop, True)                
                if self.filePath == "":
                    db.writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields", value)                    
                    db.displayDatabase(resultField, db.CUSTOMER, False) 
                else:
                    
                    db.writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields", True)
                    db.displayDatabase(resultField, db.CUSTOMER, False)
                    db.writeToTextField(resultField, "Database:", False)
                    db.displayDatabase(resultField, db.CUSTOMERS, False)
                submitButton.config(text="Add", command=submitInput)

            # Query Data
            elif db.OPTIONS[2] == str(selection):                
                db.displayDatabase(resultField, db.CUSTOMERS)
                if self.filePath == "":                    
                    db.writeToTextField(resultField, "Import/Create Data First\nThen Select Query Type and Filter with Input", value)
                else:
                    db.writeToTextField(resultField, "Select Query Type and Filter with Input", True)
                    db.displayDatabase(resultField, db.CUSTOMERS, False)
                db.toggleDataTypeWidget(dataTypeDrop, True)
                submitButton.config(text="Search", command=queryInput)

            # Reverse Data
            elif db.OPTIONS[3] == str(selection):
                db.displayDatabase(resultField, db.CUSTOMERS)
                if self.filePath == "":                    
                    db.writeToTextField(resultField, "Import/Create Data First\nThen Press The Button To Reverse The Data.", value)
                else:
                    db.writeToTextField(resultField, "Press The Button To Reverse The Data.", True)
                    db.displayDatabase(resultField, db.CUSTOMERS, False)
                db.toggleDataTypeWidget(dataTypeDrop)
                submitButton.config(text="Reverse", command=reverseCustomer)

        # Reverse the database output
        def reverseCustomer():
            db.reverseDatabase(resultField)
            db.saveExcel(resultField, self.filePath)

        # Select Data Type
        def submitInput():
            queryType = dataTypeText.get()
            dataInput = userInput.get()            
            hasAdded = db.addUser(resultField, queryType, dataInput, self.filePath)
            if hasAdded == True:
                currentIndex = db.QUERYTYPES.index(dataTypeText.get())
                dataTypeText.set(db.QUERYTYPES[currentIndex + 1])
        
        def queryInput():
            queryType = dataTypeText.get()
            dataInput = userInput.get()            
            db.queryData(resultField, queryType, dataInput)    

        # Tkinter Widgets ----------------------------------------------------------------------------------------------

        # Title
        tk.Label(self, text='Safe Zone', font='Helvetica 32 bold', bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, sticky = 'nw')

        # Header
        tk.Label(self, text='Backend Data Storage System', font='Helvetica 12 bold', bg=BG_COLOR, fg=FG_COLOR).grid(row=0, column=0, sticky = 'sw', pady=50)

        # Instruction
        tk.Label(frame, fg=FG_COLOR, bg=BG_COLOR, text="Instructions:   Import Data -->  Select Option --> Enter Input --> Submit",
        font='Helvetica 10', padx=30).grid(row=0, column=0, sticky='e')

        # Create a center frame to display information
        centerFrame = tk.Frame(frame)
        centerFrame.configure(bg=BG_COLOR2)
        centerFrame.grid(row=1, column=0, sticky='nsew', pady=4)
        centerFrame.rowconfigure(0, weight=0)
        centerFrame.rowconfigure(1, weight=1)
        centerFrame.columnconfigure(0, weight= 1)

        # Import Button
        tk.Button(centerFrame, text="Import Data", fg=BG_COLOR, font='arial 10', command= openFile).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # Save Button
        tk.Button(centerFrame, text="Save Data", fg=BG_COLOR, font='arial 10', command=saveData).grid(row=0, column=0, sticky="e", padx=5, pady=5)

        # Results Field
        scrollbar = tk.Scrollbar(centerFrame)
        resultField = tk.Text(centerFrame, bg=FG_COLOR, fg=BG_COLOR, xscrollcommand= scrollbar.set, yscrollcommand= scrollbar.set)
        db.writeToTextField(resultField, "Import/Add Data")
        resultField.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)
        
        # Create a bottom frame to receive input and run functions
        bottomFrame = tk.Frame(frame)
        bottomFrame.configure(bg=BG_COLOR2)
        bottomFrame.grid(row=2, column=0, sticky='nsew', pady=5)
        for i in range(3):
            if i == 2:
                bottomFrame.columnconfigure(i, weight=1)
            else:
                bottomFrame.columnconfigure(i, weight=0)
        bottomFrame.rowconfigure(0, weight=1)

        # Create Options Dropdown menu
        optionsText = tk.StringVar()
        optionsText.set(db.OPTIONS[0])
        optionsDrop = tk.OptionMenu(bottomFrame, optionsText , *db.OPTIONS, command=optionSelect)
        optionsDrop.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        # Create Data Type Dropdown menu
        dataTypeText = tk.StringVar()
        dataTypeText.set(db.QUERYTYPES[0])
        dataTypeDrop = tk.OptionMenu(bottomFrame, dataTypeText , *db.QUERYTYPES)
        dataTypeDrop.grid(row=0, column=1, sticky='w', padx=5, pady=5)
        dataTypeDrop.grid_forget()

        # User Input Field
        userInput = tk.StringVar()
        inputField = tk.Entry(bottomFrame, fg=BG_COLOR, textvariable=userInput, width= 30, font='arial 10')
        inputField.grid(row=0, column=2, sticky='ew', padx=15)

        # Submit Button
        submitButton = tk.Button(bottomFrame, text="Search", fg=BG_COLOR, font='arial 10')
        submitButton.grid(row=0, column=3, sticky="e", padx=5, pady=5)

        # Footing
        tk.Label(self, text="©" + BRAND + " 2022-2023",
        bg=BG_COLOR,
        fg=FG_COLOR).grid(row=2, column=0, sticky='ew', pady=5)

# EULA Agreement Tkinter Window --------------------------------------
class EULA_Program(tk.Tk):
    def __init__(self):
        super().__init__()

        # Program Members
        self.programSizeX = 920
        self.programSizeY = 650

        # Root Window Configuration
        self.geometry(str(self.programSizeX)+"x"+str(self.programSizeY))
        self.minsize(self.programSizeX, self.programSizeY)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.title('EULA Agreement')
        self.configure(bg=BG_COLOR)

        # Create a centered frame to display and align info
        # 'nsew' represents the directions North, South, East, West
        frame = tk.Frame(self)
        frame.configure(bg=BG_COLOR)
        frame.grid(row = 1, column=0, sticky='nsew')
        for i in range(3):
            frame.columnconfigure(i, weight=1)
        frame.rowconfigure(1, weight=1)

        # Header
        tk.Label(self, text="EULA Agreement",
        font='Helvetica 18 bold',
        bg=BG_COLOR,
        fg=FG_COLOR).grid(row=0, column=0, sticky = 'w')

        # Body
        tk.Message(frame, text=eula.eulaText(PROGRAM_NAME, BRAND) + "\nBy continuing, you are stating that you understand and agree to comply to our End User License Agreement.\n",
            bg=BG_COLOR,
            fg=FG_COLOR).grid(row=0, column=0, sticky = 'w')
        
        # Accept Button - Writes a eula file and launches program
        tk.Button(frame, text="Accept", command=lambda: [eula.writeEULA(PROGRAM_NAME, BRAND), launchProgram(self)]).grid(row=1, column=1, sticky = 'w')

        # Footing
        tk.Label(self, text="©" + BRAND + " 2022-2023",
        bg=BG_COLOR,
        fg=FG_COLOR).grid(row=2, column=0)


#------------------------------------------------------------------------------------------------------------------

# Launches the base program and terminates any other windows that was passed through
def launchProgram(self = None):
    if self != None:
        self.destroy()
    window = Program()
    window.mainloop()    

if __name__ == "__main__":  
    # If EULA file exists, run program. Else, prompt EULA.
    if(eula.openEULA()) == True:
        launchProgram()     
    else:
        popup = EULA_Program()
        popup.mainloop()
