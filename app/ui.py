import tkinter as tk
from tkinter import messagebox
from app.calculator.pricing import calculate_busCard_price  # use the new function

def run_ui():
    def on_calculate():
        try:
            zones = int(entry_zones.get())
            people = int(entry_people.get())
            customer_type = customer_var.get()

            price = calculate_busCard_price(zones, people, customer_type)
            label_result.config(text=f"Total Price: ${price:.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    app = tk.Tk()
    app.title("Buscard Price Calculator")

    # Zone input
    tk.Label(app, text="Number of Zones:").pack()
    entry_zones = tk.Entry(app)
    entry_zones.pack()

    # Number of people
    tk.Label(app, text="Number of People:").pack()
    entry_people = tk.Entry(app)
    entry_people.pack()

    # Customer type dropdown
    tk.Label(app, text="Customer Type:").pack()
    customer_var = tk.StringVar(value="adult")
    customer_dropdown = tk.OptionMenu(app, customer_var, "todler, less than 6 years old","child, above 6 years old","adult", "student", "pensioner", )
    customer_dropdown.pack()

    # Calculate button
    tk.Button(app, text="Calculate", command=on_calculate).pack()
    label_result = tk.Label(app, text="Total Price: $0.00")
    label_result.pack()

    app.mainloop()
