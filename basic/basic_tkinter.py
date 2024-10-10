import tkinter as tk


# Window Configuration
gui = tk.Tk()
gui.geometry('300x400')
gui.title('Hello World!')

# Plot text on window
headline = tk.Label(gui, text='Hello World!')
headline.pack()

# Populate GUI
gui.mainloop()
