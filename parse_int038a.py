import time
from datetime import datetime
import pandas as pd
import os
import glob

pd.set_option('display.max_columns', None)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', None)


output_file3 = 'Int038a_Output{}.csv'


try:
    dest = r'.'

    files = os.listdir(dest)

    #print(files)

    print(f"Success! Found {len(files)} files.")

    dir_path = glob.glob(f"{dest}/*.csv")

    csv_count = len(dir_path)

    print(f"Number of CSV files: {csv_count}")


    count3 = 0

    for x in dir_path:

        print(x)

        file_path = f"{x}"

        print(f"Reading {file_path}")

        filename = os.path.basename(file_path)

        parts = filename.split('_')


        int_part = parts[1]
        date_part = parts[2].split('.')[0]
        date_part_formatpatt = datetime.strptime(date_part, '%m%d%Y')
        dateFormat = f"{date_part_formatpatt.month}/{date_part_formatpatt.day}/{date_part_formatpatt.year}"

        if "bnrcust" in str(x):
            count3 += 1

            print(f"\n Number {count3} csv file")

            print("\n The path contains 'bnrcust'")


            df = pd.read_csv(x, na_values=["N/A", "Unknown"])

            print("99999999999999999999999999999999999999999")

            df['Integration'] = int_part

            df['File Date'] = dateFormat


            df = df[['Integration','Primary_ID','Secondary_ID','Tertiary_ID','Customer_Type','First_Name','Middle_Name','Last_Name','Subclassification','Phone_1','Phone_2','Phone_3','Address_Primary_Street','Address_Second_Street','Address_City','Address_State','Address_Postal_Code','Email_Address','Financial_Aid','File Date']]

            print(df)

            df.to_csv(output_file3.format(time.strftime(f"%Y%m%d_%H%M%S_{count3}")), index=False)



except FileNotFoundError as e:
    print(f"\n.Error: One or more input files not found. Check the file paths.")
    print(f"Missing file: {e.filename}")

except Exception as e:
    print(f"\n An unexpected error occurred: {e}")

