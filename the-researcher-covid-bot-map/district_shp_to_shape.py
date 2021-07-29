import json

with open("../th-adm2-district-centroid.geojson", encoding="utf-8") as f:
    district_data_centroid = json.load(f)

for feature in district_data_centroid["features"]:
    feature["properties"]["centroid"] = feature["geometry"]["coordinates"]

with open("../th-adm2-district-shape.geojson", encoding="utf-8") as f:
    district_data_shape = json.load(f)

for i in range(0,928):
    district_data_centroid["features"][i]["geometry"] = district_data_shape["features"][i]["geometry"]

with open("th-district-shape-fid.json", "w+", encoding="utf-8") as fout :
    json.dump(district_data_centroid,fout, ensure_ascii=False, indent=2)
