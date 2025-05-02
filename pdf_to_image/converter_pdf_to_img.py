import fitz  # PyMuPDF
import os

# Folder paths
pdf_folder = './samsung/'
conversion_folder = './samsung_subway_img/'

# Ensure the conversion folder exists
os.makedirs(conversion_folder, exist_ok=True)

# Set zoom factor for increasing resolution (1.0 = 72 DPI, 2.0 = 144 DPI, etc.)
zoom = 2.0
matrix = fitz.Matrix(zoom, zoom)

# Iterate over each PDF file in the folder
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith('.pdf'):
        print(f"Check file: {pdf_file}")
        pdf_path = os.path.join(pdf_folder, pdf_file)
        doc = fitz.open(pdf_path)
        print(f"Opened document with {len(doc)} pages.")

        pdf_name = os.path.splitext(pdf_file)[0]
        pdf_conversion_folder = os.path.join(conversion_folder, pdf_name)
        os.makedirs(pdf_conversion_folder, exist_ok=True)

        # Convert only valid page numbers
        for page_num in range(min(1000, len(doc))):
            try:
                page = doc.load_page(page_num)
                pix = page.get_pixmap(matrix=matrix)
                image_path = os.path.join(pdf_conversion_folder, f"{pdf_name}_page_{page_num + 1}.png")
                pix.save(image_path)
                print(f"Saved {image_path}")
            except Exception as e:
                print(f"Error processing page {page_num + 1}: {e}")

        doc.close()
