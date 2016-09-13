import csv


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

nessus_report = "Monthly_Scheduled_Site_1_BE_Scan_idi7p6.csv"

# not exactly the right idea for lists, but consider converting to a list value
sev = ['critical', 'high', 'medium', 'low']

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

# Get a total count of each criticality
# if are repeated a lot, get rid of this shit
#
with open(nessus_report, newline='') as csvfile:
    report = csv.DictReader(csvfile)
    for row in report:
        if row['Risk'] == "Critical":
            critical = critical + 1
        if row['Risk'] == "High":
            high = high + 1
        if row['Risk'] == "Medium":
            medium = medium + 1
        if row['Risk'] == "Low":
            low = low + 1
        if row['Risk'] == "None":
            low = low + 1

print ('Total vulnerablilities')
print ('----------------------------------')
print ('Critical:   %i' % critical)
print ('High:       %i' % high)
print ('Medium:     %i' % medium)
print ('Low:        %i' % low)
print ('None:       %i' % none)

# Count total number of unique vulnerablilities

with open(nessus_report, newline='') as csvfile:
    report = csv.DictReader(csvfile)
    for row in report:
        if row['Name'] not in uniqueVulns:
            uniqueVulns.append(row['Name'])
print ('----------------------------------')
print('Total number of uniq vulnerablilities: ' + str(len(uniqueVulns)))
print ('----------------------------------')







       # print(row['hostname'], row['id'])
