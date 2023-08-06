#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 20:00:57 2022

@author: mike
"""
import io
import os
import geopandas as gpd
import pandas as pd
import numpy as np
import pathlib
from shapely.geometry import Point, Polygon, box, LineString
from copy import copy
from time import time
import booklet
import shapely
from scipy.spatial import KDTree
import zstandard as zstd
from hashlib import blake2b, blake2s

import utils

pd.options.display.max_columns = 10

##################################################
### Parameters

base_path = pathlib.Path(os.path.join(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0], 'data'))

rec_rivers_clean = '/media/nvme1/data/NIWA/REC25_rivers/rec25_rivers_clean.feather'

rec_catch_clean = '/media/nvme1/data/NIWA/REC25_watersheds/rec25_watersheds_clean.feather'

node_blt = 'node.blt'
way_blt = 'way.blt'
way_tag_blt = 'way_tag.blt'
node_way_blt = 'node_way_index.blt'
way_index_blt = 'way_index.blt'
catch_blt = 'catch.blt'


# class NodeSerial:
#     def dumps(obj):
#         return (obj.round(7) * 10000000).astype('i4').tobytes()
#     def loads(obj):
#         return np.frombuffer(obj, 'i4') * 0.0000001

tag_files = {
    'NZRiverMaps_bed_sediment_2023-01-14.csv': ('nzsegment', 'Catchment name', 'Strahler stream order', 'Region', 'Bedrock', 'Boulder', 'CoarseGravel', 'Cobble', 'FineGravel', 'Mud', 'Sand'),
    'NZRiverMaps_bird_habitat_2023-01-14.csv': ('Whio (blue duck)'),
    'NZRiverMaps_fish_habitat_2023-01-14.csv': ('Koaro total WUA low flow', 'Koaro WUA_MALF / WW_Median', 'Longfin total WUA low flow', 'Longfin WUA_MALF / WW_Median', 'Shortfin total WUA low flow', 'Shortfin WUA_MALF / WW_Median', 'Smelt total WUA low flow', 'Smelt WUA_MALF / WW_Median', 'Torrentfish total WUA low flow', 'Torrentfish WUA_MALF / WW_Median', 'Trout total WUA low flow', 'Trout WUA_MALF / WW_Median'),
    'NZRiverMaps_fish_presence_2023-01-14.csv': ("Alpine galaxias","Banded kokopu","Bignose galaxias","Black flounder","Bluegill bully","Brook char","Brook char (Potential)","Brown trout","Brown trout (Potential)","Canterbury galaxias","Chinook salmon","Clutha flathead galaxias","Common bully","Common smelt","Crans bully","Dwarf galaxias","Flathead galaxias","Gambusia","Gambusia (Potential)","Giant bully","Giant kokopu","Goldfish","Goldfish (Potential)","Gollum galaxias","Inanga","Koaro","Lamprey","Longfin eel","Northern flathead galaxias","Rainbow trout","Rainbow trout (Potential)","Redfin bully","Roundhead galaxias","Shortfin eel","Shortjaw kokopu","Torrentfish","Upland bully","Upland longjaw galaxias"),
    'NZRiverMaps_hydrology_2023-01-09.csv': ("1 in 5 year low flow","February flow seasonality","FRE3","MALF","Mean Flow","Median flow","Month lowest mean flow"),
    'NZRiverMaps_invertebrate_2023-01-14.csv': ("% EPT Richness","EPT","EPTNoHydrop","Invertebrate Taxa Richness","MCI (2015)","MCI (2019)","MCI (2021)","Number of EPT taxa","Number of taxa","SQMCI-hb"),
    'NZRiverMaps_isotopes_2023-01-14.csv': ("delta 18O","delta 2H"),
    'NZRiverMaps_rec_2023-01-09.csv': ("Climate class","Geology class","Landcover class","Network position class","Topography class","Upstream catchment area","Valley landform class"),
    'NZRiverMaps_sediment_load_2023-01-14.csv': ("Suspended sediment load","Suspended sediment load lake percent change ","Suspended sediment load no lake adjustment"),
    'NZRiverMaps_wetted_width_2023-01-14.csv': ("Width at MALF","Width at mean flow","Width at median flow","Width at Q5"),
    'NZRiverMaps_WQ_2023-01-14.csv': ("Ammoniacal nitrogen AnnMax pH","Ammoniacal nitrogen median","Ammoniacal nitrogen median pH","ANZECC elevation class","CHLA 92%","CHLA Mean","Dissolved oxygen","Dissolved oxygen saturation","Dissolved reactive phosphorus median","Dissolved reactive phosphorus Q95","E. coli G260","E. coli G540","E. coli median","E. coli Q95","Nitrate + nitrite median","Nitrate + nitrite Q95","Temperature","Total nitrogen median","Total phosphorus median","Total suspended solids","Turbidity median","Visual clarity median","WCC 92%","WCC Mean"),
    }

tag_float_cols = ['Bedrock', 'Boulder', 'CoarseGravel', 'Cobble', 'FineGravel', 'Mud', 'Sand', 'Whio (blue duck)', 'Koaro total WUA low flow', 'Koaro WUA_MALF / WW_Median', 'Longfin total WUA low flow', 'Longfin WUA_MALF / WW_Median', 'Shortfin total WUA low flow', 'Shortfin WUA_MALF / WW_Median', 'Smelt total WUA low flow', 'Smelt WUA_MALF / WW_Median', 'Torrentfish total WUA low flow', 'Torrentfish WUA_MALF / WW_Median', 'Trout total WUA low flow', 'Trout WUA_MALF / WW_Median', "1 in 5 year low flow", "February flow seasonality", "FRE3","MALF","Mean Flow","Median flow", "% EPT Richness","EPT","EPTNoHydrop","Invertebrate Taxa Richness","MCI (2015)","MCI (2019)","MCI (2021)","Number of EPT taxa","Number of taxa","SQMCI-hb", "delta 18O","delta 2H", "Upstream catchment area", "Suspended sediment load","Suspended sediment load lake percent change ","Suspended sediment load no lake adjustment", "Width at MALF","Width at mean flow","Width at median flow","Width at Q5", "Ammoniacal nitrogen AnnMax pH","Ammoniacal nitrogen median","Ammoniacal nitrogen median pH","ANZECC elevation class","CHLA 92%","CHLA Mean","Dissolved oxygen","Dissolved oxygen saturation","Dissolved reactive phosphorus median","Dissolved reactive phosphorus Q95","E. coli G260","E. coli G540","E. coli median","E. coli Q95","Nitrate + nitrite median","Nitrate + nitrite Q95","Temperature","Total nitrogen median","Total phosphorus median","Total suspended solids","Turbidity median","Visual clarity median","WCC 92%","WCC Mean"]

float_precision = 4

###############################################
### Rivers

rivers0 = gpd.read_feather(rec_rivers_clean)
rivers1 = rivers0.to_crs(4326)
# rivers1['nzsegment'] = rivers1.nzsegment.astype('int32')
# rivers1['from_node'] = rivers1.from_node.astype('int32')
# rivers1['to_node'] = rivers1.to_node.astype('int32')

### Make the dicts
# dict_start = time()
way_dict = {}
node_dict = {}
way_tag_dict = {}

node_counter = 1000000
for i, row in rivers1.iterrows():
    # print(i)
    # Nodes
    tmp_node = {}
    nodes = list(row.geometry.coords)
    tmp_node[row.from_node] = np.array(nodes[0])

    for n in nodes[1:-1]:
        node_id = node_counter
        node_counter += 1
        tmp_node[node_id] = np.array(n)

    tmp_node[row.to_node] = np.array(nodes[-1])

    node_dict.update(tmp_node)

    # Ways
    way_id = int(row.nzsegment)
    way_dict[way_id] = list(tmp_node.keys())
    way_tag_dict[way_id] = {'Strahler stream order': row.stream_order}

# dict_end = time()

# print((dict_end - dict_start)/60)

## node to way index
node_way_dict = {}
for i, wa in way_dict.items():
    # print(i)
    for n in wa:
        if n in node_way_dict:
            node_way_dict[int(n)].append(i)
        else:
            node_way_dict[int(n)] = [i]

## way to way index
way_index_dict = {}
for w, nodes in way_dict.items():
    waynode = []
    for node in nodes:
        if node in node_way_dict:
            ways = copy(node_way_dict[node])
            ways.remove(w)
            if ways:
                waynode.extend(ways)
    way_index_dict[w] = waynode

d

### Make the special persistant dicts
with booklet.open(base_path.joinpath(way_blt), 'n', value_serializer='numpy_int4', key_serializer='uint4', n_bytes_value=2, n_buckets=100000) as way:
    for k, v in way_dict.items():
        way[k] = np.array(v)

with booklet.open(base_path.joinpath(node_blt), 'n', value_serializer='numpy_int4', key_serializer='uint4', n_bytes_value=1, n_buckets=500000) as node:
    for k, v in node_dict.items():
        node[k] = (v.round(7) * 10000000).astype('i4')

# with booklet.open(base_path.joinpath(way_tag_blt), 'n', value_serializer='orjson_zstd', key_serializer='uint4', n_bytes_value=1, n_buckets=100000) as way_tag:
#     for k, v in way_tag_dict.items():
#         way_tag[k] = v

with booklet.open(base_path.joinpath(node_way_blt), 'n', value_serializer='numpy_int4', key_serializer='uint4', n_bytes_value=1, n_buckets=500000) as node_way:
    for k, v in node_way_dict.items():
        node_way[k] = np.array(v)

with booklet.open(base_path.joinpath(way_index_blt), 'n', value_serializer='numpy_int4', key_serializer='uint4', n_bytes_value=1, n_buckets=100000) as way_index:
    for k, v in way_index_dict.items():
        way_index[k] = np.array(v)


### Catchments
catch0 = gpd.read_feather(rec_catch_clean)
catch1 = catch0.to_crs(4326)

with booklet.open(base_path.joinpath(catch_blt), 'n', value_serializer='wkb_zstd', key_serializer='uint4', n_bytes_value=3, n_buckets=100000) as catch:
    for k, v in catch1.iterrows():
        catch[v.nzsegment] = v.geometry


## Btree index
node = booklet.open(base_path.joinpath(node_blt))
node_ids = np.array(list(node.keys()), dtype='int32')

nodes_coords = np.array([v for v in node.values()])
# node_ids = np.array([v for v in node.keys()], dtype='i4')

# btree = KDTree(nodes_coords, copy_data=True)

with open('/media/nvme1/git/nzrec/data/btree.node_coords.np.zstd', 'wb') as f:
    f.write(zstd.compress(nodes_coords.tobytes(), 20))

# with open('/media/nvme1/git/nzrec/data/btree.node_coords.np.zstd', 'rb') as f:
#     nodes3 = np.frombuffer(zstd.decompress(f.read()), 'i4').reshape(nodes_coords.shape)

with open('/media/nvme1/git/nzrec/data/btree.node_ids.np.zstd', 'wb') as f:
    f.write(zstd.compress(node_ids.tobytes(), 20))

### Way tags
rec_rivers_base_path = pathlib.Path(rec_rivers_clean).parent
tag_df_list = []
for file, cols in tag_files.items():
    print(file)
    if isinstance(cols, str):
        cols = [cols]
    df1 = pd.read_csv(rec_rivers_base_path.joinpath(file), usecols=list(cols))
    tag_df_list.append(df1)

combo_tag = pd.concat(tag_df_list, axis=1)
combo_tag = combo_tag.set_index('nzsegment')

combo_tag = combo_tag[combo_tag.index.isin(set(way_tag_dict.keys()))].copy()

missing_segs = list(set(way_tag_dict.keys()).difference(set(combo_tag.index)))

stream_orders = []
for seg_id in missing_segs:
    stream_orders.append(way_tag_dict[seg_id]['Strahler stream order'])

mis_seg_df = pd.Series(stream_orders, index=missing_segs)
mis_seg_df.name = 'Strahler stream order'

combo_tag = pd.concat([combo_tag, mis_seg_df.to_frame()])

combo_tag.index = combo_tag.index.astype('int32')
combo_tag['Strahler stream order'] = combo_tag['Strahler stream order'].astype(int)
combo_tag[tag_float_cols] = combo_tag[tag_float_cols].round(float_precision)


with booklet.open(base_path.joinpath(way_tag_blt), 'n', value_serializer='orjson_zstd', key_serializer='uint4', n_bytes_value=3, n_buckets=100000) as way_tag:
    for seg_id, row in combo_tag.iterrows():
        way_tag[seg_id] = row.to_dict()














############################################################
### Testing




# node_id = 590718
# node_id = 436822

# node_way = booklet.open(base_path.joinpath(node_way_blt))
# way = booklet.open(base_path.joinpath(way_blt))
# way_index = booklet.open(base_path.joinpath(way_index_blt))
# node = booklet.open(base_path.joinpath(node_blt))
# catch = booklet.open(base_path.joinpath(catch_blt))

# ways_up = find_upstream(node_id, node_way, way, way_index)

# reach_gpd = make_reaches(ways_up, way, node)

# reach_gpd.to_file(base_path.joinpath('test_reach.gpkg'))


# way_down = find_downstream(node_id, node_way, way, way_index)

# catch_gpd = gpd.GeoDataFrame([node_id], geometry=[catch1], columns=['way_id'], crs=4326)

# catch_gpd.to_file(base_path.joinpath('test_catch.gpkg'))






# keys = list(node_dict.keys())

# mod_set = set()
# mod_dict = {}
# for key in keys:
#     k_int = int.from_bytes(blake2b(key.to_bytes(4, 'little'), digest_size=13).digest(), 'little')
#     mod = k_int % 9765625
#     if mod in mod_set:
#         if mod in mod_dict:
#             mod_dict[mod] += mod_dict[mod]
#         else:
#             mod_dict[mod] = 2
#     mod_set.add(mod)






















