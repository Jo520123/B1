from pathlib import Path
import pandas as pd


input_dir = Path("C:/Desktop/T2Py")

pd.set_option('display.max_columns', None)

pd.set_option('display.width', 1000)

pd.set_option('display.max_colwidth', None)


csv_files3 = list(input_dir.glob("Int038a*.csv"))
csv_files1 = list(input_dir.glob("Int038b*.csv"))
csv_files2 = list(input_dir.glob("Int038c*.csv"))


if not csv_files1:
    print("No matching Int038b CSV files found.")

else:

    df_list1 = []
    c1 = 0

    for file in csv_files1:
        try:
            temp_df = pd.read_csv(file)


            if not temp_df.empty:
                df_list1.append(temp_df)
                c1 += 1
                #print("c1", c1)

            else:
                print(f"Skipping empty file: {file.name}")


        except pd.errors.EmptyDataError:
            print(f"Skipping truly blank file: {file.name}")


    if df_list1:
        combined_df1 = pd.concat(df_list1, ignore_index=True)

        #combined_df1_order = combined_df1.sort_values(by='File Date', ascending=True)

        #output_path1 = input_dir / "Combined_output_int038b.csv"

        #combined_df1.to_csv(output_path1, index=False)

        #print(f"Successfully combined {len(csv_files1)} files into :{output_path1}")
        print(f"Successfully combined Int038b CSV files {c1}")

    else:
        print("All matched files were empty. No combined file created.")


if not csv_files2:
    print("No matching Int038c CSV files found.")

else:
    df_list2 = []
    c2 = 0

    for file in csv_files2:

        try:
            temp_df = pd.read_csv(file)

            if not temp_df.empty:
                df_list2.append(temp_df)
                c2 += 1

            else:
                print(f"Skipping empty file: {file.name}")


        except pd.errors.EmptyDataError:
            print(f"Skipping truly blank file: {file.name}")


    if df_list2:
        combined_df2 = pd.concat(df_list2, ignore_index=True)

        #combined_df2_order = combined_df2.sort_values(by='File Date', ascending=True)

        #print("66666666666666666666")
        #print("------------combined_df2", combined_df2_order)

        #output_path2 = input_dir / "Combined_output_int038c.csv"

        #combined_df2.to_csv(output_path2, index=False)

        #print(f"Successfully combined {len(csv_files2)} files into : {output_path2}")

        print(f"Successfully combined Int038c CSV files {c2}")

    else:

        print("All matched files were empty. No combined file created.")



    #df_list = [pd.read_csv(file) for file in csv_files]

    #combined_df = pd.concat(df_list, ignore_index=True)

    #output_path = input_dir / "Combined_output_int038b.csv"



    #print(f"Successfully combined {len(csv_files)} files into : {output_path}")


#Int038b_Output20260820_151223_9.csv



if not csv_files3:
    print("No matching Int038a CSV file found.")

else:

    df_list3 = []
    c3 = 0

    for file in csv_files3:
        try:
            temp_df = pd.read_csv(file)

            if not temp_df.empty:

                temp_df = temp_df[['Integration', 'Primary_ID', 'Secondary_ID','First_Name',
                         'Middle_Name', 'Last_Name', 'Subclassification','Email_Address','File Date']]

                df_list3.append(temp_df)
                c3 += 1

            else:
                print(f"Skipping empty file: {file.name}")

        except pd.errors.EmptyDataError:
            print(f"Skipping truly blank file: {file.name}")


    if df_list3:

        combined_df3 = pd.concat(df_list3, ignore_index=True)
        ##print("66666666666666666666")
        ##print("------------combined_df3", combined_df3)

        #combined_df3_order = combined_df3.sort_values(by='File Date', ascending=True)


        # output_path3 = input_dir / "Combined_output_int038a.csv"

        # output_path3 = input_dir / "Combined_output_int038a.csv"

        # output_path3 = input_dir / "Combined_output_int038a.csv"


        print(f"Successfully combined Int038a CSV files {c3}")


    else:
        print("All matched files were empty. No combined file created.")


