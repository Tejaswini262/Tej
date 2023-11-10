import face_recognition
import pickle
import csv

with open("pickle.pkl","rb") as pickle_file:
    ref_face_enc=pickle.load(pickle_file)

roll_list = []
attendance={}

for i in range(220001001,220001083):
    if i==220001030:
        continue
    if i==220001072:
        continue
    roll_list.append(i)
roll_list.append(220002018)
roll_list.append(220002029)
roll_list.append(220002063)
roll_list.append(220002081)

for roll_no in roll_list:
    attendance[str(roll_no)]="Absent"

img = face_recognition.load_image_file("CS 203 Attendance/attendance.jpg")
class_face_enc= face_recognition.face_encodings(img)

print(f"Found {len(class_face_enc)} faces in the image")

for enc in class_face_enc:
    dist=[]
    for rollno in roll_list:
        dist.append(face_recognition.face_distance([enc],ref_face_enc[str(rollno)][0]))
    min_dist=min(dist)
    for rollno in roll_list:
        if face_recognition.face_distance([enc],ref_face_enc[str(rollno)][0])==min_dist:
            attendance[str(rollno)]="Present"
            break

csv_file_name = "location.csv"

# Create and open the CSV file in write mode
with open(csv_file_name, mode='w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the header (field names)
    csv_writer.writerow(["Roll No", "Attendance"])

    # Write the data from the attendance dictionary to the CSV file
    for student, is_present in attendance.items():
        csv_writer.writerow([student, is_present])