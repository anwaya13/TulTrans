import tkinter as tk
import pandas as pd

# Function to perform the translation
def translate_text():
    hindi_input = hindi_entry.get()
    translation = translation_dict.get(hindi_input, "Translation not found!")
    output_label.config(text=translation)

# Load the dataset from the CSV file (make sure it's in the same directory)
df = pd.read_csv('hindi_to_tulu_dataset.csv')
translation_dict = dict(zip(df['Hindi'], df['Tulu']))

# Create the main window
root = tk.Tk()
root.title("Hindi to Tulu Translator")
root.geometry("500x400")

# Set up the GUI components
hindi_label = tk.Label(root, text="Enter Hindi Text:", font=("Arial", 14))
hindi_label.pack(pady=20)

hindi_entry = tk.Entry(root, font=("Arial", 14), width=30)
hindi_entry.pack(pady=10)

translate_button = tk.Button(root, text="Translate", font=("Arial", 14), command=translate_text)
translate_button.pack(pady=20)

output_label = tk.Label(root, text="Tulu Translation will appear here", font=("Arial", 14), fg="blue")
output_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
