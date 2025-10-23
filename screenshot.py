import time
import pyautogui
import tkinter as tk

def screenshot():
    name = time.strftime("%Y%m%d-%H%M%S") # Format: YYYYMMDD-HHMMSS 
    name = 'C:/Users/User/OneDrive/Documents/Desktop/Python Tutorial/Sample Python Projects/screenshot data/{}.png'.format(name) 
    img = pyautogui.screenshot(name)
    img.show()
    print(f"Screenshot saved to {name}")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "Take Screenshot",
    command = screenshot)
button.pack(side = tk.LEFT)

close = tk.Button(
    frame,
    text = "QUIT",
    command = quit)
close.pack(side = tk.LEFT)

root.mainloop()