#print("--------------------------------------Start----------------------------------------")
print("--------------------------------------Int038a--------------------------------------")

#100001321
#100100421

#filtered_int038a = combined_df3.query('Secondary_ID == 100100421').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100001321').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100001963').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100001360').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100103562').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100103944').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100001816').copy()

#filtered_int038a = combined_df3.query('Secondary_ID == 100001360').copy()
#003119

filtered_int038a = combined_df3.query('Secondary_ID == 100001816').copy()
#filtered_int038a = combined_df3.query('Secondary_ID == 100003119').copy()

filtered_int038a['File Date'] = pd.to_datetime(filtered_int038a['File Date'].str.strip())

filtered_int038a_order = filtered_int038a.sort_values(by='File Date', ascending=True)

filtered_int038a_order['File Date'] = filtered_int038a_order['File Date'].dt.strftime('%m/%d/%Y')

print(filtered_int038a_order)



#print("--------------------------------------Start----------------------------------------")
print("--------------------------------------Int038b--------------------------------------")
#print(combined_df1)


#print(combined_df1['SECONDARY_ID'] == 1321)

#print(combined_df1)

#filtered_int038b = combined_df1.query('SECONDARY_ID == 100421').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 1321').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 1963').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 1360').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 103562').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 103944').copy()

filtered_int038b = combined_df1.query('SECONDARY_ID == 1816').copy()

#filtered_int038b = combined_df1.query('SECONDARY_ID == 3119').copy()
##100003119

####filtered_int038b = combined_df1.query('PAYMENT_PLAN_UID == 9115').copy()

####filtered_int038b = combined_df1.query('FULL_AMOUNT_DUE == 7.50' and 'SECONDARY_ID == 104355').copy()

##filtered_int038b = combined_df1.query('FULL_AMOUNT_DUE == 7.50').copy()

filtered_int038b['File Date'] = pd.to_datetime(filtered_int038b['File Date'].str.strip())

filtered_int038b_order = filtered_int038b.sort_values(by='File Date', ascending = True)

filtered_int038b_order['File Date'] = filtered_int038b_order['File Date'].dt.strftime('%m/%d/%Y')

print(filtered_int038b_order)

##print(filtered_int038b)





#print("--------------------------------------Start----------------------------------------")
print("--------------------------------------Int038c--------------------------------------")

#print(combined_df2)

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100001321').copy()

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100001963').copy()

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100001360').copy()

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100103562').copy()

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100103944').copy()

filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100001816').copy()
#3119

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 3119').copy()

####filtered_int038c = combined_df2.query('PAYMENT_PLAN_ID == 9115').copy()

##filtered_int038c = combined_df2.query('PAYMENT_AMOUNT == 7.89 ').copy()

#filtered_int038c = combined_df2.query('ENTITY_PRIMARY_ID == 100100421').copy()

filtered_int038c['File Date'] = pd.to_datetime(filtered_int038c['File Date'].str.strip())

filtered_int038c_order = filtered_int038c.sort_values(by='File Date', ascending=True)

filtered_int038c_order['File Date'] = filtered_int038c_order['File Date'].dt.strftime('%m/%d/%Y')

print(filtered_int038c_order)

##print(filtered_int038c)

print("************ End *************")

#print("*********** try *************")

#df_list3 = [filtered_int038a, filtered_int038b, filtered_int038c]

#print(df_list3)

#com_df_list3 = pd.concat(df_list3)
#with open('Output_CombineQuery_Result444.csv', 'w') as f:

"""

filtered_int038a_order.to_csv('Output_CombineQuery_Result.csv', index=False)

  
filtered_int038b_order.to_csv('Output_CombineQuery_Result.csv', mode='a',index=False, header=True)


filtered_int038c_order.to_csv('Output_CombineQuery_Result.csv', mode='a', index=False, header=True)

print("Successfully combined")


"""


