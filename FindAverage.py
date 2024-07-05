import tkinter as tk
import tkinter.ttk as ttk  # Import ttk for the table
import statistics


def calculate_statistics():
    """Calculates the statistics of the numbers in the entry widget and displays them in a table."""
    try:
        # Get the user input from the entry widget
        numbers_string = numbers_entry.get()

        # Split the string using commas as separators
        numbers_list = [float(num) for num in numbers_string.split(",")]

        # Calculate statistics
        total_sum = sum(numbers_list)
        count = len(numbers_list)
        median = statistics.median(numbers_list)
        geometric_mean = (
            statistics.geometric_mean(numbers_list) if count > 0 else 0
        )  # Handle empty list
        largest = max(numbers_list)
        smallest = min(numbers_list)
        range_value = largest - smallest

        # Create or update the table data (if table exists)
        table_data = [
            ("Sum:", total_sum),
            ("Count:", count),
            ("Median:", median),
            ("Geometric Mean:", geometric_mean),
            ("Largest:", largest),
            ("Smallest:", smallest),
            ("Range:", range_value),
        ]
        # Calculate index values (1-based)
        # for i,(_, value) in enumerate(table_data[1:], start=1):
        #     table_data[i]= (f"{i}",value)

        # Clear table data if previously populated
        table.delete(*table.get_children())
        # Clear table data if previously populated
        for i, (statistic, value) in enumerate(table_data, start=1):
            table.insert("", tk.END, values=(i, statistic, value))

    except ValueError:
        # Handle invalid input (non-numeric characters)
        result_label.config(
            text="Error: Please enter only numbers separated by commas."
        )


# Create the main window
window = tk.Tk()
window.title("Infinite Number Statistics Calculator (Commas)")

# Create labels for instructions
instructions_label = tk.Label(
    window, text="Enter a list of numbers separated by commas"
)
instructions_label.pack(pady=10)

numbers_entry = tk.Entry(window, width=50)  # Entry widget for user input
numbers_entry.pack(pady=10)

# Create the button to trigger calculation
calculate_button = tk.Button(
    window, text="Calculate Statistics", command=calculate_statistics
)
calculate_button.pack(pady=10)

# Create the table for displaying results
table_frame = tk.Frame(window)
table_frame.pack(pady=10)

table = ttk.Treeview(
    table_frame, columns=("Index", "Statistic", "Value"), show="headings"
)
table.heading("Index", text="Index")
table.column("Index", anchor=tk.CENTER)

table.heading("Statistic", text="Statistic")

table.heading("Value", text="Value")
table.pack()

# Label for potential error messages
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Start the main event loop
window.mainloop()
