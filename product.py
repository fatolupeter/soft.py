import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to load data
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            global df
            df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")
            display_data_summary()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to display data summary
def display_data_summary():
    summary_text.delete('1.0', tk.END)
    if 'Grade' in df.columns:
        summary_text.insert(tk.END, df.describe())
        plot_grade_distribution()
    else:
        messagebox.showerror("Error", "The dataset must have a 'Grade' column.")

# Function to plot grade distribution
def plot_grade_distribution():
    fig, ax = plt.subplots(figsize=(6, 4))
    df['Grade'].plot(kind='hist', bins=10, ax=ax, color='skyblue')
    ax.set_title("Grade Distribution")
    ax.set_xlabel("Grade")
    ax.set_ylabel("Frequency")
    
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main application window
window = tk.Tk()
window.title("Student Grade Analysis")
window.geometry("800x600")

frame = tk.Frame(window)
frame.pack(pady=20)

load_button = tk.Button(frame, text="Load Data", command=load_data, bg='lightgreen', font=("Arial", 12))
load_button.grid(row=0, column=0, padx=5)

summary_label = tk.Label(window, text="Data Summary", font=("Arial", 14))
summary_label.pack()

summary_text = tk.Text(window, height=10, width=90)
summary_text.pack()

window.mainloop()
