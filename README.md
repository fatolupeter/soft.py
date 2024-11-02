import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize the main application window
app = tk.Tk()
app.title("Data Analysis Software")
app.geometry("800x600")
app.config(bg="#f0f4f8")  # Set a light background color for better UI

# Header Label
header_label = tk.Label(app, text="Data Analysis Software", font=("Helvetica", 24, "bold"), bg="#0073e6", fg="white")
header_label.pack(fill=tk.X, pady=(0, 20))

# Global variable to store DataFrame
data = None

def load_file():
    """Function to load a CSV file."""
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            data = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")
            show_data_preview()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")

def show_data_preview():
    """Display a preview of the loaded data in the interface."""
    if data is not None:
        data_preview.delete(*data_preview.get_children())
        # Insert column headers
        data_preview["columns"] = list(data.columns)
        data_preview["show"] = "headings"
        for col in data.columns:
            data_preview.heading(col, text=col)
        # Insert rows (only first 5 for preview)
        for index, row in data.head(5).iterrows():
            data_preview.insert("", "end", values=list(row))
    else:
        messagebox.showwarning("Warning", "No data loaded.")

def visualize_data():
    """Generate a chart based on the selected options."""
    if data is None:
        messagebox.showwarning("Warning", "Please load data first.")
        return

    chart_type = chart_type_var.get()
    column = column_var.get()

    if chart_type == "Histogram":
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True, color="#0073e6")
        plt.title(f"Histogram of {column}")
    elif chart_type == "Bar Chart":
        plt.figure(figsize=(8, 6))
        data[column].value_counts().plot(kind="bar", color="#0073e6")
        plt.title(f"Bar Chart of {column}")
    elif chart_type == "Box Plot":
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=data[column], color="#0073e6")
        plt.title(f"Box Plot of {column}")
    plt.xlabel(column)
    plt.show()

# Frame for loading data and options
frame = tk.Frame(app, bg="#f0f4f8")
frame.pack(pady=20)

# Load data button
load_button = tk.Button(frame, text="Load Data", command=load_file, font=("Helvetica", 12), bg="#0073e6", fg="white", width=15)
load_button.grid(row=0, column=0, padx=10, pady=10)

# Chart type dropdown
chart_type_var = tk.StringVar()
chart_type_var.set("Histogram")  # default option

chart_type_label = tk.Label(frame, text="Select Chart Type:", font=("Helvetica", 12), bg="#f0f4f8")
chart_type_label.grid(row=0, column=1, padx=10, pady=10)
chart_type_dropdown = ttk.Combobox(frame, textvariable=chart_type_var, values=["Histogram", "Bar Chart", "Box Plot"], font=("Helvetica", 12))
chart_type_dropdown.grid(row=0, column=2, padx=10, pady=10)

# Column selection dropdown
column_var = tk.StringVar()
column_label = tk.Label(frame, text="Select Column:", font=("Helvetica", 12), bg="#f0f4f8")
column_label.grid(row=1, column=1, padx=10, pady=10)
column_dropdown = ttk.Combobox(frame, textvariable=column_var, font=("Helvetica", 12))
column_dropdown.grid(row=1, column=2, padx=10, pady=10)

# Update columns after data load
def update_columns():
    if data is not None:
        column_dropdown["values"] = data.columns.tolist()
    else:
        messagebox.showwarning("Warning", "No data loaded.")

# Update columns when data is loaded
load_button.config(command=lambda: [load_file(), update_columns()])

# Visualize button
visualize_button = tk.Button(app, text="Visualize Data", command=visualize_data, font=("Helvetica", 12), bg="#0073e6", fg="white", width=15)
visualize_button.pack(pady=20)

# Data preview table
data_preview = ttk.Treeview(app, height=8)
data_preview.pack(pady=20, fill=tk.X, padx=20)

# Run the application
app.mainloop()
# soft.py
