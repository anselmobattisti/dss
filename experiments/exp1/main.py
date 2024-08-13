from src.DSS.helper import helper
from datetime import datetime
import csv

vnfs = []
vnfs.append([])
vnfs.append([])
vnfs.append(["V0", "V1"])
vnfs.append(["V0", "V1", "V2"])
vnfs.append(["V0", "V1", "V2", "V3"])
vnfs.append(["V0", "V1", "V2", "V3", "V4"])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5"])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6"])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7"])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8"])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9"])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14"])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19"])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append([])
vnfs.append(["V0", "V1", "V2", "V3", "V4", "V5", "V6", "V7", "V8", "V9", "V10", "V11", "V12", "V13", "V14", "V15", "V16", "V17", "V18", "V19", "V20", "V21", "V22", "V23", "V24", "V25", "V26", "V27", "V28", "V29"])

results = list()

def run(i):
    all_plans = helper.generate_all_segmentation_plans(vnfs)

for k in range(0, 1):
    print(k)
    print("----")
    for i in range(10,1,-1):
        print(i)
        startTime = datetime.now()
        for j in range(0, 1000):
            print(j)
            # a = run(i)

        endTime = datetime.now() - startTime
        results.append([k, i, endTime])
        print(endTime)

print("Terminou .....")

with open('result.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["round", "size", "time"]
    writer.writerow(field)
    for result in results:
        writer.writerow(result)
