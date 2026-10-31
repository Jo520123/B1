import csv

import pandas as pd

from pathlib import Path

import re
import time
import warnings
import os


start_time = time.time()

pd.set_option('display.max_columns', None)

pd.set_option('display.width', None)

pd.set_option('display.max_colwidth', None)


file_path_1 = r"C:/xxx/xxx/Py/CSV/Students.csv"
file_path_2 = r"C:/xxx/xxx/Py/CSV/Academic_Record.csv"
file_path_3 = r"C:/xxx/xxx/Py/CSV/Academic_Period_Records.csv"
file_path_4 = r"C:/xxx/xxx/Py/CSV/Financial_Aid_Period_Records.csv"
file_path_5 = r"C:/xxx/xxx/Py/CSV/Student External Transcripts.csv"


output_dir = Path("C:/xxx/xxx/Py")

output_dir_backup = Path("C:/xxx/xxx/Py/CSV")

output_file = 'ABC_xxx_{}.csv'

join_column = "student_id"


try:

    print()

    print(f"Reading {file_path_1}...")
    df1 = pd.read_csv(file_path_1, na_values=["N/A", "Unknown"])

    print(" Students.csv Data loaded into DataFrame successfully.\n")


    print(f"Reading {file_path_2}...")
    df2 = pd.read_csv(file_path_2, na_values=["N/A", "Unknown"])

    print(" Academic_Record.csv Data loaded into DataFrame successfully.\n")


    print(f"Reading {file_path_3}...")
    df3 = pd.read_csv(file_path_3, na_values=["N/A", "Unknown"])

    print(" Academic_Period_Records.csv Data loaded into DataFrame successfully.\n")


    print(f"Reading {file_path_4}...")
    df4 = pd.read_csv(file_path_4, na_values=["N/A", "Unknown"])

    print(" Financial_Aid_Period_Records.csv Data loaded into DataFrame successfully.\n")


    print(f"Reading {file_path_5}...")
    df5 = pd.read_csv(file_path_5, na_values=["N/A", "Unknown"])

    print(" Student External Transcripts.csv Data loaded into DataFrame successfully.\n")



    df4['nm_resident'] = df4['nm_resident'].replace('/','')
    df4['nm_resident'] = df4['nm_resident'].replace('NONRESIDENT/', 'NONRESIDENT')

    Result1 = df1.merge(df2, how= "left", on=join_column)

    Result2 = Result1.merge(df3, how="left", on=join_column)

    Result3 = Result2.merge(df4, how="left", on=join_column)

    Result4 = Result3.merge(df5, how="left", on=join_column)


    Result4 = Result4[
        ['student_id', 'email', 'SSO_username', 'first_name', 'middle_name', 'last_name', 'permanent_address_line1',
         'permanent_address_line2', 'permanent_city', 'permanent_state', 'current_phone', 'gender', 'ethnicity',
         'new_ethnicity', 'race', 'date_of_birth', 'age', 'veteran', 'foster_care_student', 'program_major',
         'degc_code', 'hours_currently_enrolled',
         'credit_hours_completed', 'credits_completed_toward_major', 'transfer_credits', 'cumulative_gpa',
         'cumulative_completion_rate', 'fafsa', 'default_status', 'efc',
         'unmet_need', 'composite_act_score', 'sat_score', 'high_school_grad_date1', 'high_school_grad_date2',
         'high_school_grad_date3', 'high_school1', 'high_school2', 'high_school3', 'high_school_state_code1',
         'high_school_state_code2', 'high_school_state_code3', 'dplm_code1', 'dplm_code2', 'dplm_code3',
         'classification', 'school',
         'academic_standing', 'sapr_code', 'degrees_awarded_ABC', 'date_degrees_awarded_ABC',
         'degrees_awarded_External', 'date_degrees_awarded_External', 'employee_waiver', 'dependent_waiver',
         'nm_resident', 'citizenship', 'dual_credit']]

    print(Result4.head())

    csv_output_path = output_dir / output_file.format(time.strftime("%Y%m%d_%H%M%S"))

    Result4.to_csv(csv_output_path, index=False)

    print("\n Success!")
    print(f"DataFram joined Successfully on the column '{join_column}'.")
    print(f"Combined data save to:{os.path.abspath(csv_output_path)}\n")


    output_file1_timestamp = 'Students_{}.csv'
    output_file2_timestamp = 'Academic_Record_{}.csv'
    output_file3_timestamp = 'Academic_Period_Records_{}.csv'
    output_file4_timestamp = 'Financial_Aid_Period_Records_{}.csv'
    output_file5_timestamp = 'Student External Transcripts_{}.csv'


    csv_output_path_backup1 = output_dir_backup / output_file1_timestamp.format(time.strftime('%Y%m%d_%H%M%S'))

    df1.to_csv(csv_output_path_backup1, index=False)

    csv_output_path_backup2 = output_dir_backup / output_file2_timestamp.format(time.strftime('%Y%m%d_%H%M%S'))

    df2.to_csv(csv_output_path_backup2, index=False)

    csv_output_path_backup3 = output_dir_backup / output_file3_timestamp.format(time.strftime('%Y%m%d_%H%M%S'))

    df3.to_csv(csv_output_path_backup3, index=False)

    csv_output_path_backup4 = output_dir_backup / output_file4_timestamp.format(time.strftime('%Y%m%d_%H%M%S'))

    df4.to_csv(csv_output_path_backup4, index=False)

    csv_output_path_backup5 = output_dir_backup / output_file5_timestamp.format(time.strftime('%Y%m%d_%H%M%S'))

    df5.to_csv(csv_output_path_backup5, index=False)


    file_to_delete = ['C:/xxx/xxx/Py/CSV/Students.csv',
                      'C:/xxx/xxx/Py/CSV/Academic_Record.csv',
                      'C:/xxx/xxx/Py/CSV/Financial_Aid_Period_Records.csv',
                      'C:/xxx/xxx/Py/CSV/Academic_Period_Records.csv',
                      'C:/xxx/xxx/Py/CSV/Student External Transcripts.csv']


    for file_path in file_to_delete:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'Successfully deleted {file_path}\n')


except FileNotFoundError as e:
    print(f"\n Error: One or more input files not found. Check the file paths.")
    print(f"Missing file:{e.filename}")


except Exception as e:
    print(f"\n An excepted error occurred: {e}")


print("--- %s seconds ---" %(time.time()- start_time))

print(f"File saved in : {os.getcwd()}")
