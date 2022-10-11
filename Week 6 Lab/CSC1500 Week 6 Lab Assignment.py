#Bryan Lor - Week 6 Lab Assignment
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Program(tk.Tk):
  def __init__(self):
    super().__init__()

    # Root Window Configuration
    self.title('My Awesome App')
    self.geometry('500x300')

    # Label
    self.label = ttk.Label(self, text='Hello, Tkinter!')
    self.label.pack()

    # Button
    self.button = ttk.Button(self, text='Click Me')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  window = Program()
  window.mainloop()