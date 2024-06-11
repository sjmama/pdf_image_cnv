import fitz  # PyMuPDF
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_images(pdf_path, high_folder, low_folder):
    # PDF 파일 열기
    pdf_document = fitz.open(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # 출력 폴더가 없다면 생성
    if not os.path.exists(high_folder):
        os.makedirs(high_folder)
    if not os.path.exists(low_folder):
        os.makedirs(low_folder)
        
    mat = fitz.Matrix(4, 4)
    
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        pix = page.get_pixmap(matrix=mat)
        
        high_image_filename = f"{pdf_name}_page_{page_number + 1}.png"
        high_image_path = os.path.join(high_folder, high_image_filename)
        
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.save(high_image_path, "PNG")

        new_width = pix.width //3
        new_height = pix.height //3
        img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
        low_image_path = os.path.join(low_folder, high_image_filename)
        img_resized.save(low_image_path, "PNG")
        
    print(f"done")

def select_file():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        high_folder = 'high'
        low_folder = 'low'
        pdf_to_images(pdf_path, high_folder, low_folder)
        messagebox.showinfo("완료")

# GUI
root = tk.Tk()
root.title("PDF to Images Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="PDF 파일 선택")
label.pack(pady=5)

select_button = tk.Button(frame, text="파일 선택", command=select_file)
select_button.pack(pady=5)

root.mainloop()
