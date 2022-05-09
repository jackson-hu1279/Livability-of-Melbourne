import json

# list of greater melbourne lga code
greater_melbourne_lga_code = [24600, 25900, 26350, 27350, 20660, 20910, 21110, 21890, 22310, 23110, 23430, 24210, 24330,
                              24970, 25060, 25250, 26980, 21180, 21450, 21610, 22170, 22670, 23270, 23670, 24410,
                              24650, 25340, 25710, 27070, 27260, 27450]
greater_melbourne_lga_name = ["Melbourne City", "Port Phillip City", "Stonnington City", "Yarra City", "Banyule City", "Bayside City", "Boroondara City", "Darebin City", "Glen Eira City",
                              "Hobsons Bay City", "Kingston City", "Manningham City", "Maribyrnong City", "Monash City", "Moonee Valley City",
                              "Moreland City", "Whitehorse City", "Brimbank City", "Cardinia Shire", "Casey City", "Frankston City", "Greater Dandenong City",
                              "Hume City", "Knox City", "Maroondah City", "Melton City", "Mornington Peninsula Shire", "Nillumbik Shire", "Whittlesea City", "Wyndham City", "Yarra Ranges Shire"]

file_name1 = "results-income.json"
file_name2 = "results-vic-lga.geojson"


def makeDict(code, name):
    lga_dict = {}
    for i in range(0, len(code)):
        lga_dict[name[i]] = code[i]
    return lga_dict


with open(file_name1) as f:
    dataset = json.load(f)
    lga_mean = {}
    lga_median = {}
    lga_sum = {}
    lga_median_age = {}
    for data in dataset["greater_melbourne"]:
        lga_code = data["lga_code"]
        mean_income = data["mean_income"]
        median_income = data["median_income"]
        sum_income = data["sum_income"]
        median_age_earner = data["median_age_earner"]
        lga_mean[lga_code] = mean_income
        lga_median[lga_code] = median_income
        lga_sum[lga_code] = sum_income
        lga_median_age[lga_code] = median_age_earner

with open(file_name2) as f:
    dataset = json.load(f)
    results_list = []
    data_dict = makeDict(greater_melbourne_lga_code,
                         greater_melbourne_lga_name)
    for data in dataset["features"]:
        lga_name = data["properties"]["lga_name"]
        if lga_name in greater_melbourne_lga_name:
            lga_code = data_dict[lga_name]
            data["properties"] = {"lga_code": lga_code, "lga_name": lga_name, "mean_income": lga_mean[lga_code],
                                  "median_income": lga_median[lga_code], "sum_income": lga_sum[lga_code], "median_age_earner": lga_median_age[lga_code]}
            results_list.append(data)


result = {"type": "FeatureCollection", "features": []}
result["features"] = results_list

# create JSON file to store process data
final_results = result
output_file = "geojson-" + file_name1
with open(output_file, "w") as f:
    json.dump(final_results, f)
