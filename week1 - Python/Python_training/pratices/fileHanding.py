
"""txt_data="I like pizza!"

file_path="C:/Users/shaik/OneDrive/Desktop/output.txt"
#w for write
with open(file_path, "a") as f:
    f.write("\n"+txt_data)
    print(f'txt file {file_path} written')"""
import csv
import json

"""employees=["asif","shaik","mohammad","bob"]
file_path="C:/Users/shaik/OneDrive/Desktop/output.txt"
with open(file_path, "w") as f:
    for employee in employees:
        f.write(employee + "\n")
    print(f'txt file {file_path} written')"""
"""email={
    "name":"shaik",
    "email":"shaik@shaik",
    "job":"IT"
}
file_path="output1.json"
with open(file_path, "w") as f:
    json.dump(email, f,indent=4)
    print(f'json file {file_path} written')"""

employees=[["Name","Age","Job"],
           ["ASIF",22,"it"],
           ["SHAIK",25,"HR"],
           ["MOHAMMAD",21,"MRK"]]
path_file="output2.csv"
with open(path_file,"w",newline="") as f:
    writer = csv.writer(f)
    for row in employees:
        writer.writerow(row)
    print(f"csv file {path_file} written")
