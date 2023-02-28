import json

with open("data/bib.json") as f:
    data = json.load(f)

data = sorted(data, key=lambda i: i.get("issued", {}).get("date-parts", ["ND"])[0], reverse=True)

with open("data/bib.json", "w") as f:
    json.dump(data, f)