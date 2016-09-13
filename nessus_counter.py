import csv
from collections import Counter

print('----------------------------------')
print('     Nessus counting tool')
print('----------------------------------')
print('  -   GPLv3 2016')
print('  -   by John Brown')
print('----------------------------------')

#inputPath = input("Please enter to path to the directory containing your nessus reports: ")
#outputPath = inputPath + "/output"


#print ("------------------------------------")
#print ("is the default output path okay?...")
#print ("Default Output Path: %s" % outputPath)
#

nessus_report = "test_data/scan_data.csv"

# not exactly the right idea for lists, but consider converting to a list value
sev = ['critical', 'high', 'medium', 'low']
 
totalVulns = []
uniqueVulns = []
critHosts = []
highHosts = []
mediumHosts = []
lowHosts = []
noneHosts = []

critical = 0
high = 0
medium = 0
low = 0
none = 0
counter = 0

# Get a total count of each criticality
# if are repeated a lot, get rid of this shit
#
with open(nessus_report, newline='') as csvfile:
    report = csv.DictReader(csvfile)
    for row in report:
        if row['Risk'] == "Critical":
            critical += 1
        if row['Risk'] == "High":
            high += 1
        if row['Risk'] == "Medium":
            medium += 1
        if row['Risk'] == "Low":
            low += 1
        if row['Risk'] == "None":
            low += 1

print ('Vulnerablilities by Criticality: ')
print ('----------------------------------')
print ('Critical:   %i' % critical)
print ('High:       %i' % high)
print ('Medium:     %i' % medium)
print ('Low:        %i' % low)
print ('None:       %i' % none)

with open(nessus_report, newline='') as csvfile:
    report = csv.DictReader(csvfile)
    for row in report:
        totalVulns.append(row['Name'])

print('----------------------------------')
print('Total Vulnerablilities: ' + str(len(totalVulns)))
print('----------------------------------')
print('Uniq Vulnerabilities: ' + str(len(set(totalVulns))))
print('----------------------------------')
print('Occurances of each Vulnerability: ')
print('----------------------------------')

#print(uniqueVulns)
# Count occurances of each vuln

count = Counter(totalVulns)
#print(count)

for x in set(totalVulns):
    print(x + ': ' + str(count[x]))



            
    
   
        # print(row['hostname'], row['id'])
