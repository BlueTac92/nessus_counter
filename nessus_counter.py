import csv
import os
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

reportDirectory = "./reports/"
reports = os.listdir(reportDirectory)
def main(report):

    # not exactly the right idea for lists, but consider converting to a list value
    sev = ['None', 'Low', 'Medium', 'High', 'Critical']

    totalVulns = []
    totalRisks = []
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
    
    with open("./reports/moooar_data.csv", newline='') as csvfile:
        report = csv.DictReader(csvfile)
        for row in report:
            totalVulns.append(row['Name'])
    
    with open("./reports/moooar_data.csv", newline='') as csvfile:
        report = csv.DictReader(csvfile)
        for row in report:
            totalRisks.append(row['Risk'])
    
    print('Total Vulnerablilities: ' + str(len(totalVulns)))
    print('----------------------------------')
    print('Uniq Vulnerabilities: ' + str(len(set(totalVulns))))
    print('----------------------------------')
    
    
    
    #print(uniqueVulns)
    # Count occurances of each vuln
    
    countVulns = Counter(totalVulns)
    countRisks = Counter(totalRisks)
    #print(count)
    
    #print(countedRisks)
    print('Occurances of each Criticality: ')
    print('----------------------------------')
    
    for x in set(totalRisks):
        print(x + ': ' + str(countRisks[x]))
    print('----------------------------------')
    print('Occurances of each Vulnerability: ')
    print('----------------------------------')
    for x in set(totalVulns):
        print(x + ': ' + str(countVulns[x]))
    print('----------------------------------')
    
    
for x in reports:
    main(x)






