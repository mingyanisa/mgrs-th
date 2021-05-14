import geopandas
import mgrs
import json
geojson_file_path = "./data/tha_province_boundary.geojson"
# gdf = geopandas.read_file("./data/tha_province_boundary.zip")
# gdf.to_file("./data/tha_province_boundary.geojson", driver='GeoJSON')
with open(geojson_file_path, 'r') as geojson:
    geojson_dict = json.load(geojson)
province = {}
m = mgrs.MGRS()
for farm in geojson_dict["features"]:
    grids=[]
    for coord in farm["geometry"]["coordinates"][0]:
        if len(coord)>2:
            coord=coord[0]
        lng,lat = coord
        c = m.toMGRS(lat, lng)
        grid = "".join(c[:5])
        if grid not in grids:
            grids.append(grid)
    print(farm["properties"]["ADM1_TH"],grids)
    province[farm["properties"]["ADM1_TH"]]=grids

with open('./result/province_grid.json', 'w') as fp:
    json.dump(province, fp, ensure_ascii=False)
    