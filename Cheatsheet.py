import tkinter as tk
from tkinter import messagebox
from typing import Any

class App:
  
  def __init__(self):
    
    self.root = tk.Tk()
    
    self.menubar = tk.Menu(self.root)
    
    self.filemenu = tk.Menu(self.menubar, tearoff=0)
    self.filemenu.add_command(label="Close", command=self.on_closing)
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit", command=exit)
    
    self.menubar.add_cascade(menu=self.filemenu, label="File")
    
    self.root.config(menu=self.menubar)
    
    self.text = tk.Label(self.root, text="Your message")
    self.text.pack()
    
    self.textbox = tk.Text(self.root, height=10, width=30)
    self.textbox.bind("<KeyPress>", self.key_press)
    self.textbox.pack()
    
    self.check_state = tk.IntVar()
    
    self.check = tk.Checkbutton(self.root, text="Check me", variable=self.check_state)
    self.check.pack()
    
    self.button = tk.Button(self.root, text="OK", command=self.show_message)
    self.button.pack()
    
    self.clearbutton = tk.Button(self.root, text="Clear", command=self.clear)
    self.clearbutton.pack()
    
    self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    self.root.mainloop()
  
  def show_message(self):
    if self.check_state.get() == 0:
      print(self.textbox.get("1.0", "end-1c"))
    else:
      messagebox.showinfo(title="Message", message=self.textbox.get("1.0", "end-1c"))
      
  def key_press(self, event):
    if event.state == 12 and event.keysym == "Return":
      self.show_message()
      
  def on_closing(self):
    if messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?"):
      self.root.destroy()
      
  def clear(self):
    self.textbox.delete("1.0", "end")
    
#TODO:Make a calculator

def button(text: str, row: int, column: int, anchor: str="center", width: int=10, height: int=1):
  button = tk.Button(text=text, width=width, height=height)
  button.grid(row=row, column=column)
  button.pack(anchor=anchor)

class Calculator:
  
  def __init__(self):
    self.rt = tk.Tk()
    
    self.rt.geometry("500x800")
    
    self.rt.title("Calculator")
    
    for i in range(0,3 ):
      self.rt.grid_rowconfigure(i, weight=1)
      self.rt.grid_columnconfigure(i, weight=1)
    
    button("1" ,0, 0, anchor="nw", width=10, height=2)
    button("2" ,0, 1, anchor="nw", width=10, height=2)
    button("3" ,0, 2, anchor="nw", width=10, height=2)
    button("4" ,1, 0, anchor="nw", width=10, height=2)
    button("5" ,1, 1, anchor="nw", width=10, height=2)
    button("6" ,1, 2, anchor="nw", width=10, height=2)
    button("7" ,2, 0, anchor="nw", width=10, height=2)
    button("8" ,2, 1, anchor="nw", width=10, height=2)
    button("9" ,2, 2, anchor="nw", width=10, height=2)
    button("0" ,3, 0, anchor="nw", width=10, height=2)    
    
    self.rt.mainloop()
  
if __name__ == "__main__":
  calculator = Calculator()