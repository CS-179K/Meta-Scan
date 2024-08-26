from flask import Flask, request, render_template, jsonify, redirect, url_for
from PIL import Image, ImageDraw
import pytesseract
import json
import os

app = Flask(__name__)

# Path to store uploaded files and data
UPLOAD_FOLDER = 'uploads'
DATA_FILE = 'data.json'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        

        new_data = process_image(file_path)
        
        existing_data = load_data()
        

        existing_data.append(new_data)
        
   
        save_data(existing_data)
        
        return render_template('upload.html', message="File uploaded successfully! Click 'View Documents' to see results.")
    return 'Invalid file type', 400

@app.route('/view')
def view_documents():
    data = load_data()
    return render_template('result.html', json_data=data)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

def process_image(image_path):
    image = Image.open(image_path)
    width = 2550
    height = 3300
    image = image.resize((width, height))
    
    draw = ImageDraw.Draw(image)
    
    json_data = {}
    
    
    labels = ['Patient control num','Medical Recipient num', 'bill-type', 'fed tax num', 'statement from',   #1
        'statement to', 'patient name', 'address a', 'address b', 'address c', #2
        'address d', 'address e','birthdate', 'sex', 'admission date', #3
        'admission hour', 'admission type', 'admission src', 'discharge hour', 'patient status', #4
        'cc', 'ACDT', 'occurence code 1', 'occurence date 1', #5
        'occurence code 2', 'occurence date 2', 'occurence code 3', 'occurence date 3', 'occurence code 4', #6
        'occurence date 1', 'span 1 code', 'span 1 from', 'span 1 through', 'span 2 code', #7
        'span 2 from', 'span 2 through', 'value code 1', 'value code 2', 'value code 3', #8
        'value code 4', 'value code 5', 'value code 6', 'value code 7', 'value code 8', #9
        'value code 9', 'value code 10', 'value code 11', 'value code 12', 'value amount 1', #10
        'value amount 2', 'value amount 3', 'value amount 4', 'value amount 5', 'value amount 6', #11
        'value amount 7', 'value amount 8', 'value amount 9', 'value amount 10', 'value amount 11', #12
        'value amount 12']
    xVals = [1637, 1637, 2357, 1547, 1848,#1
            2059, 378, 1278, 978, 1967,   
            2087, 2418, 46, 317, 407,      
            586, 677, 765, 857, 947,       
            1037, 2027, 47, 137,    #5       
            347, 437, 648, 738, 948,       
            1032, 1248, 1338, 1548, 1758,  
            1848, 2058, 1338, 1338, 1338,  
            1338, 1728, 1728, 1728, 1728, 
            2118, 2118, 2118, 2118, 1428, #10 
            1428, 1428, 1428, 1818, 1818, 
            1818, 1818, 2208, 2208, 2208,
            2208]
    Width = [2351, 2351, 2504, 1842, 2053,      #1
            2263, 942, 2505, 1931, 2051,
            2382, 2505, 311, 401, 581,
            625, 759, 851, 941, 1031, 
            2021, 2119, 131, 341,              #5
            431, 642, 732, 942, 1032,
            1242, 1332, 1542, 1752, 1842,
            2052, 2262, 1422, 1422, 1422,
            1422, 1812, 1812, 1812, 1812,
            2202, 2202, 2202, 2202, 1722,      #10
            1722, 1722, 1722, 2112, 2112,
            2112, 2112, 2505, 2505, 2505,
            2505]
    yVals = [59, 107, 107, 207, 207,        #1
            207, 256, 256, 306, 306,       
            306, 306, 406, 406, 406,
            406, 406, 406, 406, 406, 
            406, 406, 506, 506,            #5
            506, 506, 506, 506, 506,
            506, 506, 506, 506, 506,
            506, 506, 656, 705, 756,
            805, 656, 705, 755, 805,
            656, 705, 756, 805, 656,       #10
            705, 756, 805, 656, 705,
            755, 805, 656, 705, 755,
            805]
    Height = [101, 151, 151, 250, 250,      #1
            250, 300, 300, 350, 350,
            350, 350, 450, 450, 450,
            450, 450, 450, 450, 450, 
            450, 450, 552, 552,           #5
            552, 552, 552, 552, 552,
            552, 552, 552, 552, 552,
            552, 552, 702, 753, 802,
            850, 702, 753, 802, 850,
            702, 753, 802, 850, 702,      #10
            753, 802, 850, 702, 753,
            802, 850, 702, 753, 802,
            850]


    #Seperating form in half for simplicity
    labels2= ['payer name 1', 'payer name 2', 'payer name 3', 'health plan 1', 'health plan 2',     #1
            'health plan 3', 'Rel Info 1', 'Rel Info 2', 'Rel Info 3', 'asg ben 1',
            'asg ben 2', 'asg ben 3', 'prior pay 1', 'prior pay 2', 'prior pay 3',
            'amount due 1', 'amount due 2', 'amount due 3', 'npi', 'insured name 1',
            'insured name 2', 'insured name 3', 'p. rel 1', 'p. rel 2', 'p. rel 3',           #5
            'insured id 1', 'insured id 2', 'insured id 3', 'group name 1', 'group name 2',
            'group name 3', 'insured group num 1', 'insured group num 2', 'insured group num 3', 'treatment auth code 1',
            'treatment auth code 2',  'treatment auth code 3', 'doc control num 1',  'doc control num 2', 'doc control num 3',
            'employer name 1', 'employer name 2', 'employer name 3']

    xVals2 =[46, 46, 46, 737, 737,                  #1
            737, 1188, 1188, 1188, 1277,
            1277, 1277, 1338, 1338, 1338,
            1637, 1637, 1637, 2057, 46,
            46, 46, 826, 826, 826,                 #5
            916, 916, 916, 1517, 1517,
            1517, 1967, 1967, 1967, 46,
            46, 46, 975, 975, 975,
            1756, 1756, 1756]

    Width2 = [731, 731, 731, 1182, 1182,            #1
            1182, 1242, 1242, 1242, 1322,
            1322, 1322, 1632, 1632, 1632,
            1961, 1961, 1961, 2505, 820,
            820, 820, 910, 910, 910,              #5
            1511, 1511, 1511, 1961, 1961,
            1961, 2505, 2505, 2505, 970,
            970, 970, 1751, 1751, 1751,
            2505, 2505, 2505]

    Yvals2 = [2106, 2154, 2205, 2106, 2154,         #1
            2205, 2106, 2154, 2205, 2106,
            2154, 2205, 2106, 2154, 2205,
            2106, 2154, 2205, 2056, 2306,
            2354, 2405, 2306, 2354, 2405,        #5
            2306, 2354, 2405, 2306, 2354,
            2405, 2306, 2354, 2405, 2506,
            2554, 2605, 2506, 2554, 2605,
            2506, 2554, 2605]

    Height2 = [2151, 2202, 2250, 2151, 2202,        #1
            2250, 2151, 2202, 2250, 2151,
            2202, 2250, 2151, 2202, 2250,
            2151, 2202, 2250, 2100, 2351,
            2402, 2450, 2351, 2402, 2450,        #5
            2351, 2402, 2450, 2351, 2402,
            2450, 2351, 2402, 2450, 2551,
            2602, 2650, 2551, 2602, 2650,
            2551, 2602, 2650]
    labels = labels + labels2
    xVals += xVals2
    yVals += Yvals2
    Width += Width2
    Height += Height2

    patient_info = 1
    admit_discharge_info = 1
    insurance_info = 1
    provider = 1
    occurance_info = 1
    value_codes = 1
    # categorize the sections so the user can choose what they want to get in the csv
    draw = ImageDraw.Draw(image)
    final_text = ''
    for val in range(len(labels)):
        #draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
        #patient info
        if patient_info == 1:
            if labels[val] == 'Patient control num' or labels[val] == 'patient name' or labels[val] == 'birthdate' or labels[val] == 'sex' or labels[val] == 'patient status':
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text
                json_data[labels[val]] = extracted_text

        #admission and discharge info
        if admit_discharge_info == 1:
            if labels[val] == 'admission date' or labels[val] == 'admission type' or labels[val] == 'admission hour' or labels[val] == 'discharge hour' or labels[val] == 'admission src':
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text
                json_data[labels[val]] = extracted_text     
        
        #insurance and financial info
        if insurance_info == 1:
            if labels[val] == 'bill-type' or labels[val] == 'Medical Recipient num' or labels[val] == 'fed tax num' or labels[val] == 'stat' or labels[val] == 'cc' or labels[val] == 'ACDT':
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text 
                json_data[labels[val]] = extracted_text 

        #provider info
        if provider == 1:
            if labels[val] == 'statement to' or labels[val] == 'address a' or labels[val] == 'address b' or labels[val] == 'address c' or labels[val] == 'address d' or labels[val] == 'address e' or labels[val] == 'statement from':
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text
                json_data[labels[val]] = extracted_text
        #occurance info
        if occurance_info == 1:
            if labels[val] == 'occurence code 1' or labels[val] == 'occurence date 1' or labels[val] == 'occurence code 2' or labels[val] ==  'occurence date 2' or labels[val] == 'occurence code 3' or labels[val] ==  'occurence date 3'  or labels[val] == 'occurence code 4' or labels[val] ==  'occurence date 4' or labels[val] == 'span 1 code' or labels[val] == 'span 1 from' or labels[val] == 'span 1 through' or labels[val] == 'span 2 code' or labels[val] == 'span 2 from' or labels[val] == 'span 2 through':
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text
                json_data[labels[val]] = extracted_text
        if value_codes == 1:
            if 'value code' in labels[val] or 'value amount' in labels[val]:
                draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
                roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
                extracted_text = pytesseract.image_to_string(roi).strip()
                final_text = final_text + ', ' + extracted_text
                json_data[labels[val]] = extracted_text
        if val > 50:
            draw.rectangle([xVals[val], yVals[val], Width[val], Height[val]], outline="red", width=2)
            roi = image.crop((xVals[val], yVals[val], Width[val], Height[val]))
            extracted_text = pytesseract.image_to_string(roi).strip()
            final_text = final_text + ', ' + extracted_text
            json_data[labels[val]] = extracted_text
    return json_data

if __name__ == '__main__':
    app.run(debug=True)
