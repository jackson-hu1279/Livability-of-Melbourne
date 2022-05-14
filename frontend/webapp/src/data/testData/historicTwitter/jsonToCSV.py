# ----------------------------------------------
# --------
#
# Cluster and Cloud Computing Assignment 2 - Team 53
# 
# Authors: 
# - Chi Yin Wong (Student ID: 836872)
# - Kaiquan Lin (Student ID: 1147233)
# - Renkai Liao (Student ID: 1141584)
# - Renwei Hu (Student ID: 1067974)
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Author of this file:
# - Siwat Chairattanamanokorn (Student ID: 1338152)
#
# Location:
# - Melbourne
#
# --------
# ----------------------------------------------

import json
import csv


def to_csv(filename):
    header = ["lga_code", "lga_name", "latitude", "longitude"]
    results = []
    with open(filename) as f:
        dataset = json.load(f)
        for data in dataset["docs"]:
            lga_code = data["LGA_CODE"]
            lga_name = data["LGA_NAME"]
            latitude = data["geo"]["coordinates"][0]
            longtitude = data["geo"]["coordinates"][1]
            result = [lga_code, lga_name, latitude, longtitude]
            results.append(result)

    output_file = "processed-" + filename[:-4] + "csv"
    with open(output_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(results)


to_csv("crimes-updated-lga.json")
to_csv("health-updated-lga.json")
