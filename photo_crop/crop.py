import cv2

# open the image
image = cv2.imread('ub04_form.jpeg')

#resize image
new_width = 770
new_height = 1024
image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Define the cropping region
# Format: (startY:endY, startX:endX)
# Example values: x, y (top-left corner), w (width), h (height)

# Patient Info 1(field 1)
x, y, w, h = 12, 17, 240, 80  
patient_info1 = image[y:h, x:w]

# Patient Info 2(field 2)
x, y, w, h = 240, 17, 465, 80  
patient_info2 = image[y:h, x:w]

# Patient CNTL num (field 3a)
x, y, w, h = 493, 17, 709, 32  
CNTL_num = image[y:h, x:w]

# Med Rec Num (field 3b)
x, y, w, h = 493, 30, 711, 47  
med_rec_num = image[y:h, x:w]

# type of bill (field 4)
x, y, w, h = 711, 32, 755, 47  
patient_info = image[y:h, x:w]

# Fed tax NO (field 5)
x, y, w, h = 466, 62, 560, 80  
fed_tax_num = image[y:h, x:w]

# Statement Period (field 6)
x, y, w, h = 560, 64, 683, 77  
statement_period = image[y:h, x:w]

# Patient Name (field 8)
x, y, w, h = 13, 79, 285, 108  
patient_name = image[y:h, x:w]

# Patient Address (field 9)
x, y, w, h = 285, 76, 759, 108  
patient_address = image[y:h, x:w]

# Patient birthdate (field 10)
x, y, w, h = 12, 125, 95, 140  
patient_birthdate = image[y:h, x:w]

# Patient sex (field 11)
x, y, w, h = 95, 125, 122, 140  
patient_sex = image[y:h, x:w]

# Patient Admission (field 12, 13, 14, 15)
x, y, w, h = 122, 125, 258, 139  
patient_admission = image[y:h, x:w]

# Patient DHR (field 16)
x, y, w, h = 258, 125, 285, 139  
patient_dhr = image[y:h, x:w]

# Patient Stat (field 17)
x, y, w, h = 286, 125, 311, 139  
patient_stat = image[y:h, x:w]

# Condition Codes (fields 18-28)
x, y, w, h = 313, 125, 611, 139  
condition_codes = image[y:h, x:w]

# Patient Accident state (fields 29)
x, y, w, h = 612, 125, 640, 139  
Patient_accident_state = image[y:h, x:w]

# Patient Occurence (code + date) (fields 31-34)
x, y, w, h = 14, 156, 375, 186  
occurance = image[y:h, x:w]

# Patient occurance Span (code, from, through) (fields 35,36)
x, y, w, h = 376, 156, 683, 186  
occurance_span = image[y:h, x:w]

# Patient value codes (code, amount) (39-41)
x, y, w, h = 404, 204, 757, 263  
value_codes = image[y:h, x:w]

# Patient Services (rev co, desc, HCPCS/RATE, serv date, serv units, total charges, non covered charges) (fields 42-48)
x, y, w, h = 14, 281, 733, 619  
patient_services = image[y:h, x:w]

# Patient Services Info ( creation date, totals)
x, y, w, h = 414, 619, 733, 637 
patient_info = image[y:h, x:w]

# Patient Payer Name (field 50)
x, y, w, h = 12, 652, 220, 700  
payer_name = image[y:h, x:w]

# Patient Health Plan ID (field 51)
x, y, w, h = 221, 651, 357, 700  
patient_info = image[y:h, x:w]

# Patient Health Plan ID rel_info (field 52)
x, y, w, h = 357, 651, 376, 700  
rel_info = image[y:h, x:w]

# Patient Asg. Ben. (field 53)
x, y, w, h = 386, 651, 403, 700  
asg_ben = image[y:h, x:w]

# Patient prior payments (field 54)
x, y, w, h = 403, 651, 493, 700  
prior_payment = image[y:h, x:w]

# Patient est amt due (field 55)
x, y, w, h = 493, 651, 592, 700  
est_amt_due = image[y:h, x:w]

# NPI (field 56)
x, y, w, h = 619, 637, 755, 654  
npi = image[y:h, x:w]

# other pvd id (field 57)
x, y, w, h = 619, 651, 755, 700  
other_pvd_id = image[y:h, x:w]

# insured names (field 58)
x, y, w, h = 14, 713, 250, 760  
insured_names = image[y:h, x:w]

# p rel (field 59)
x, y, w, h = 250, 713, 277, 760  
p_rel = image[y:h, x:w]

# insured unique id (field 60)
x, y, w, h = 277, 713, 454, 760  
npi = image[y:h, x:w]

# group name (field 61)
x, y, w, h = 454, 713, 593, 760  
group_name = image[y:h, x:w]

# Insurance group num (field 62)
x, y, w, h = 593, 713, 755, 760  
insurance_num = image[y:h, x:w]

# Treatment authorization codes (field 63)
x, y, w, h = 14, 776, 293, 822  
treatment_auth_codes = image[y:h, x:w]

# document control number (field 64)
x, y, w, h = 293, 776, 530, 822  
control_num = image[y:h, x:w]

# employer name (field 65)
x, y, w, h = 530, 776, 755, 822  
employer_name = image[y:h, x:w]

# DX (field 66,67)
x, y, w, h = 14, 822, 676, 854  
dx = image[y:h, x:w]

# admit DX (field 69)
x, y, w, h = 49, 855, 115, 870  
admit_dx = image[y:h, x:w]

# patient reason DX (field 70)
x, y, w, h = 161, 854, 350, 870  
reason_dx = image[y:h, x:w]

# pps code (field 71)
x, y, w, h = 387, 854, 430, 870  
pps_code = image[y:h, x:w]

# ECI (field 72)
x, y, w, h = 450, 854, 666, 870  
eci = image[y:h, x:w]

# principal procedue (code, date) (field 74)
x, y, w, h = 14, 885, 420, 930  
principle_procedure = image[y:h, x:w]

# attending info (NPI, qual, name) (field 76)
x, y, w, h = 467, 870, 755, 900  
attending_info = image[y:h, x:w]

# operating info (NPI, qual, name) (field 77) 
x, y, w, h = 467, 900, 755, 930  
operating_info = image[y:h, x:w]

# other staff info (NPI, qual, name) (field 78)
x, y, w, h = 467, 930, 755, 960  
other_info1 = image[y:h, x:w]

# other staff info (NPI, qual, name) (field 79)
x, y, w, h = 467, 960, 755, 990  
other_info2 = image[y:h, x:w]

# Remarks (field 80)
x, y, w, h = 14, 950, 228, 992  
remarks = image[y:h, x:w]

# CC Info (field 81)
x, y, w, h = 250, 931, 465, 994  
cc_info = image[y:h, x:w]

# Optional: Display the cropped image
# cv2.imshow('Cropped Image', cc_info)
# cv2.waitKey(0)  # Wait for a key press to close the image window
# cv2.destroyAllWindows()
