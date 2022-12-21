# Bryan Lor - Final Lab Exam
# Week 12 Lab Assignment Overhaul
from library.functions import *
import tkinter as tk
from tkinter import filedialog
import os

# Main Program Tkinter Window --------------------------------------
class Program(tk.Tk):
    def __init__(self):
        super().__init__()

        # Program Members
        self.programName = "Salary Management Calculator"
        self.brand = "Forestview"
        self.bgColor = "#1D2024"
        self.bgColor2 = "#16171A"
        self.fgColor = "#Ffffff"
        self.programSizeX = 1400
        self.programSizeY = 920
        self.currentDir = os.getcwd()
        self.filePath = ""
        self.employeeDatabase = None
        self.underpaidSalaries = None
        self.salaryRaises = None

        # Root Window Configuration
        self.geometry(str(self.programSizeX)+"x"+str(self.programSizeY))
        self.minsize(self.programSizeX, self.programSizeY)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight= 1)
        self.rowconfigure(2, weight=0)
        self.title(self.programName)
        self.configure(bg=self.bgColor)

        # Main Frame
        mainFrame = tk.Frame(self)
        mainFrame.configure(bg=self.bgColor)
        mainFrame.grid(row = 1, column=0, sticky='nsew')
        mainFrame.rowconfigure(1, weight=1)
        mainFrame.columnconfigure(0, weight=1)        
        mainFrame.columnconfigure(1, weight=1)        
        mainFrame.columnconfigure(2, weight=1)

        # Footer Frame
        footerFrame = tk.Frame(self)
        footerFrame.configure(bg=self.bgColor)
        footerFrame.grid(row = 2, column=0, sticky='nsew')
        footerFrame.columnconfigure(0, weight=1)        
        footerFrame.columnconfigure(1, weight=1)        
        footerFrame.columnconfigure(2, weight=1)
        
        # Program Member Functions ---------------------------------------------------------------------------------------

        # On click, open file
        def openFile():
            self.filePath = filedialog.askopenfilename(initialdir=self.currentDir)
            
            # Check if excel file and attempt to read it
            if ".xlsx" in self.filePath:
                try:
                    data = importFile(self.filePath)

                    # Employee Database
                    self.employeeDatabase = importDatabase(data)
                    printEmployeeDatabase(employeeField, self.employeeDatabase, "Employee Database:", clear=True)

                    # Underpaid Salaries
                    self.underpaidSalaries = getUnderpaidSalaries(self.employeeDatabase)
                    printDatabase(underpaidField, self.underpaidSalaries, "Underpaid Salaries: ", clear=True)

                    # Company Raises
                    self.salaryRaises = getSalaryRaises(self.employeeDatabase)
                    printDatabase(salaryRaisesField, self.salaryRaises, "Salary Raises:", clear=True)
                except:
                    writeToTextField(employeeField, "An issue occured with file reading.")
            else:
                writeToTextField(employeeField, "Could not open file.\nPlease make sure excel file is selected and try again.", clear=True)

        # On click, save employees database file
        def saveEmployeeData():
            if self.filePath == "":
                return
            hasSaved = saveExcel(self.employeeDatabase, self.currentDir)
            if hasSaved:
                writeToTextField(employeeField, "Employee Database Successfully Saved!", True)
                printEmployeeDatabase(employeeField, self.employeeDatabase, "Employee Database:")

        # On click, save underpaid employees as file
        def saveUnderpaidData():
            if self.filePath == "":
                return
            saveData = createSaveFile(self.underpaidSalaries)
            hasSaved = saveExcel(saveData, self.currentDir, name="Underpaid Salaries")
            if hasSaved:
                writeToTextField(underpaidField, "Underpaid Salaries Successfuly Exported!", True)
                printDatabase(underpaidField, self.underpaidSalaries, "Underpaid Salaries: ")
        
        # On click, save employee raises as file
        def saveRaisesData():
            if self.filePath == "":
                return
            saveData = createSaveFile(self.underpaidSalaries)
            saved = saveExcel(saveData, self.currentDir, name="Salary Raises")
            if saved:
                writeToTextField(salaryRaisesField, "Salary Raises Successfuly Exported!", True)
                printDatabase(salaryRaisesField, self.salaryRaises, "Salary Raises:")
        
        # Tkinter Widgets ----------------------------------------------------------------------------------------------

        # Results Field
        scrollbar = tk.Scrollbar(mainFrame)
        employeeField = tk.Text(mainFrame, bg=self.bgColor2, fg=self.fgColor, xscrollcommand= scrollbar.set, yscrollcommand= scrollbar.set)
        writeToTextField(employeeField, "Import Employee Excel Sheet")
        employeeField.grid(row=1, column=0, sticky='nsew', padx=8, pady=8)

            # Results Field
        scrollbar = tk.Scrollbar(mainFrame)
        underpaidField = tk.Text(mainFrame, bg=self.bgColor2, fg=self.fgColor, xscrollcommand= scrollbar.set, yscrollcommand= scrollbar.set)
        writeToTextField(underpaidField, "Import Data To Calculate Underpaid")
        underpaidField.grid(row=1, column=1, sticky='nsew', padx=8, pady=8)

            # Results Field
        scrollbar = tk.Scrollbar(mainFrame)
        salaryRaisesField = tk.Text(mainFrame, bg=self.bgColor2, fg=self.fgColor, xscrollcommand= scrollbar.set, yscrollcommand= scrollbar.set)
        writeToTextField(salaryRaisesField, "Import Data To Calculate Raises")
        salaryRaisesField.grid(row=1, column=2, sticky='nsew', padx=8, pady=8)

        # Import Employee Database Button
        tk.Button(mainFrame, text="Import Database", fg=self.bgColor, font='arial 10', command= openFile).grid(row=0, column=0, sticky="w", padx=5, pady=5)

        # Save Employee Database Button
        tk.Button(mainFrame, text="Save", fg=self.bgColor, font='arial 10', command=saveEmployeeData).grid(row=0, column=0, sticky="e", padx=5, pady=5)

        # Export Underpaid Salaries Button
        tk.Button(mainFrame, text="Export", fg=self.bgColor, font='arial 10', command=saveUnderpaidData).grid(row=0, column=1, sticky="e", padx=5, pady=5)

        # Export Salary Raises Button
        tk.Button(mainFrame, text="Export", fg=self.bgColor, font='arial 10', command=saveRaisesData).grid(row=0, column=2, sticky="e", padx=5, pady=5)

        # Footing
        tk.Label(footerFrame, text="©" + self.brand + " 2022-2023", bg=self.bgColor, fg=self.fgColor).grid(row=0, column=1, sticky='ew', pady=5)


if __name__ == "__main__":  
    window = Program()
    window.mainloop() 

    