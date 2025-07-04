import csv
import os

FILENAME = "demo.csv"

if not os.path.isfile(FILENAME):
     with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No",])