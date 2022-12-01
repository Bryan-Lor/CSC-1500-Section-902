# Bryan Lor - EULA Agreement --------------------------------------
import os
import os.path
from datetime import date
import tkinter as tk

# Global Variables - Directory Paths
SUBPARENT_DIR = os.path.dirname(os.getcwd())
EULA_DIR = os.getcwd() + "\eula.txt"

# Attempt to open EULA file, and based on outcome return respective bool values
def openEULA():
    try:
        f = open(EULA_DIR, "r")
        f.close()
        return True
    except:
        return False

# This is the EULA text string that will be used to prompt and write EULA
def eulaText(PROGRAM_NAME, BRAND):
    text = "License. Subject to the terms and conditions of "+BRAND+" and except as otherwise provided.\n\n"
    text += BRAND+" and its suppliers grant to Customer (\"Customer\") a license to use the specific "+PROGRAM_NAME+" program modules,\nfeature set(s) or feature(s) required license fees (the \"Software\"), in object executible form only."
    text += " In addition, the subject to each of the following limitations: \n\n"
    text += "    •Unless otherwise expressly provided in the documentation, Custom embeds, script executions,\n or "+PROGRAM_NAME+" services are legally owned by "+BRAND+"\n\n"
    text += "    •Customer's use of the Software shall be limited to use on a single central processing unit, as applicable,\n or use on such greater number units as Customer may have paid "+BRAND+" the required license fee\n\n"
    text += "    •Customer's use of the Software shall also be limited as applicable to outstanding IP addresses,\n central processing unit performance restrictions set forth in "+BRAND+"'s Release Notes for the Software.\n\n"
    text += "\nNOTE: For evaluation or beta copies for which "+BRAND+" does not charge a license a license fee does not apply.\n"
    text += "\nGeneral Limitations. Except as otherwise expressly provided under this Agreement, Customer specifically agrees not to:\n\n"
    text += "    (i) transfer, assign or sublicense its license rights to any other person, nor use the secondhand "+BRAND+" equipment, and any such attempted transfer, assignment or\n\n"
    text += "    (ii) make error corrections to or otherwise modify Software, or to permit third\n\n"
    text += "    (iii) decompile, decrypt, reverse engineer, disassemble or otherwise reduce the \n   to gain access to trade secrets or confidential information in the Software.\n\n"
    text += "    (iiii) sell or distribute data without the express consent of "+BRAND+".\n"
    text += "\n"+BRAND+" is not responsible for for any data breaches, zero-day attacks, database worms (SQL Injection), or any other unilateral indemnity clauses. The sole purpose of "+PROGRAM_NAME
    text += " is to provide a software that manages information within a database, not to provide security.\n"+PROGRAM_NAME+" conducts periodic vulnerability assessments but still demands that"
    text += " all users take preventative actions.\nEULA requirements may change over time as technology and overall security landscape develops.\n"
    return text

# Create a EULA text file in which the program will write the EULA and show that the user has agreed to it
def writeEULA(programName, brandName):
    f = open(EULA_DIR, "w")
    f.write("End User License Agreement Terms\n")
    f.write(eulaText(programName, brandName))
    f.write("\nAgreement Validity: " + str(True) + "\nDate: " + str(date.today()))
    f.close()