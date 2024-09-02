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
7. Run the command cd WindowsStuff in order to navigate to the correct folder
8. Run the command python app.py in order to start the server
9. Click on the link in the terminal in order to go to the webpage

```
sudo apt install pip
pip install pytest
pip install pytesseract
pip install flask

//start server
cd WindowsStuff
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
**About Button** - Takes you to the about page where there is a tutorial on how to use MetaScan
**Submit Feedback Button** - Press to send your feedback.<br/>
**Home Button** - Takes you back to the homepage.

## Details
### Final Design Report:
[https://docs.google.com/document/d/1ot5YUuMUkqlNLCF3K9zoNZ_bk0Xqz00ZRUvFPL0qYXA/edit?usp=sharing](https://docs.google.com/document/d/18dtr7a9fTweZALLGFuHJozUKClPUyk0Ot-HKsm6Hn10/edit?usp=sharing)

### User Stories and Demos
- As a person who processes ub-04 forms, I want to be able to leave feedback that the development team can act on
  <br> &emsp; https://youtu.be/2Kptw2U5dBU
- As an employee, I want to be able to receive data that I'm interested in and save or discard others
  <br> &emsp; https://youtu.be/yU92igcdIBU
- As a person who processes many ub-04 forms for multiple patients, I want a way to upload an array of images, and have them all process at once
- As a new user, I want a tutorial to teach me how to use the software if I can't figure it out myself
- As an employee, I want to the program to be able to validate the documents for indiscrepancies and errors
  <br> &emsp; https://youtu.be/i7BHoRHBKZw
- As a user, I want the interface to be intuitive on my devices and easy to navigate
  <br> &emsp; https://www.youtube.com/watch?v=kWKtUbSsxdU
- As a user, I want to be able to use the application on my different devices (MacOS, Windows, etc)
  <br> &emsp; https://youtu.be/JyaaiEu9P3s
- As someone who uses the data extracted from the ob-04 form, I want to be able to extract the data as a JSON file
  <br> &emsp; https://www.youtube.com/watch?v=bPXc-pPXr-w

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
3. **smtplib**: send emails

## Architecture
![meta_scan_architecture (1)](https://github.com/user-attachments/assets/d7866988-21d9-4245-b81d-4ed26ba01424)

