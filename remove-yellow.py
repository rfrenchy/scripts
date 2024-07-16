# Description: Remove yellow from a pdf, namely Otta CV, so it looks more professional
# PyMuPDF - https://pymupdf.readthedocs.io/en/latest/index.html
import fitz
import sys
import math

def remove_yellow_from_pdf(pdf_path, output_path):
    # open the pdf
    pdf = fitz.open(pdf_path)

    # iterate over each pdf page
    page = pdf.load_page(0)
    pixmap = page.get_pixmap()


    footer = math.floor(pixmap.height * 0.9) 

    # iterate over each pixel in the page
    for y in range(pixmap.height):        
        for x in range(pixmap.width):
            r, g, b = pixmap.pixel(x, y)

            # if yellow, set to white
            if r > 200 and g > 200 and b < 100:         
                pixmap.set_pixel(x, y, (255, 255, 255))
            # if in footer area, set to white
            if y > footer:
                #print(y)
                pixmap.set_pixel(x, y, (255, 255, 255)) 

    # save the modified pdf
    pixmap.save(output_path)
    
    # pdf.save(output_path)
    pdf.close()

# Usage: python remove-yellow-otta.py otta-cv.pdf otta-cv-no-yellow.pdf
if __name__ == "__main__":
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_yellow_from_pdf(pdf_path, output_path)
