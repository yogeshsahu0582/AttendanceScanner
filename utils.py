import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk

def save_to_excel(attendance_summary, output_file):
    try:
        df = pd.DataFrame(attendance_summary)
        df.to_excel(output_file, index=False)
        messagebox.showinfo("Success", f"Attendance data saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error in saving Excel file: {e}")

def save_excel(attendance_summary):
    from tkinter import filedialog
    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if output_file:
        save_to_excel(attendance_summary, output_file)

def preview_image(file_path, preview_label):
    try:
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)

        preview_label.config(image=img_tk)
        preview_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Error loading image preview: {e}")
