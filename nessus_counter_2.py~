# add to dictionary of vulns, unless already exists, then increment count by 1

import csv
import os

currentDir = os.path.dirname(os.path.realpath(__file__))
reportDirectory = currentDir + "/reports/"
reports = []

for x in os.listdir(reportDirectory):
    reports.append(reportDirectory + '/' + x)

uniqueVulns = []
vulns = {}

def main(report):

    with open(report, newline='') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            if row['Name'] not in vulns.keys():
                vulns.update({row['Name']:{'name': row['Name'],'risk': row['Risk'], 'count': 1}})
            if row['Name'] in vulns.keys():
                vulns[row['Name']]['count'] +=1

for x in reports:
    main(x)
    print('Processing ' + x)
    for vuln in vulns:
        print(vuln + ',' + vulns[vuln]['risk'] + ',' + str(vulns[vuln]['count']))


