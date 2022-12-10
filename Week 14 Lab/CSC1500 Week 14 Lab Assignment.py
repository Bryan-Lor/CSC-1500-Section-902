# Bryan Lor - Week 14 Lab Assignment
import tkinter as tk
import data.library.db as db

# Global Variables
PROGRAM_NAME = "Library App"
BRAND = "Library"
BG_COLOR = "#040f13"
BG_COLOR2 = "#000000"
FG_COLOR = "#Ffffff"

# Main Program Tkinter Window --------------------------------------
class Program(tk.Tk):
    def __init__(self):
        super().__init__()

        # Program Members
        self.programSizeX = 670
        self.programSizeY = 400
        self.filePath = ""
        self.selectedID = -1

        # Root Window Configuration
        self.geometry(str(self.programSizeX)+"x"+str(self.programSizeY))
        self.minsize(self.programSizeX, self.programSizeY)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight= 1)
        self.rowconfigure(2, weight=0)
        self.title(PROGRAM_NAME)
        self.configure(bg=BG_COLOR)

        # Upper frame to query and add books
        upperFrame = tk.Frame(self)
        upperFrame.configure(bg=BG_COLOR)
        upperFrame.grid(row=0, column=0, sticky='nsew')
        upperFrame.columnconfigure(0, weight=0)
        upperFrame.columnconfigure(1, weight=0)        
        upperFrame.columnconfigure(2, weight=1)      
        upperFrame.columnconfigure(3, weight=0)

        # Create a frame to display and align info
        centerFrame = tk.Frame(self)
        centerFrame.configure(bg=BG_COLOR)
        centerFrame.grid(row = 1, column=0, sticky='nsew')
        centerFrame.rowconfigure(1, weight=1)
        centerFrame.columnconfigure(0, weight=1)
        
        # Lower frame to query and add books
        lowerFrame = tk.Frame(self)
        lowerFrame.configure(bg=BG_COLOR)
        lowerFrame.grid(row=2, column=0, sticky='nsew')
        lowerFrame.columnconfigure(0, weight=0)
        lowerFrame.columnconfigure(1, weight=1)        
        lowerFrame.columnconfigure(2, weight=0)  

        # Program Member Functions ---------------------------------------------------------------------------------------

        # On click, open file
        def openFile():
            self.filePath = db.askOpenFile()
            readFile()
            db.resetBook()

        # Read the file and store it
        def readFile():
            if ".xlsx" in self.filePath:
                try:
                    data = db.readExcel(self.filePath)
                    optionSelect(optionText.get())
                except:
                    db.writeToTextField(resultField, "An issue occured with file reading.")
            else:
                db.writeToTextField(resultField, "Could not open file. Please make sure excel file is selected.")

        # On click, save file
        def saveData():
            db.saveExcel(resultField,self.filePath)

        # Writes to text field based on option
        def optionSelect(selection):
            submitButton.config(text="Search")
            if self.filePath != "":
                value = False
                cornerButton.config(text="Save", command=saveData)
            else:
                value = True
                cornerButton.config(text="Import", command=openFile)
            db.resetBook()    

            # Query Option
            if db.OPTIONS[0] == selection:
                if self.filePath == "":                    
                    db.writeToTextField(resultField, "Import/Create Data First\nThen Query By Data Type and Input Field", value)
                else:
                    db.writeToTextField(resultField, "Select Query Type and Filter with Input", True)
                    db.displayDatabase(resultField, db.BOOKS, False)
                db.toggleQueryTypeWidget(queryTypeDrop, True)
                submitButton.config(text="Search", command=queryInput)

            # Add Customer
            elif db.OPTIONS[1] == selection:
                db.toggleQueryTypeWidget(queryTypeDrop, True)                
                if self.filePath == "":
                    db.writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields", value)                    
                    db.displayDatabase(resultField, db.BOOK, False) 
                else:                    
                    db.writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields", True)
                    db.displayDatabase(resultField, db.BOOK, False)
                    db.writeToTextField(resultField, "Database:", False)
                    db.displayDatabase(resultField, db.BOOKS, False)
                submitButton.config(text="Add", command=submitInput)

            # Edit Data
            elif db.OPTIONS[2] == selection:          
                if self.filePath == "":                    
                    db.writeToTextField(resultField, "Import/Create Data First\nThen Enter The EntryID(Far Left Number) of Book To Edit", value) #Then Select Data Type and Enter New Inputs For Fields
                else:
                    db.writeToTextField(resultField, "Enter The EntryID(Far Left Number) of Book To Edit", True)
                    db.displayDatabase(resultField, db.BOOKS, False)
                db.toggleQueryTypeWidget(queryTypeDrop, False)
                submitButton.config(text="Select", command=submitEditID)

            # Remove Data
            elif db.OPTIONS[3] == selection:
                if self.filePath == "":
                    db.writeToTextField(resultField, "Import/Create Data First\nThen Enter ISBN And Press The Button To Remove The Book.", value)
                else:
                    db.writeToTextField(resultField, "Enter ISBN And Press The Button To Remove The Book.", True)
                    db.displayDatabase(resultField, db.BOOKS, False)
                db.toggleQueryTypeWidget(queryTypeDrop, False)
                submitButton.config(text="Delete", command=promptRemove)

        # Select Data Type
        def submitInput():
            queryType = queryTypeText.get()    
            hasAdded = db.addEntry(resultField, queryType, queryInputField.get(), self.filePath)
            if hasAdded == True:
                currentIndex = db.QUERYTYPES.index(queryType)
                if currentIndex + 1 < len(db.QUERYTYPES):
                    queryTypeText.set(db.QUERYTYPES[currentIndex + 1])
                else:
                    queryTypeText.set(db.QUERYTYPES[0])

        # Send Entry ID To Edit
        def submitEditID(): 
            self.selectedID = int(queryInputField.get())
            found = db.findEntryID(resultField, self.selectedID)
            if found:      
                db.toggleQueryTypeWidget(queryTypeDrop, True)          
                submitButton.config(text="Update", command=editEntry)
            else:
                self.selectedID = -1
        
        
        def editEntry():
            db.editEntry(resultField, self.selectedID, queryTypeText.get(), queryInputField.get(), self.filePath)
        
        # Query based on User Input
        def queryInput():          
            db.queryData(resultField, queryTypeText.get(), queryInputField.get())    

        # Attempt to remove a book
        def promptRemove():
            self.selectedID = db.getBookToRemove(resultField, queryInputField.get())
            if self.selectedID >= 0:
                submitButton.config(text="Confirm", command=confirmRemove)
                
        # Confirm removal of book
        def confirmRemove():
            db.confirmRemove(resultField, queryInputField.get(), self.selectedID, self.filePath)
            submitButton.config(text="Delete", command=promptRemove)
            self.selectedID = -1
           

        # Tkinter Widgets ----------------------------------------------------------------------------------------------

        # Hides the data type widget
        def toggleDataTypeDrop(widget, show = False):
            if show: widget.grid(row=0, column=1, sticky='w', padx=5, pady=5)
            else: widget.grid_forget()

        # Create Option Dropdown Menu
        optionText = tk.StringVar()
        optionText.set(db.OPTIONS[0])
        optionDrop = tk.OptionMenu(upperFrame, optionText , *db.OPTIONS, command=optionSelect)
        optionDrop.grid(row=0, column=0, sticky='e', padx=8, pady=5)

        # Create Query Type Dropdown Menu
        queryTypeText = tk.StringVar()
        queryTypeText.set(db.QUERYTYPES[0])
        queryTypeDrop = tk.OptionMenu(upperFrame, queryTypeText , *db.QUERYTYPES)
        queryTypeDrop.grid(row=0, column=1, sticky='e', padx=8, pady=5)

        # Query Input Field        
        userInput = tk.StringVar()
        queryInputField = tk.Entry(upperFrame, bg=FG_COLOR, fg=BG_COLOR, textvariable=userInput)
        queryInputField.grid(row=0, column=2, sticky='ew', padx=8, pady=5)

        # Query Button
        submitButton = tk.Button(upperFrame, text="Search", fg=BG_COLOR, font='arial 10')
        submitButton.grid(row=0, column=3, sticky="e", padx=8, pady=5)

        # Results Field
        scrollbar = tk.Scrollbar(centerFrame)
        resultField = tk.Text(centerFrame, bg=FG_COLOR, fg=BG_COLOR, xscrollcommand= scrollbar.set, yscrollcommand= scrollbar.set)
        resultField.grid(row=1, column=0, sticky='nsew', padx=8)                    
        db.writeToTextField(resultField, "Import/Create Data First\nThen Query By Data Type and Input Field", True)

        # Footing Label
        tk.Label(lowerFrame, text="©" + BRAND + " 2022-2023",
        bg=BG_COLOR,
        fg=FG_COLOR).grid(row=0, column=1, sticky='ew', pady=5)

        # Import/Save Button
        cornerButton = tk.Button(lowerFrame, text="Import", fg=BG_COLOR, font='arial 10', command= openFile)
        cornerButton.grid(row=0, column=2, sticky="e", padx=8, pady=5)

window = Program()
window.mainloop()    