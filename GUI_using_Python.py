import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()

apps = []

if os.path.isfile('Save.txt'):
    with open('Save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]
        print(apps)

def addapp():
    for w in frame.winfo_children():
        w.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select the file you wanna open bruh",
                                          filetypes=(("Executable Files", "*.exe"), ("All Files", "*.*")))
    apps.append(filename)
    print(apps)
    for a in apps:
        label1 = tk.Label(frame, text = a, bg="Black", fg = "White")
        label1.pack()



def runapps():
    for i in apps:
        os.startfile(i)

canvas = tk.Canvas(root, height=500, width=500, bg="#3A4263")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# o_f is variable made for the Open File Button
o_f = tk.Button(root, text="Open File", fg="White", bg="#3A4263", padx=10, pady=5, command=addapp)
o_f.pack()

# similarly r_a is a variable made for the Run Apps button
r_a = tk.Button(root, text="Run Application", fg="White", bg="#3A4263", padx=10, pady=5, command=runapps)
r_a.pack()

for q in apps:
    label1 = tk.Label(frame, text=q)
    label1.pack()

root.mainloop()

with open('Save.txt', 'w') as f:
    for x in apps:
        f.write(x + ',')
