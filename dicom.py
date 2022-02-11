import pydicom

img = pydicom.dcmread('CT_1h.dcm')


patient_name = img.PatientName
patient_id = img.PatientID
study_id  = img.StudyID

print(patient_id, study_id, patient_name)

img = pydicom.dcmread('SPECT_1h.dcm')

patient_name = img.PatientName
patient_id = img.PatientID
study_id  = img.StudyID


print(patient_id, study_id, patient_name)