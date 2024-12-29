import csv

def CSV_READER():
    try:
        with open('info.csv', 'r') as csv_file:
            csvr = csv.reader(csv_file)
            for line in csvr:
                print(line)
    except FileNotFoundError:
        print("The file 'info.csv' does not exist. Please create or save data to it first.")

command = input("Do you want to read the CSV file? (yes/Y): ").strip().lower()
if command in ["yes", "y"]:
    CSV_READER()
else:
    print("Exiting without reading the CSV file.")
    
