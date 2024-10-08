import tkinter as tk
from PIL import Image, ImageTk


# Window Configuration
gui = tk.Tk()
gui.geometry('800x1000')
gui.title('Displaying an Image')


# Load images
img = Image.open('DSC_0308.JPG')
org_size = img.size
# img = img.resize((600,400)) # Alternatively, hardcode the size
img = img.resize(tuple([int(x/6) for x in img.size]))
photo = ImageTk.PhotoImage(img)
label = tk.Label(gui, image=photo)
label.pack()

# Start the window
gui.mainloop()
