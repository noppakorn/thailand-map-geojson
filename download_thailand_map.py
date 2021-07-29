import requests
import zipfile
import io

def download(URL : str) -> None:
    print("Downloading")
    req = requests.get(map_url)
    print("Downloaded, Unzipping")
    zip_file = zipfile.ZipFile(io.BytesIO(req.content))
    zip_file.extractall(".")
    print("Done")


if __name__ == "__main__":
    map_url = "https://data.humdata.org/dataset/d24bdc45-eb4c-4e3d-8b16-44db02667c27/resource/d0c722ff-6939-4423-ac0d-6501830b1759/download/tha_adm_rtsd_itos_20190221_shp_part_1.zip"
    download(map_url)

