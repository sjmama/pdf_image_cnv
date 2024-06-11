from PIL import Image
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def pngs_to_pdf(image_files, output_pdf):
    # Open all PNG images and convert them to PDF format
    images = [Image.open(img).convert('RGB') for img in image_files]
    print(image_files)
    # Save the first image as the base PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])

# 예시 사용법

def select_file():
    path = filedialog.askdirectory()
    imglist=[]
    filenames = os.listdir(path)
    sp=os.path.split(path)
    print(sp)
    for filename in filenames:
        full_filename = os.path.join(path, filename)
        imglist.append(full_filename)
    imglist.sort()
    pdfpath = os.path.join(path,"../"+sp[1]+".pdf")
    pngs_to_pdf(imglist,pdfpath)
    messagebox.showinfo("sjmama","다했당")





root = tk.Tk()
root.title("sjmama")

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(padx=20, pady=10)

label = tk.Label(frame, text="이미지 폴더 선택")
label.pack(pady=5)

select_button = tk.Button(frame, text="파일 선택", command=select_file)
select_button.pack(pady=5)

root.mainloop()