import json

with open("th-adm2-district-centroid.geojson", encoding="utf-8") as f:
    district_data = json.load(f)

for feature in district_data["features"]:
    feature["properties"]["cen_lat"] = feature["geometry"]["coordinates"][0]
    feature["properties"]["cen_long"] = feature["geometry"]["coordinates"][1]

with open("th-amphoes-points-with-centroid-id.json", "w+", encoding="utf-8") as fout :
    json.dump(district_data,fout, ensure_ascii=False, indent=2)
