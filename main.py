import tkinter as tk
from tkinter import filedialog, Label, Button, Entry
from PyPDF2 import PdfReader, PdfWriter
import os

def compress_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    
    if file_path:
        
        output_path = file_path.replace(".pdf", "_comprimido.pdf")
        
        pdf_reader = PdfReader(file_path)
        pdf_writer = PdfWriter()
        
        for page in pdf_reader.pages:
            page.compress_content_streams()
            pdf_writer.add_page(page)
                
        with open(output_path, "wb") as output_file:
            pdf_writer.write(output_file)
        
        status_label.config(text="PDF comprimido y guardado como \n {}".format(output_path))

# Crear la ventana principal
root = tk.Tk()
root.title("Compresor para archivos PDF")
# Establecer las dimensiones (ancho x alto)
root.geometry("800x300")

lbl1= Label(root, text="asdasdasd", bg="yellow")
lbl1.place(x=10, y=10, width=100, height=30)

# Botón para cargar el PDF
load_button = Button(root, fg="red", text="Cargar PDF" , command=compress_pdf)
load_button.place(x=110, y=11, width=100, height=30) 
load_button.pack()


# Etiqueta para mostrar el estado
status_label = Label(root, text="")
status_label.place(x=30, y=33, width=100, height=30)
status_label.pack()

root.mainloop()