"""
Generate th-adm2-district-centroid.geojson containing
Centroid Geometry and fid with province and district code
adjusted to match The Researcher
"""
import geopandas

filename = "../tha_adm_rtsd_itos_20190221_SHP_PART_1/tha_admbnda_adm2_rtsd_20190221.shp"
 
# Fields name mapping to use with the-researcher-covid-bot
COL_NAME_MAPPING = {
    "ADM1_EN": "P_NAME_E",
    "ADM1_TH": "P_NAME_T",
    "ADM1_PCODE": "P_CODE",
    "ADM2_EN": "A_NAME_E",
    "ADM2_TH": "A_NAME_T",
    "ADM2_PCODE": "A_CODE",
}

def last_two_char(string : str) -> str:
    return string[-2:]


shp_file = geopandas.read_file(filename).to_crs(epsg=4326)
shp_file["geometry"] = shp_file.centroid

shp_file = shp_file.drop(columns=['Shape_Leng', 'Shape_Area', 'ADM2_REF', 'ADM2ALT1EN', 'ADM2ALT2EN', 'ADM2ALT1TH', 'ADM2ALT2TH','ADM0_EN', 'ADM0_TH', 'ADM0_PCODE','date', 'validOn', 'validTo'])

shp_file = shp_file.rename(columns=COL_NAME_MAPPING)

shp_file.P_NAME_E = shp_file.P_NAME_E.str.upper()
shp_file.A_NAME_E = shp_file.A_NAME_E.str.upper()

shp_file.A_CODE = shp_file.A_CODE.apply(lambda name : last_two_char(name))
shp_file.P_CODE = shp_file.P_CODE.apply(lambda name : last_two_char(name))

shp_file = shp_file.reset_index().rename(columns={"index": "fid"})
shp_file.fid += 1
print(shp_file)

shp_file.to_file('th-adm2-district-centroid.geojson', driver='GeoJSON')