# thailand-map-geojson
## About
- I couldn't find any Thailand maps in the form of geojson.
- The data avalible is from [The Humanitarian Data Exchange](https://data.humdata.org/dataset/thailand-administrative-boundaries) which is provided in form of shp file.
- All code that will be used to convert the map is written in Python.
## Requirements
- Python 3
- pandas
- geopandas
- requests (for downloading files)
## Building the map
1. Install Requirements `pip install -r requirements.txt`
2. Download the shp file `python download_thailand_map.py`

## Data Source
- [The Humanitarian Data Exchange](https://data.humdata.org/dataset/thailand-administrative-boundaries)
