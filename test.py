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

currentDir = os.path.dirname(os.path.realpath(__file__))
reportDirectory = "/reports/"
reports = []

for x in os.listdir(currentDir + reportDirectory):
    reports.append(currentDir + '/' + x) 

def main(report):

    print(report)
    
    
for x in reports:
    main(x)






