def calculate():
    try:
        c1 = float(entry_c1.get())
        v1 = float(entry_v1.get())
        c2 = float(entry_c2.get())

        # Update this line to get both values
        v2, v_add = calculate_final_volume(c1, v1, c2)
        
        # Update the label to show both
        result_label.config(text=f"V2: {v2:.2f} | Add: {v_add:.2f} buffer")

    except ValueError as e:
        messagebox.showerror("Error", str(e))