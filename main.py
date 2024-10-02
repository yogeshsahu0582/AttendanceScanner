import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from ocr import extract_text
from processing import process_attendance
from utils import save_excel, preview_image

def open_file_with_preview():
    file_path = filedialog.askopenfilename(
        title="Select Attendance Image",
        filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*"))
    )
    if file_path:
        preview_image(file_path, preview_label)
        ocr_text = extract_text(file_path)
        if ocr_text:
            attendance_summary = process_attendance(ocr_text)
            save_excel(attendance_summary)

def close_app():
    root.quit()

def setup_ui():
    global preview_label
    root = tk.Tk()
    root.title("Yogesh Sahu Attendance Scanner")
    root.geometry("500x500")
    root.config(bg="#f0f0f0")

    label = tk.Label(root, text="Yogesh Sahu Attendance Scanner", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
    label.pack(pady=20)

    preview_label = tk.Label(root, text="Image Preview", font=("Arial", 12), bg="#f0f0f0", fg="#333")
    preview_label.pack(pady=10)

    btn_open = tk.Button(root, text="Open Attendance Sheet", command=open_file_with_preview, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
    btn_open.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", command=close_app, width=20, height=2, bg="#f44336", fg="white", font=("Arial", 12))
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    setup_ui()
