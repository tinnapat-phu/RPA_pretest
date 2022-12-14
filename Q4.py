import pandas
import numpy as np
import json

def first_table():
    global df
    global column_headers
    global dict
    global origin_header
 
    #drop all nan rows
    df = df.dropna()

    origin_header = list(df)

    #remove Unnamed header (if it have)
    if(origin_header[0]=="Unnamed: 0"):
        new_header = df.iloc[0]
        df = df[1:]
        df.columns = new_header



    #get list of header and extracted campaign name
    column_headers = list(df)

    #order header by fixed list
    df = df[['filename', 'effdate','remark']]

    #change time format
    df['effdate'] = pandas.to_datetime(df["effdate"]).dt.strftime('%Y/%m/%d')
    dict = df.to_dict('records')
    # print(dict)

def second_table():
    global second_df
    global interest_list


    #find index of "interate rate"
    index = second_df[origin_header[0]]=="interate rate"

    #drop all nan columns
    second_df = second_df.iloc[np.where(index)[0][0]:len(index)].dropna(axis=1)

    #make a list
    interest_list = second_df.values.tolist()

def json_append():


    json_export[column_headers[0]] = {
            "data": dict,
            "interest": interest_list
    }



    

interest_list = []
origin_header = []
column_headers = []
dict = {}
df = pandas.DataFrame()
second_df = pandas.DataFrame()
json_export = {}

xls = pandas.ExcelFile('Q4_excel.xlsx')

for sheet in xls.sheet_names:
    excel_data_df = pandas.read_excel('Q4_excel.xlsx', sheet_name=sheet)
    df = pandas.DataFrame(excel_data_df)
    second_df = df
    first_table()
    second_table()
    json_append()

with open("result.json", "w") as outfile:
    json.dump(json_export, outfile)

    





########################################

