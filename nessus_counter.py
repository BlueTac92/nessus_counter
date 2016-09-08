import csv


print('----------------------------------')
print('     Nessus counting tool')
print('')
print('     GPU 2016')
print('')
print('')
print('     by John Brown')
print('----------------------------------')

#inputPath = input("Please enter to path to the directory containing your nessus reports: ")
#outputPath = inputPath + "/output"


#print ("------------------------------------")
#print ("is the default output path okay?...")
#print ("Default Output Path: %s" % outputPath)
#

nessus_report = "./test_data/scan_data.csv"

critical = 0
high = 0
medium = 0
low = 0


with open(nessus_report, newline='') as csvfile:
    vulns = csv.DictReader(csvfile)
    for row in vulns:
        if row['severity'] == "critical":
            critical = critical + 1
        if row['severity'] == "high":
            high = high + 1
        if row['severity'] == "medium":
            medium = medium + 1
        if row['severity'] == "low":
            low = low + 1
       
print ('Total vulnerablilities')
print ('----------------------------------')
print ('Critical:   %i' % critical)
print ('High:       %i' % high)
print ('Meidum:     %i' % medium)
print ('Low:        %i' % low)



       # print(row['hostname'], row['id'])
