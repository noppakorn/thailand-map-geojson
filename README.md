# thailand-map-geojson
## About
- I couldn't find any Thailand maps with updated data in form of GeoJSON. 
- The data avalible is from [The Humanitarian Data Exchange](https://data.humdata.org/dataset/thailand-administrative-boundaries) which is provided in form of shp file.
- All code that will be used to convert the map is written in Python.
- Map is used by [The Researcher](https://github.com/porames/the-researcher-covid-bot). See the specific build at [the-researcher-covid-bot-map](the-researcher-covid-bot-map)
## Requirements
- Python 3
- pandas
- geopandas
- requests (for downloading files)
## Building the map
1. Install Requirements `pip install -r requirements.txt`
2. Download the shp file `python download_thailand_map.py`
3. Build the map with `python convert_shp_to_geojson.py [MODE] [ADM LEVEL]`, Example : `python convert_shp_to_geojson.py shape 2`
## Parameters Details
- MODE : centroid, shape
- ADM LEVEL : 1,2,3
## Data Source
- [The Humanitarian Data Exchange](https://data.humdata.org/dataset/thailand-administrative-boundaries)
