import time
from datetime import datetime
from pathlib import Path
import pandas as pd

import os

import glob

output_file ='Combine_output{}.csv'

"""
file_path_1 ='bnrpayment_int038c_05222026.csv'
filename = os.path.basename(file_path_1)

parts = filename.split('_')

int_part = parts[1]
date_part = parts[2].split('.')[0]
date_part_formatpatt = datetime.strptime(date_part, '%m%d%Y')
dateFormat = f"{date_part_formatpatt.month}/{date_part_formatpatt.day}/{date_part_formatpatt.year}"


print("11111111111111")
print(int_part)
print(date_part)
print(date_part_formatpatt)
print(dateFormat)
print("11111111111111111")
"""



try:

    dest = r'.'

    files = os.listdir(dest)

    print(f"Success! Found {len(files)} files.")

    dir_path = glob.glob(f"{dest}/*.csv")
    csv_count = len(dir_path)

    print(f"Number of CSV files: {csv_count}")

    print("5555555555555555555555555555")
    count = 0

    for x in dir_path:

        count += 1
        print(f"Number{count} csv file")

        print(x)

    print("5555555555555555555555555555")

    file_path_1 = 'bnrpayment_int038c_05222026.csv'
    filename = os.path.basename(file_path_1)

    parts = filename.split('_')

    int_part = parts[1]
    date_part = parts[2].split('.')[0]
    date_part_formatpatt = datetime.strptime(date_part, '%m%d%Y')
    dateFormat = f"{date_part_formatpatt.month}/{date_part_formatpatt.day}/{date_part_formatpatt.year}"



    print(f"Reading {file_path_1}")

    df1 =pd.read_csv(file_path_1, na_values=["N/A", "Unknown"])

    df1['Integration'] = int_part
    df1['File Date'] = dateFormat

    #filtered = df1.query('ENTITY_PRIMARY_ID == 100104355')

    #print(filtered)

    #print(df1['ENTITY_PRIMARY_ID'] == 100104355)

    #print(df1[0])


    df1 = df1[['Integration', 'ENTITY_PRIMARY_ID', 'PAYMENT_PLAN_ID', 'PAYMENT_AMOUNT','File Date']]

    #df1.to_csv(output_file.format(time.strftime("%Y%m%d_%H%M%S")), index=False)

    filtered = df1.query('ENTITY_PRIMARY_ID == 100104355')

    print(filtered)



except FileNotFoundError as e:
    print(f"\n.Error: One or more input files not found. Check the file paths.")
    print(f"Missing file: {e.filename}")


except Exception as e:
    print(f"\n An unexpected error occurred: {e}")



