from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def jpeg_to_pdf(jpeg_path, pdf_path):
    # Open the image file
    image = Image.open(jpeg_path)

    # Create a PDF with the same dimensions as the image
    c = canvas.Canvas(pdf_path, pagesize=(image.width, image.height))

    # Draw the image on the PDF
    c.drawImage(jpeg_path, 0, 0, width=image.width, height=image.height)

    # Save the PDF
    c.save()

# Path to the JPEG file
jpeg_path = 'example.jpg'  # Change this to your image file path

# Path to save the PDF
pdf_path = 'output.pdf'  # Change this to your desired output file path

# Convert the JPEG to PDF
jpeg_to_pdf(jpeg_path, pdf_path)

print(f'Converted {jpeg_path} to {pdf_path}')