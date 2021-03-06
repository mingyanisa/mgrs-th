## Public MGRS code for Thailand

![alt text](https://raw.githubusercontent.com/mingyanisa/mgrs-th/master/mgrs-th.jpg)

This repository is opensource and publicly open for anyone to contribute!

p.s. This mini-project is part of my work at [ARV(PTTEP)](https://www.arv.co.th/) and [Varuna](https://www.varunatech.co/) company

### Dataset
---
1. data/tha_province_boundary.geojson : The Geojson file converting from Thailand shapefile
2. result/province_grid.json : MGRS code group by province
3. result/region_grid.json : MGRS code group by region

### Example Usecase
---
You can use the MGRS code to specify which tile/image grid that you want to download from the data source e.g. AWS S3 bucket (opendata for [Sentinel2](https://registry.opendata.aws/sentinel-2/)) and calculate NDVI index from those images.