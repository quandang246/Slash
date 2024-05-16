# csv_handling.py

import slash
import csv
import warnings 
import os

def test_display_csv_data():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "data", "Hoc_sinh.csv")

    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            stt = int(row[0])
            ten = row[1]
            tuoi = int(row[2])
            gioi_tinh = row[3]
            
            if tuoi >= 10:
                print(f"STT: {stt} / ten: {ten} / tuoi: {tuoi} / gioi_tinh: {gioi_tinh}")
            else:
                warnings.warn(f"Warning: Age of student {ten} is less than 10.") 
