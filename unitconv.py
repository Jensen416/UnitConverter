import tkinter as tk

# Define the conversion fxn
def convert():
    input_value = float(input_entry.get())
    from_unit = from_unit_var.get()
    to_unit = to_unit_var.get()

    # Define conversion rates
    conversidon_rates = {
        ("Miles", "Kilometers"): 1.60934,
        ("Kilometers", "Miles"): 0.621371,
        ("Pounds", "Kilograms"): 0.453592,
        ("Kilograms"," Pounds"): 2.20462,
        ("Inches", "Centimeters"): 2.54,
        ("Centimeters", "Inches"): 0.393701
    }

    # Perform the conversion
    result = input_value * conversidon_rates[()]
    