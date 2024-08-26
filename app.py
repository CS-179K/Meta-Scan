from flask import Flask, render_template, request, jsonify
import subprocess
import os
from werkzeug.utils import secure_filename
import traceback
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_folder='static')
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            result = subprocess.run(['python3', 'main.py', file_path], capture_output=True, text=True, check=True)
            
            # Process the output into a structured format
            lines = result.stdout.strip().split('\n')
            labels = ['Patient control num', 'Medical Recipient num', 'bill-type', 'fed tax num', 'statement from',
                      'statement to', 'patient name', 'address a', 'address b', 'address c', 
                      'address d', 'address e', 'birthdate', 'sex', 'admission date',
                      'admission hour', 'admission type', 'admission src', 'discharge hour', 'patient status', 
                      'stat', 'cc', 'ACDT', 'occurence code 1', 'occurence date 1',
                      'occurence code 2', 'occurence date 2', 'occurence code 3', 'occurence date 3', 'occurence code 4', 
                      'occurence date 1', 'span 1 code', 'span 1 from', 'span 1 through', 'span 2 code',
                      'span 2 from', 'span 2 through']
            data = {'data': [{'label': labels[i], 'value': lines[i] if i < len(lines) else ''} for i in range(len(labels))]}
            
            # Save the structured data to a JSON file
            with open('static/extracted_data.json', 'w') as f:
                json.dump(data, f)
            
            return jsonify({'output': result.stdout}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({'error': f"Script execution failed: {e.stderr}"}), 500
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            app.logger.error(f"Error details: {error_message}\n{traceback.format_exc()}")
            return jsonify({'error': error_message}), 500

@app.route('/document-output', methods=['GET'])
def document_output():
    try:
        with open('static/extracted_data.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'Data file not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/about')
def about():
    return render_template('about.html')

#smtp uses the email and sends an email to itself using the feedback info
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER = 'MetaScanSpprt@gmail.com'
SMTP_APPPASSWORD = 'iynl ferj vies kfjx'
SUPPORT_EMAIL = 'MetaScanSpprt@gmail.com'

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    feedback_type = data.get('type')
    feedback_text = data.get('text')
        
    msg = MIMEMultipart()
    msg['From'] = SMTP_USER
    msg['To'] = SUPPORT_EMAIL
    msg['Subject'] = 'New Feedback Submitted!'

    body = f"Feedback Type: {feedback_type} \n\nFeedback: {feedback_text}"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        #smtp sends email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_APPPASSWORD)
            server.send_message(msg)
        return jsonify({"message": "Feedback submitted successfully!"}), 200
    except smtplib.SMTPException as e:
        app.logger.error(f"SMTP error{str(e)}")
        return jsonify({"error": 'Failed to send feedback due to SMTP error'}), 500
    except Exception as e:
        app.logger.error(f"Failed to send email{str(e)}")
        return jsonify({'error': 'Failed to send feedback'}), 500

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
