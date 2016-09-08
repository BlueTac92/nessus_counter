import csv

#inputPath = input("Please enter to path to the directory containing your nessus reports: ")
#outputPath = inputPath + "/output"


#print ("------------------------------------")
#print ("is the default output path okay?...")
#print ("Default Output Path: %s" % outputPath)
#

with open('./test_data/scan_data.csv', newline='') as csvfile:
    vulns = csv.DictReader(csvfile)
    for row in vulns:
        print(row['hostname'], row['id'])
        
