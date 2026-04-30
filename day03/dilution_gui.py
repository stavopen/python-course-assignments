import tkinter as tk
from tkinter import messagebox
from dilution import calculate_final_volume

def calculate():
    try:
        c1 = float(entry_c1.get())
        v1 = float(entry_v1.get())
        c2 = float(entry_c2.get())

        v2 = calculate_final_volume(c1, v1, c2)
        result_label.config(text=f"V2 = {v2:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Dilution Calculator")

tk.Label(root, text="C1").pack()
entry_c1 = tk.Entry(root)
entry_c1.pack()

tk.Label(root, text="V1").pack()
entry_v1 = tk.Entry(root)
entry_v1.pack()

tk.Label(root, text="C2").pack()
entry_c2 = tk.Entry(root)
entry_c2.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

result_label = tk.Label(root, text="V2 = ")
result_label.pack()

root.mainloop()