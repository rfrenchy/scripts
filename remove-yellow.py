# Description: Remove yellow from a pdf, namely Otta CV, so it looks more professional
import fitz
import sys

def remove_yellow_from_pdf(pdf_path, output_path):
    # open the pdf
    pdf = fitz.open(pdf_path)

    # iterate over each pdf page
    for i in range(pdf.page_count): # should only be 2 pages
        page = pdf.load_page(i)
        pixmap = page.get_pixmap()

        # iterate over each pixel in the page
        for y in range(pixmap.height):
            for x in range(pixmap.width):
                r, g, b = pixmap.pixel(x, y)
                if r > 200 and g > 200 and b < 100:         # if YELLOW
                    pixmap.set_pixel(x, y, (255, 255, 255)) # set to WHITE

        # update the page with the modified pixmap i.e. without yellow
        page.set_pixmap(pixmap)

    # save the modified pdf
    pdf.save(output_path)
    pdf.close()

# Usage: python remove-yellow-otta.py otta-cv.pdf otta-cv-no-yellow.pdf
if __name__ == "__main__":
    pdf_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_yellow_from_pdf(pdf_path, output_path)
