import geopandas
import sys

ADM_TO_NAME = {
    0 : "country",
    1 : "province",
    2 : "district",
    #3 : "subdistrict",
}

if __name__ == "__main__" :
    mode = sys.argv[1].strip().lower()
    if mode not in {"centroid", "shape"} :
        print("Invalid Mode:", mode)
        sys.exit(0)
    # ADM0 is Country ADM1 is Province ADM2 is District
    ADM = int(sys.argv[2].strip())
    if ADM > 2 :
        print("Invalid ADM Level")
        sys.exit(0)

    filename = f"tha_adm_rtsd_itos_20190221_SHP_PART_1/tha_admbnda_adm{ADM}_rtsd_20190221.shp"
    shp_file = geopandas.read_file(filename).to_crs(epsg=4326)
    
    if mode == "centroid" :
        shp_file["geometry"] = shp_file.centroid

    shp_file.to_file(f"th-adm{ADM}-{ADM_TO_NAME[ADM]}-{mode}.geojson", driver="GeoJSON")
