#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:02:57 2022

@author: mike
"""
import io
import os
import geopandas as gpd
import pandas as pd
import numpy as np
import utils
from shapely.geometry import Point, Polygon, box, LineString

pd.options.display.max_columns = 10

##################################################
### Parameters

base_path = os.path.join(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0], 'data')

rec_rivers_shp = '/media/nvme1/data/NIWA/REC25_rivers/rec25_rivers.shp'
rec_catch_shp ='/media/nvme1/data/NIWA/REC25_watersheds/rec25_watersheds.shp'

segment_id_col = 'nzsegment'

# rec_rivers_clean_gpkg = '/media/nvme1/data/NIWA/REC25_rivers/rec25_rivers_clean.gpkg'

rec_rivers_clean_shp = '/media/nvme1/data/NIWA/REC25_rivers/rec25_rivers_clean.shp'
rec_rivers_clean_feather = '/media/nvme1/data/NIWA/REC25_rivers/rec25_rivers_clean.feather'

rec_catch_clean_shp = '/media/nvme1/data/NIWA/REC25_watersheds/rec25_watersheds_clean.shp'
rec_catch_clean_feather = '/media/nvme1/data/NIWA/REC25_watersheds/rec25_watersheds_clean.feather'

#################################################
### Rivers

rec_rivers0 = gpd.read_file(rec_rivers_shp)

## Select basic columns and simplify slightly
rec_rivers1 = rec_rivers0[['nzsegment', 'FROM_NODE', 'TO_NODE', 'geometry']].rename(columns={'FROM_NODE': 'from_node', 'TO_NODE': 'to_node'}).copy()
rec_rivers1['from_node'] = rec_rivers1.from_node.astype('int32')
rec_rivers1['to_node'] = rec_rivers1.to_node.astype('int32')
rec_rivers1['nzsegment'] = rec_rivers1.nzsegment.astype('int32')

rec_rivers1['geometry'] = rec_rivers1['geometry'].simplify(1)

## Find all end segments
end_segs = []
append = end_segs.append
for i, seg in rec_rivers1[['nzsegment', 'from_node', 'to_node']].iterrows():
    # print(i)
    seg_bool = rec_rivers1.from_node == seg.to_node
    if not seg_bool.any():
        append(seg.nzsegment)

## Make sure all lines are oriented downstream and remove lone 1st order streams
rec_rivers1.set_index('nzsegment', inplace=True)

lone_end_seg_list = []
end_seg_list = []
for seg in end_segs:
    row = rec_rivers1.loc[seg].copy()

    # Determine end seg orientation
    other1 = rec_rivers1[rec_rivers1.to_node == row.from_node]

    if not other1.empty:
        row2 = other1.iloc[0]
        pts0 = utils.convert_line_to_points(row.geometry, 0, 'array')
        pts2 = utils.convert_line_to_points(row2.geometry, 0, 'array')

        if (pts0[0] == pts2[-1]).all() or (pts0[0] == pts2[0]).all():
            pass
        elif (pts0[-1] == pts2[-1]).all() or (pts0[-1] == pts2[0]).all():
            print('reverse')
            pts0.reverse()
            row['geometry'] = LineString(pts0)
        else:
            raise ValueError('What is going on...')

        dict1 = row.to_dict()
        dict1['nzsegment'] = row.name
        end_seg_list.append(dict1)
    else:
        lone_end_seg_list.append(seg)
        # print(seg)
        # print('lonely segment')


## Are the lone ones at the upper end just reversed?
from_from_list = []
from_to_list = []

for seg in lone_end_seg_list:
    row = rec_rivers1.loc[seg].copy()

    # Determine end seg orientation
    other1 = rec_rivers1[rec_rivers1.from_node == row.from_node]
    other2 = rec_rivers1[rec_rivers1.from_node == row.to_node]

    if len(other1) > 1:
        from_from_list.append(seg)
    if not other2.empty:
        from_to_list.append(seg)


## Test all upstream segments and correct direction
reaches_lst = []
append = reaches_lst.append
for seg in end_segs:
    print(seg)
    reach1 = rec_rivers1.loc[[seg]].copy()
    append(reach1)
    up1 = rec_rivers1[rec_rivers1.to_node.isin(reach1.from_node)]
    while not up1.empty:
        up_list = []
        for i, row in up1.iterrows():
            base = reach1[reach1.from_node == row.to_node].iloc[0]
            pts0 = utils.convert_line_to_points(base.geometry, 0, 'array')
            pts2 = utils.convert_line_to_points(row.geometry, 0, 'array')

            if (pts0[0] == pts2[-1]).all():
                pass
            else:
                print('reverse')
                print(row)
                pts2 = utils.convert_line_to_points(row.geometry, 3, 'array')
                pts2.reverse()
                row['geometry'] = LineString(pts2)

            row_df = row.to_frame().T
            append(row_df)
            up_list.append(row_df)

        reach1 = pd.concat(up_list)
        up1 = rec_rivers1[rec_rivers1.to_node.isin(reach1.from_node)]

for seg in lone_end_seg_list:
    reach1 = rec_rivers1.loc[[seg]].copy()
    reaches_lst.append(reach1)

reaches = pd.concat(reaches_lst)
reaches.index.name = 'nzsegment'
reaches = reaches.reset_index().drop_duplicates(subset='nzsegment')

# Save cleaned up data
reaches = reaches.merge(rec_rivers0[['nzsegment', 'StreamOrde']].rename(columns={'StreamOrde': 'stream_order'}), on='nzsegment')
reaches.crs = rec_rivers0.crs
# reaches['geometry'] = reaches['geometry'].simplify(0)

reaches.to_file(rec_rivers_clean_shp)

# reaches = gpd.read_file(rec_rivers_clean_shp)
# reaches = reaches.rename(columns={'stream_ord': 'stream_order'})
reaches['nzsegment'] = reaches['nzsegment'].astype('int32')
reaches['from_node'] = reaches['from_node'].astype('int32')
reaches['to_node'] = reaches['to_node'].astype('int32')
reaches['stream_order'] = reaches['stream_order'].astype('int8')

reaches.to_feather(rec_rivers_clean_feather, compression='zstd')

# b1 = io.BytesIO()

# reaches.to_feather(b1, compression='zstd')


del rec_rivers0
del rec_rivers1
del reaches

######################################################
### Watersheds

rec_catch0 = gpd.read_file(rec_catch_shp)

rec_catch1 = rec_catch0[['nzsegment', 'geometry']].copy()

rec_catch1['geometry'] = rec_catch1.buffer(0)
rec_catch1['nzsegment'] = rec_catch1['nzsegment'].astype('int32')

rec_catch1.to_file(rec_catch_clean_shp)

# rec_catch1 = gpd.read_file(rec_catch_clean_shp)

rec_catch1.to_feather(rec_catch_clean_feather, compression='zstd')


































































