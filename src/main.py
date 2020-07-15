from time import sleep
import requests
import os
import pandas as pd

print("Project to export Excel data files.")

url = "https://www.tn.gov/content/dam/tn/health/documents/cedep/novel-coronavirus/datasets/"
    
excellist = [
    "Public-Dataset-Age.XLSX",
    "Public-Dataset-Daily-County-Age-Group.XLSX", 
    "Public-Dataset-County-New.XLSX", 
    "Public-Dataset-Daily-Case-Info.XLSX",
    "Public-Dataset-RaceEthSex.XLSX"
    ]

def process_data(excellist):
    
    for x in excellist:
        print(x)
        read_file = pd.read_excel (r'./data/' + x)
        csv = os.path.splitext(x)[0] + ".csv"
        read_file.to_csv (r'./data/' + csv, index = None, header=True)
        print("Beginning data processing...   " + csv)
    modified_data = " CSV Exported"
    print("Data processing finished.")
    return modified_data

def read_data_from_web():
    print("Reading data from the Web")
    for x in excellist:
        print(x)
        dls = url + x
        resp = requests.get(dls)
        output = open('./data/' + x, 'wb')
        output.write(resp.content)
        output.close()

def main():
    data = read_data_from_web()
    modified_data = process_data(excellist)

if __name__ == "__main__":
    main()