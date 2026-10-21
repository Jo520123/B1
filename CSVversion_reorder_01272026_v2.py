import csv
import pandas as pd

from pathlib import Path

import re
import time
import warnings
import os


start_time = time.time()

#file_path_1 = 'CR_Students_2222.csv'
#file_path_1 = 'CR_Students_02022026.csv'
#file_path_1 = 'CR_Students_2.csv'
#file_path_1 = 'CR_Students_2_05052026_2.csv'
file_path_1 = '/home/vagrant/Report/CR_Students_2_dummydata.csv'


csv_path = "/var/data/analytics/sales_records.csv"
#file_path_2 = 'CR_Academic_Period_Records_2222.csv'
#file_path_2 = 'CR_Academic_Period_Records_02022026.csv'
#file_path_2 = 'CR_Academic_Period_Records_2.csv'
#file_path_2 = 'CR_Academic_Period_Records_2_05052026_2.csv'
file_path_2 = '/home/vagrant/Report/CR_Academic_Period_Records_2_dummydata.csv'

#file_path_2 = 'CR_33333.csv'
#file_path_3 = 'CR_INT1003A02_Financial_Aid_Period_2222.csv'
#file_path_3 = 'CR_INT1003A02_Financial_Aid_Period_Records_02022026.csv'
#file_path_3 = 'CR_Financial_Aid_Period_Records_2.csv'
#file_path_3 = 'CR_Financial_Aid_Period_Records_2_05052026_2.csv'
file_path_3 = '/home/vagrant/Report/CR_Financial_Aid_Period_Records_2_dummydata.csv'

#file_path_4 = 'CR_Financial_Aid_Records_2222.csv'
#file_path_4 = 'CR_Financial_Aid_Records_02022026.csv'
#file_path_4 = 'CR_Academic_Record_2.csv'
#file_path_4 = 'CR_Academic_Record_2_05052026_2.csv'
file_path_4 = '/home/vagrant/Report/ CR_Academic_Record_2_dummydata.csv'


output_dir = Path("/home/vagrant/OutPutFile")
output_dir.mkdir(parents=True, exist_ok=True)



output_file = 'Reorder_Swap_output_v1{}.csv'
join_column = "student_id"

