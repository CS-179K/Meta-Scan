from PIL import Image, ImageDraw
import pytesseract
import csv

# Load image
image_path = '.\\ub04-online-6.jpg'
image = Image.open(image_path)

labels = ['Patient control num','Medical Recipient num', 'bill-type', 'fed tax num', 'statement from',
          'statement to', 'patient name', 'address a', 'address b', 'address c', 
          'address d', 'address e','birthdate', 'sex', 'admission date',
          'admission hour', 'admission type', 'admission src', 'discharge hour', 'patient status', 
          'stat', 'cc', 'ACDT', 'occurence code 1', 'occurence date 1',
          'occurence code 2', 'occurence date 2', 'occurence code 3', 'occurence date 3', 'occurence code 4', 
          'occurence date 1', 'span 1 code', 'span 1 from', 'span 1 through', 'span 2 code',
          'span 2 from', 'span 2 through']
xVals = [1637, 1637, 2357, 1547, 1848,
         2059, 378, 1278, 978, 1967,
         2087, 2418, 46, 317, 407,
         586, 677, 765, 857, 947, 
         187, 1037, 2027, 47, 137,
         347, 437, 648, 738, 948,
         1032, 1248, 1338, 1548, 1758,
         1848, 2058]
Width = [2351, 2351, 2504, 1842, 2053,
         2263, 942, 2505, 1931, 2051,
         2382, 2505, 311, 401, 581,
         625, 759, 851, 941, 1031, 
         930, 2021, 2119, 131, 341,
         431, 642, 732, 942, 1032,
         1242, 1332, 1542, 1752, 1842,
         2052, 2262]
yVals = [59, 107, 107, 207, 207, 
         207, 256, 256, 306, 306,
         306, 306, 406, 406, 406,
         406, 406, 406, 406, 406, 
         906, 406, 406, 506, 506,
         506, 506, 506, 506, 506,
         506, 506, 506, 506, 506,
         506, 506]
Height = [101, 151, 151, 250, 250, 
          250, 300, 300, 350, 350,
          350, 350, 450, 450, 450,
          450, 450, 450, 450, 450, 
          952, 450, 450, 552, 552,
          552, 552, 552, 552, 552,
          552, 552, 552, 552, 552,
          552, 552]
draw = ImageDraw.Draw(image)
final_text = ''
for val in range(len(labels)):
    draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
    roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
    final_text = final_text + ', ' + pytesseract.image_to_string(roi).strip()

claimCodes=[906, 955, 1006, 1055, 1106, 1155, 1206, 1255, 1306, 1355, 1406, 1455, 
1506, 1555, 1606, 1655, 1706, 1755, 1806, 1855, 1906, 1955]

for i in range(22):
    if (pytesseract.image_to_string(image.crop((47, claimCodes[i], 181, claimCodes[i] + 46))).strip()):
        end = False
        k=0
        j = i
        while not end and j<21:
            k = k + 1
            j = j + 1
            if (pytesseract.image_to_string(image.crop((47, claimCodes[j], 181, claimCodes[j] + 46))).strip()):
                end = True
        Description = pytesseract.image_to_string(image.crop((187, claimCodes[i], 930, claimCodes[i] + 46))).strip()
        for num in range(1, k):
            i = i + 1
            Description = Description + ' ' + pytesseract.image_to_string(image.crop((187, claimCodes[i], 930, claimCodes[i] + 46))).strip()
        i = i - 1
        print(Description + '\n')





image.show()
print(final_text)
'''
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

print(f"saved to {csv_file}")'''
