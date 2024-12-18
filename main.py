import tkinter as tk

root = tk.Tk()
root.title("Ohm's Law Calculator")  # Window title
root.geometry("400x300")  # Window size

# Define the font and padding
label_font = ('Helvetica', 12)
button_font = ('Helvetica', 12, 'bold')
entry_font = ('Helvetica', 12)
padding = 10

def calculate_voltage(current, resistance):
    voltage = current * resistance
    return voltage

def calculate_current(voltage, resistance):
    current = voltage / resistance
    return current

def calculate_resistance(current, voltage):
    resistance = voltage / current
    return resistance

def on_click():
    try:
        # Error when all three fields are filled
        if entry_volts.get() and entry_resisit.get() and entry_current.get():
            result = "Error: You entered a value in all three fields!"
            result_label.config(text=result)
        # Voltage calculation
        elif entry_current.get() and entry_resisit.get():
            current = float(entry_current.get())
            resistance = float(entry_resisit.get()) 
            result = calculate_voltage(current, resistance)
            result_label.config(text=f"Voltage: {result} V")
        # Current calculation
        elif entry_volts.get() and entry_resisit.get():
            voltage = float(entry_volts.get())
            resistance = float(entry_resisit.get())
            result = calculate_current(voltage, resistance)
            result_label.config(text=f"Current: {result} A")  
        # Resistance calculation
        elif entry_current.get() and entry_volts.get():
            current = float(entry_current.get())
            voltage = float(entry_volts.get())
            result = calculate_resistance(current, voltage)
            result_label.config(text=f"Resistance: {result} Ω")
        # Error when only one value is entered
        else:
            result = "Error: You only entered one value!"
            result_label.config(text=result)
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers.")

# UI Layout
title = tk.Label(root, text="Ohm's Law Calculator (Enter two units)", font=('Helvetica', 14, 'bold'))
title.grid(row=0, column=0, columnspan=2, pady=padding)

text_current = tk.Label(root, text="Current (A) =", font=label_font)
text_current.grid(row=1, column=0, padx=padding, pady=padding, sticky='e')
entry_current = tk.Entry(root, font=entry_font)
entry_current.grid(row=1, column=1, padx=padding, pady=padding)

text_volts = tk.Label(root, text="Voltage (V) =", font=label_font)
text_volts.grid(row=2, column=0, padx=padding, pady=padding, sticky='e')
entry_volts = tk.Entry(root, font=entry_font)
entry_volts.grid(row=2, column=1, padx=padding, pady=padding)

text_resisit = tk.Label(root, text="Resistance (Ω) =", font=label_font)
text_resisit.grid(row=3, column=0, padx=padding, pady=padding, sticky='e')
entry_resisit = tk.Entry(root, font=entry_font)
entry_resisit.grid(row=3, column=1, padx=padding, pady=padding)

calc_button = tk.Button(root, text="Calculate", command=on_click, font=button_font, bg="#4CAF50", fg="white")
calc_button.grid(row=4, column=0, columnspan=2, pady=padding)

result_label = tk.Label(root, text="Result will be displayed here", font=label_font, fg="#FF5733")
result_label.grid(row=5, column=0, columnspan=2, pady=padding)

root.mainloop()
