#!/usr/bin/python
import json
import collections
import csv



print ("Provide the absolute path of Input file name:")
input_filename  = input( "> " )

print ("Provide the absolute path of Ouput file name:")
output_filename  = input( "> " )

input_data_file_name_and_path = input_filename
output_data_file_name_and_path=output_filename

#input_data_file_name_and_path = 'C:\\Users\\xxxxxxxx\\Desktop\\data.json'
#output_data_file_name_and_path = 'C:\\Users\\xxxxxxxx\\Desktop\\data.csv'

with open(input_data_file_name_and_path) as json_file:
    data = json.load(json_file)

#Below ref_list should be updated with names of fields or columns that you need in your csv output file. Below are the possible example values
ref_list = ['CSV_FieldName1','CSV_FieldName2','Remaining_FieldNames']

csv_data = open(output_data_file_name_and_path, 'w')

str1 = ','.join(str(e) for e in ref_list)
csv_data.write(str1 + '\n')
rec_count=(len(data))
ref_count= len(ref_list)
#print(rec_count)
for i in range (0,rec_count):
    #print(i)
    values=''
    instance_count=0
    values = data[i][0][0] + ','
    for j in range (1,ref_count):
        if (data[i][0][1]) is not None:
            #print(len(data[i][0]),data[i][0][1])
            key_length= len(data[i][0][1])
            for k in range (0,key_length):
           #print(data[i][0][0],data[i][0][1][k])
   #        print(i,k,data[i][0000][1][k]['Key'], data[i][0000][1][k]['Value'])
                if ref_list[j] == data[i][0000][1][k]['Key'] :
   #                #print(data[i][0][1][k]['Key'],' ', data[i][0][1][k]['Value'])
                   values = values + data[i][0000][1][k]['Value'] + ','
    csv_data.write(values[:-1] + '\n')



json_file.close()
csv_data.close()
