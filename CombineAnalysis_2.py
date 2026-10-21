import time
from datetime import datetime
from pathlib import Path
import pandas as pd

import os

import glob
from pathlib import Path

#output_file ='Combine_output{}.csv'
output_file1 ='Int038b_Output{}.csv'
output_file2 ='Int038c_Output{}.csv'


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

    print("5555555555555555555")

    #print("5555555555555555555555555555")
    count1 = 0
    count2 = 0

    for x in dir_path:

        if "bnrpayment" in str(x):
            count1 += 1

            print(f"\n Number {count1} csv file")

        elif "payrollexport" in str(x):
            count2 += 1

            print(f"\n Number {count2} csv file")

        else:
            continue


        print(x)

        #print("5555555555555555555555555555")

        file_path = f"{x}"

        #print(x)
        #print(file_path)

        print(f"Reading {file_path}")

        filename = os.path.basename(file_path)

        parts = filename.split('_')

        int_part = parts[1]
        date_part = parts[2].split('.')[0]
        date_part_formatpatt = datetime.strptime(date_part, '%m%d%Y')
        dateFormat = f"{date_part_formatpatt.month}/{date_part_formatpatt.day}/{date_part_formatpatt.year}"


    #filtered = df1.query('ENTITY_PRIMARY_ID == 100104355')

    #print(filtered)

    #print(df1['ENTITY_PRIMARY_ID'] == 100104355)

    #print(df1[0])

        if "bnrpayment" in str(x):
            print("\n The path contains 'bnrpayment'")

            df = pd.read_csv(x, na_values=["N/A", "Unknown"])

            print("99999999999999999999999999999999999999999")

            df['Integration'] = int_part
            df['File Date'] = dateFormat

            df = df[['Integration', 'ENTITY_PRIMARY_ID', 'PAYMENT_PLAN_ID', 'PAYMENT_AMOUNT','File Date']]

            #output_dir = Path("Output")
            #output_dir.mkdir(parents=True, exist_ok=True)

            #file_pathpath = output_dir / output_file2

            df.to_csv(output_file2.format(time.strftime("%Y%m%d_%H%M%S")), index=False)

            #print(f"File {output_file2} saved successfully to {output_dir}")




        elif "payrollexport" in str(x):
            print("\n The path contains 'payrollexport'")

            df = pd.read_csv(x, na_values=["N/A", "Unknown"])

            print("888888888888888888888888888")

            df["Integration"] = int_part
            df['File Date'] = dateFormat

            df = df[['Integration','SECONDARY_ID','FIRST_NAME','MIDDLE_NAME','LAST_NAME','FULL_AMOUNT_DUE','PAYMENT_PLAN_UID','DEDUCTION_CODE','DEDUCTION_DESCRIPTION','STOP_PAYMENT','File Date']]

            #output_dir = Path("Output")
            #output_dir.mkdir(parents=True, exist_ok=True)

            #file_path = output_dir / output_file1

            df.to_csv(output_file1.format(time.strftime("%Y%m%d_%H%M%S")), index=False)

            #print(f"File {output_file1} saved successfully to {output_dir}")


    #df = df[['Integration', 'ENTITY_PRIMARY_ID', 'PAYMENT_PLAN_ID', 'PAYMENT_AMOUNT','File Date']]

    #df1.to_csv(output_file.format(time.strftime("%Y%m%d_%H%M%S")), index=False)

    #filtered = df.query('ENTITY_PRIMARY_ID == 100104355')

    #print(filtered)



except FileNotFoundError as e:
    print(f"\n.Error: One or more input files not found. Check the file paths.")
    print(f"Missing file: {e.filename}")


except Exception as e:
    print(f"\n An unexpected error occurred: {e}")



