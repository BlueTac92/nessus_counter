import os

reports = os.listdir("./")

for roots, dirs, files in os.walk(reports):
    for file in files:
        print(roots + files)

