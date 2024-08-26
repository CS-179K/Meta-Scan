# Meta Scan
## Team
<br>Ali Naqvi - https://github.com/anaqv007
<br>William Struve - https://github.com/struv
<br>Jessica Luu - https://github.com/jluu034
<br>Arman Seth - https://github.com/armanseth

## Software Introduction
Our software is called Meta Scan. It is a billing software to help Medical providers with MediCAL billing. It will take an image scan of a ub-04 form and record all the data into a CSV file.
<br>This is a ub-04 form:
<br>![image](https://github.com/user-attachments/assets/b806edd8-fc13-41bb-bcc6-783dcc262641)
<br>It is meant to expedite the current practice of manually entering the paper data.
<br>

## Installation Instructions
Installation Instructions
1. Open the terminal and run the command sudo apt install git in order to install git
2. Run the command git clone https://github.com/CS-179K/Meta-Scan.git in order to download MetaScan loacally
3. Run the command sudo apt install pip in order to install pip
4. Run the command pip install pytest in order to install pytest
5. Run the command pip install pytesseract in order to insall pytesseract
6. Run the command pip install flask in order to install flask
7. Run the command python app.py in order to start the server
8. Click on the link in the terminal in order to go to the webpage

```
sudo apt install pip
pip install flask
pip install pytest
pip install pytesseract
pip install flask

//start server
python app.py

//run tests
cd test
python -m pytest
```

## Usage Instructions
**Upload Button** - Select the file with the UB-04 form to be processed <br/>
**View Documents Button** - Takes you to another page where the processed information can be viewed. You can download the CSV, return to home, add more files, or leave feedback.<br/>
**Add More Files Button** - Promts you to upload another file and the processed data is appeneded below the initial UB-04 form.<br/>
**Download Button** - Downloads the CSV with the processed information to your files.<br/>
**Leave Feedback Button** - Takes you to another page where you can select your feedback type and write out your feedback for MetaScan.<br/>
**Submit Feedback Button** - Press to send your feedback.<br/>
**Home Button** - Takes you back to the homepage.

## Details
### Major Functional Features
1. **Document Upload**: Allows users to upload medical documents. (Story Points: 3)
2. **OCR**: Converts the image into data values. (Story Points: 6)
3. **Data Extraction**:  Returns a CSV with selected data fields. (Story Points: 2)
4. **Document Validation**: The documents will automatically catch basic errors and discrepancies. (Story Points: 7)
5. **Data Clustering**: Multiple documents can be uploaded and returned in a shared file. (Story Points: 4)
6. **Data Manipulation**: The user can choose what data they want and want to discard. (Story Points: 2)
7. **Cross-Platforming**: Different devices on different Operating Systems can use the application. (Story Points: 4)
8. **Tutorial/Help**: A tutorial video or instructions tab to use the software. (Story Points: 1)
9. **Interface**: There will be an intuitive interface to download and use the program. (Story Points: 2)
10. **Feedback**: Users can send comments and questions for developers to answer. (Story Points: 2)

### Non-Functional Features
1. **Performance and Speed**
2. **Scalability**
3. **Security and Privacy**
4. **User Interface Usability**
5. **Cross-Platform Compatibility**
6. **Support and Documentation**

### Techniques
1. **Programming Languages**: Python
2. **Web Dev Tools**: HTML/CSS/JS
3. **JS Frameworks**: React/Node.js

### Python Libraries:
1. **OpenCV**: image processing
2. **PyTesseract**: img -> text
3. **Pandas**: data manipulation
4. **Tkinter or PyQt**: UI

### Executive Design:
https://docs.google.com/document/d/1ot5YUuMUkqlNLCF3K9zoNZ_bk0Xqz00ZRUvFPL0qYXA/edit?usp=sharing

## Architecture
![meta_scan_architecture](https://github.com/user-attachments/assets/bf7e0851-ecc9-4cbd-ad06-26af4615f3da)

## Install
<br>Install flask
```
pip install flask
```

### Testing
<br>Our project uses the pytest framework for unit testing. Run the following commands to install:
```
pip install pytest
```

<br>To run:
```
python -m pytest
```
