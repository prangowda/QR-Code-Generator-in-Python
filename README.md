# **QR Code Generator in Python**  

This project is a **QR Code Generator** built using Python. It allows users to generate QR codes from any text or URL and save them as images.

---

## **📌 Features**  

✔ Generate QR codes from **text, URLs, or any data**  
✔ **Save QR codes** as PNG images  
✔ **Display QR codes** instantly in a GUI  
✔ **Cross-platform** (Windows, macOS, Linux)  

---

## **🛠️ Technologies Used**  

| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Main programming language |  
| **qrcode**  | QR code generation |  
| **Pillow (PIL)**  | Image handling |  
| **Tkinter**  | GUI for user interaction |

---

## **📂 Project Structure**  

```
/QR_Code_Generator
│── qr_generator.py         # Main Python script
│── README.md               # Documentation
│── qr_codes/               # Folder where generated QR codes are saved
│── requirements.txt        # Dependencies
```

---

## **🔧 Installation Guide**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/prangowda/QR_Code_Generator.git
cd QR_Code_Generator
```

### **2️⃣ Install Dependencies**  
```sh
pip install qrcode[pil] pillow
```

### **3️⃣ Run the QR Code Generator**  
```sh
python qr_generator.py
```

---

## **📜 How It Works**  

1. The user **enters text or a URL**  
2. The program **generates a QR code**  
3. The QR code is **displayed** and **saved as an image**  

---

## **📊 Sample Output**  

### **📸 Generated QR Code Example**  
![Sample QR Code](qr_codes/sample_qr.png)  

---

## **🚀 Future Enhancements**  
✅ Allow users to **scan QR codes**  
✅ Add **color customization** for QR codes  
✅ Generate **bulk QR codes** from a list  

---

## **🤝 Contributing**  
We welcome contributions! Follow these steps:  
1. **Fork** the repository  
2. **Create** a new branch (`feature-xyz`)  
3. **Commit** your changes  
4. **Push** to your branch and submit a **Pull Request**  
