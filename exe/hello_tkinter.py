# hello_tkinter.py
import tkinter as tk

def show_hello():
    label.config(text="Hello, World!")

# สร้างหน้าต่าง
window = tk.Tk()
window.title("Tkinter Hello World")

# สร้าง Label
label = tk.Label(window, text="Click the button to say hello!")
label.pack(pady=10)

# สร้างปุ่ม
button = tk.Button(window, text="Say Hello", command=show_hello)
button.pack(pady=10)

# เริ่ม GUI loop
window.mainloop()
