import tkinter as tk
import tkinter.ttk as ttk
import statistics
import pandas as pd
from tkinter import filedialog  # Corrected import statement

def calculate_statistics():
    """Calculates the statistics of the numbers in the entry widget and displays them in a table."""
    try:
        # Clear previous error message
        result_label.config(text="")

        # Get the user input from the entry widget
        numbers_string = numbers_entry.get()

        # Split the string using commas as separators and convert to float
        numbers_list = [float(num.strip()) for num in numbers_string.split(",")]

        # Calculate statistics
        total_sum = sum(numbers_list)
        count = len(numbers_list)
        average = total_sum / count if count > 0 else 0
        median = statistics.median(numbers_list)
        geometric_mean = statistics.geometric_mean(numbers_list) if count > 0 else 0
        largest = max(numbers_list)
        smallest = min(numbers_list)
        range_value = largest - smallest

        # Prepare table data
        table_data = [
            ("Sum", total_sum),
            ("Count", count),
            ("Average", round(average, 2)),
            ("Median", median),
            ("Geometric Mean", round(geometric_mean, 2)),
            ("Largest", largest),
            ("Smallest", smallest),
            ("Range", range_value),
        ]

        # Clear table data if previously populated
        table.delete(*table.get_children())

        # Insert data into the table
        for i, (statistic, value) in enumerate(table_data, start=1):
            table.insert("", tk.END, values=(i, statistic, value))

    except ValueError:
        # Handle invalid input (non-numeric characters)
        result_label.config(text="Error: Please enter only numbers separated by commas.")

def clear_table():
    """Clears the table data."""
    table.delete(*table.get_children())
    result_label.config(text="Table cleared.")

def export_to_excel():
    """Exports the table data to an Excel file."""
    try:
        # Create a DataFrame from table data
        data = []
        for item in table.get_children():
            values = table.item(item, 'values')
            data.append([values[1], values[2]])

        df = pd.DataFrame(data, columns=["Statistic", "Value"])

        # Choose file path for saving
        file_path = tk.filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        # If file_path is not None (user clicked save)
        if file_path:
            # Write DataFrame to Excel
            df.to_excel(file_path, index=False)
            result_label.config(text=f"Data exported to {file_path}")

    except Exception as e:
        result_label.config(text=f"Error exporting to Excel: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Infinite Number Statistics Calculator")
window.geometry("600x500")
window.resizable(False, False)
window.configure(background="#f0f0f0")

# Instructions label
instructions_label = tk.Label(window, text="Enter numbers separated by commas:")
instructions_label.pack(pady=10)

# Entry widget
numbers_entry = tk.Entry(window, width=50)
numbers_entry.pack(pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate Statistics", command=calculate_statistics)
calculate_button.pack(pady=10)

# Frame for table
table_frame = tk.Frame(window, bg="#ffffff")
table_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Table
table = ttk.Treeview(table_frame, columns=("Index", "Statistic", "Value"), show="headings")
table.heading("Index", text="Index")
table.column("Index", anchor=tk.CENTER, width=50)

table.heading("Statistic", text="Statistic")
table.column("Statistic", anchor=tk.CENTER, width=150)

table.heading("Value", text="Value")
table.column("Value", anchor=tk.CENTER, width=90)

table.pack(fill="both", expand=True)

# Footer frame
footer_frame = tk.Frame(window, height=100, bg="#e0e0e0")
footer_frame.pack(fill=tk.X)

# Clear Table button in footer
clear_button = tk.Button(footer_frame, text="Clear Table", command=clear_table)
clear_button.pack(pady=10, padx=20, side=tk.LEFT)

# Export to Excel button in footer
export_button = tk.Button(footer_frame, text="Export to Excel", command=export_to_excel)
export_button.pack(pady=10, padx=20, side=tk.LEFT)

# Label for potential error messages
result_label = tk.Label(window, text="", fg="red", wraplength=500)
result_label.pack(pady=10, fill="x")

# Center window on screen
window.update_idletasks()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = (screen_width // 2) - (window.winfo_width() // 2)
window_y = (screen_height // 2) - (window.winfo_height() // 2)
window.geometry(f"+{window_x}+{window_y}")

# Start the main event loop
window.mainloop()
