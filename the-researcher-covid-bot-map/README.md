# the-researcher-covid-bot-map
## About
- Map is used by [The Researcher](https://github.com/porames/the-researcher-covid-bot).
- Specifically [this](th-amphoes-points-with-centroid-id.json).
- Map Data is updated at 2019-03-01
## Requirements
- Python 3
- pandas
- geopandas
- requests (for downloading files)
## Building the map
1. Install Requirements `pip install -r ../requirements.txt`
2. Download the shp file `python ../download_thailand_map.py`. Will download and unzipped files.
3. Build the map with `python district_shp_to_centroid.py`
4. Add centroid field to map with `python add_centroid_field.py`
## Data Source
- [The Humanitarian Data Exchange](https://data.humdata.org/dataset/thailand-administrative-boundaries)