try:

    #dest = r'.'


    """
    for path1 in Path(dest).rglob('CR_Students_2.csv'):
    #for path1 in Path(dest).rglob('CR_INT1003A02_Student_*.xlsx'):
        if path1.is_file():
            print(path1)

    for path2 in Path(dest).rglob('CR_Academic_Period_Records_2.csv'):
        if path2.is_file():
            print(path2)

    for path3 in Path(dest).rglob('CR_INT1003A02_Financial_Aid_Period_Records_22.csv'):
        if path3.is_file():
            print(path3)

    for path4 in Path(dest).rglob('CR_Financial_Aid_Records_2.csv'):
        if path4.is_file():
            print(path4)
            """

    #warnings.simplefilter("ignore")

    #df1 = pd.read_excel(path1)
    #print(df1)


    #df1 = pd.read_csv('CR_Students_2.csv', na_values=["N/A", "Unknown"])

    print(f"Reading {file_path_1}...")
    df1 = pd.read_csv(file_path_1, na_values=["N/A", "Unknown"])

    print("############################# df1 #############################")
    print("df1 Data loaded into DataFrame successfully.")
    print(df1)

    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    #df2 = pd.read_csv('CR_Academic_Period_Records_2.csv')

    print(f"Reading {file_path_2}...")
    df2 = pd.read_csv(file_path_2, na_values=["N/A", "Unknown"])
    print("############################# df2 #############################")
    print("df2 Data loaded into DataFrame successfully.")
    print(df2)

    print(f"Reading {file_path_3}...")
    df3 = pd.read_csv(file_path_3, na_values=["N/A", "Unknown"])
    print("############################# df3 #############################")
    print("df3 Data loaded into DataFrame successfully.")
    print(df3)

    print(f"Reading {file_path_4}...")
    df4 = pd.read_csv(file_path_4, na_values=["N/A", "Unknown"])
    print("############################# df4 #############################")
    print("df4 Data loaded into DataFrame successfully.")


    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")

    print(f"Reading {file_path_3} Research")
    #print(df3)

    #for x in df3:

        #print(x)
    #df33 = df3
    #print(df33.head())

    #for x in df33.head():
        #print(x)
    #print(df33['nm_resident'])

    #hoo = df33[df33['nm_resident'] == '/']

    #print(hoo)


    #print('try')

    #print(df33['nm_resident'].head(10))

    #print(f"before-------------")
    #print(df33)

    df3['nm_resident'] = df3['nm_resident'].replace('/', '')
    df3['nm_resident'] = df3['nm_resident'].replace('NONRESIDENT/', 'NONRESIDENT')

    #print(f"After-------------")
    #print(df33)

    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")


    Result1 = df1.merge(df2, how="left", on=join_column)

    print('Result1 [CR_Students_2.csv, CR_Academic_Period_Records_2.csv]')
    print(Result1)

    print("kkkkkkkkkkkkkk")

    for x in Result1:
        print(x)

    Result2 = Result1.merge(df3, how="left", on=join_column)

    print('Result2 [CR_Students_2.csv, CR_Academic_Period_Records_2.csv, CR_Financial_Aid_Period_Records_2.csv]')
    print(Result2)

    Result3 = Result2.merge(df4, how="left", on=join_column)
    print('Result3 [CR_Students_2.csv, CR_Academic_Period_Records_2.csv, CR_Financial_Aid_Period_Records_2.csv, CR_Academic_Record_2.csv]')
    print(Result3)


    """
    #writer1 = pd.ExcelWriter("Join_test_WD_studio_outputFiles{}.csv".format(time.strftime("%Y%m%d_%H%M%S")), engine='xlsxwriter')
    with pd.ExcelWriter("Join_test_WD_studio_outputFiles{}.csv".format(time.strftime("%Y%m%d_%H%M%S"))) as writer:
    ###writer2 = pd.ExcelWriter("Jointest9999.xlsx", engine='xlsxwriter')
    #fields = []
        Result1.to_excel(writer, sheet_name='Sheet1', startrow=1, header=False, index=False)
        """



    """
    filename = "output.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        #csvwriter.writerow()
        csvwriter.writerows(Result1)
        """

    ##df = df[['A', 'B', 'C']]



    #Result3 = Result3['student_id', 'email', 'SSO_username', 'first_name', 'middle_name', 'last_name', 'permanent_address_line1', 'permanent_address_line2', 'permanent_city', 'permanent_state', 'current_phone', 'gender', 'ethnicity', 'new_ethnicity', 'race', 'date_of_birth', 'age', 'veteran', 'foster_care_student', 'program_major', 'degc_code', 'hours_currently_enrolled', 'credit_hours_completed', 'credits_completed_toward_major', 'transfer_credits', 'cumulative_gpa', 'cumulative_completion_rate', 'fafsa', 'default_status', 'efc', 'unmet_need', 'composite_act_score', 'sat_score', 'high_school_grad_date1', 'high_school_grad_date2', 'high_school_grad_date3', 'high_school1', 'high_school2', 'high_school3', 'high_school_state_code1', 'high_school_state_code2', 'high_school_state_code3', 'dplm_code1', 'dplm_code2', 'dplm_code3', 'classification', 'school', 'academic_standing', 'sapr_code', 'degrees_awarded', 'degrees_awarded_XXX', 'date_degrees_awarded_XXX', 'degrees_awarded_External' , 'date_degrees_awarded_External' , 'dependency', 'employee_waiver', 'dependent_waiver', 'nm_resident', 'citizenship', 'dual_credit']
    Result3 = Result3[['student_id', 'email', 'SSO_username', 'first_name', 'middle_name', 'last_name', 'permanent_address_line1', 'permanent_address_line2', 'permanent_city', 'permanent_state', 'current_phone', 'gender', 'ethnicity', 'new_ethnicity', 'race', 'date_of_birth', 'age', 'program_major', 'degc_code', 'hours_currently_enrolled', 'credit_hours_completed', 'credits_completed_toward_major', 'transfer_credits', 'cumulative_gpa', 'efc', 'unmet_need', 'composite_act_score', 'sat_score', 'high_school_grad_date1', 'high_school_grad_date2', 'high_school_grad_date3', 'high_school1', 'high_school2', 'high_school3', 'high_school_state_code1', 'high_school_state_code2', 'high_school_state_code3', 'dplm_code1', 'dplm_code2', 'dplm_code3', 'school', 'academic_standing', 'sapr_code', 'nm_resident', 'citizenship']]

    #CR_Students_2.csv
    #student_id, email SSO_username first_name middle_name last_name permanent_address_line1 permanent_address_line2 permanent_city permanent_state current_phone gender ethnicity new_ethnicity race date_of_birth age program_major composite_act_score sat_score high_school_state_code1 high_school_state_code2 high_school_state_code3 citizenship school

    #CR_Academic_Record_2(2).csv

    #student_id high_school_grad_date1 high_school_grad_date2 high_school_grad_date3

    #CR_Financial_Aid_Period_Records_2(1).csv

    #student_id efc unmet_need nm_resident sapr_code

    #CR_Academic_Period_Records_2(3).csv

    #student_id dplm_code1 dplm_code2 dplm_code3 degc_code high_school1 high_school2 high_school3 academic_standing hours_currently_enrolled credit_hours_completed credits_completed_toward_major transfer_credits cumulative_gpa

    #Result3 = Result3[['student_id','email','first_name','middle_name','last_name','permanent_address_line1','permanent_address_line2','permanent_city','permanent_state','county_of_residence','current_phone','cell_phone','gender','ethnicity','new_ethnicity','race','date_of_birth','age','veteran',	 'foster_care_student','program_major','degc_code','hours_currently_enrolled','credit_hours_completed','credits_completed_toward_major',	 'transfer_credits','cumulative_gpa','cumulative_completion_rate','fafsa','default_status','efc','unmet_need','composite_act_score',	 'sat_score','high_school_grad_date1','high_school_grad_date2','high_school_grad_date3','high_school1','high_school2','high_school3',	 'high_school_state_code1','high_school_state_code2','high_school_state_code3','dplm_code1','dplm_code2','dplm_code3','classification',	 'school','academic_standing','sapr_code','degrees_awarded','date_degrees_awarded','dependency','employee_waiver','dependent_waiver',	 'nm_resident','citizenship','dual_credit','eligible_for_aid']]

    csv_output_path = output_dir / output_file.format(time.strftime("%Y%m%d_%H%M%S"))

    Result3.to_csv(csv_output_path, index=False)


    print("\n Success!")
    print(f"DataFrams joined successfully on the column '{join_column}'.")
    print(f"Combined data saved to: {os.path.abspath(output_file)}")


    # Display the first few rows of the result
    print("\nCombined Data Preview:")
    ####print("Result1.head()",Result1.head())
    print(Result1.head())

    print("1111111111111--Result3.head()--111111111111111111")

    print(Result3.head())

    print("1111111111111--Result3.head()--111111111111111111")

except FileNotFoundError as e:
    print(f"\n Error: One or more input files not found. Check the file paths.")
    print(f"Missing file: {e.filename}")

except Exception as e:
    print(f"\n An unexpected error occurred: {e}")



print("--- %s seconds ---" % (time.time() - start_time))

print(f"File saved in : {os.getcwd()}")


