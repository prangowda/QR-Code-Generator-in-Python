import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Function to generate QR code
def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text or a URL!")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    
    # Save QR code image
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")
    img_path = f"qr_codes/{data[:10]}.png"
    img.save(img_path)
    
    # Display the QR code in the GUI
    img = Image.open(img_path)
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

    messagebox.showinfo("Success", f"QR Code saved at: {img_path}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.configure(bg="white")

# Input field
entry_label = tk.Label(root, text="Enter Text or URL:", font=("Arial", 12), bg="white")
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr, font=("Arial", 12), bg="blue", fg="white")
generate_button.pack(pady=20)

# QR Code Display
qr_label = tk.Label(root, bg="white")
qr_label.pack()

# Run the GUI
root.mainloop()
