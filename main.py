from PIL import Image, ImageDraw
import pytesseract
import csv

# Load image
image_path = 'C:\\Users\\anaqv\\OneDrive\\Documents\\CS179_Project_Personal\\ub04-online.jpg'
image = Image.open(image_path)

x, y = 1290, 250
rect_width, rect_height = 500, 50

draw = ImageDraw.Draw(image)
draw.rectangle([x, y, x + rect_width, y + rect_height], outline="red", width=2)


#image.show()


roi = image.crop((x, y, x + rect_width, y + rect_height))


final_text = pytesseract.image_to_string(roi)
final_text = final_text.strip()


#final_text = extracted_text.strip() + ", Ali Naqvi"
roi = image.crop((190, 900, 190 + rect_width, 900 + rect_height))
extracted_text = pytesseract.image_to_string(roi)
final_text = final_text + ', ' + extracted_text.strip()
draw.rectangle([190, 900, 190 + rect_width, 900 + rect_height], outline="red", width=2)
image.show()


print("Extracted text:")
print(final_text)

csv_file = 'extracted_text.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Extracted Text"])
    writer.writerow([final_text])

print(f"saved to {csv_file}")