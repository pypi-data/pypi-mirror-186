# -*- coding: utf-8 -*-
"""
Utility functions.
"""
import os
import io
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, Polygon, box, LineString
import shapely
from scipy.spatial import KDTree
import zstandard as zstd
import pathlib
from copy import copy
import smart_open
import smart_open.http as so_http
from time import sleep
import concurrent.futures

so_http.DEFAULT_BUFFER_SIZE = 524288

#########################################
### parameters

file_dict = {'btree.node_coords.np.zstd': 'https://b2.tethys-ts.xyz/file/nz-rec/btree.node_coords.np.zstd',
             'catch.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/catch.blt',
             'node.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/node.blt',
             'node_way_index.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/node_way_index.blt',
             'way.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/way.blt',
             'way_index.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/way_index.blt',
             'way_tag.blt': 'https://b2.tethys-ts.xyz/file/nz-rec/way_tag.blt',
             'btree.node_ids.np.zstd': 'https://b2.tethys-ts.xyz/file/nz-rec/btree.node_ids.np.zstd'
             }


########################################
### Functions


def url_to_file(url, file_path, chunk_size: int=524288, retries=3):
    """
    General function to get an object from an S3 bucket. One of s3, connection_config, or public_url must be used.

    Parameters
    ----------
    url: http str
        The http url to the file.
    chunk_size: int
        The amount of bytes to download as once.

    Returns
    -------
    file object
        file object of the S3 object.
    """
    transport_params = {'buffer_size': chunk_size, 'timeout': 120}

    ## Get the object
    counter = retries
    while True:
        try:
            file_obj = smart_open.open(url, 'rb', transport_params=transport_params, compression='disable')
            file_path1 = pathlib.Path(file_path)
            file_path1.parent.mkdir(parents=True, exist_ok=True)

            with open(file_path1, 'wb') as f:
                chunk = file_obj.read(chunk_size)
                while chunk:
                    f.write(chunk)
                    chunk = file_obj.read(chunk_size)
            break
        except Exception as err:
            counter = counter - 1
            if counter > 0:
                sleep(3)
            else:
                print('smart_open could not open url with the following error:')
                print(err)
                file_obj = None
                break

    return file_obj


def check_files(data_path):
    """

    """
    data_path1 = pathlib.Path(data_path)

    files = [f.name for f in data_path1.glob('*') if f.name in file_dict]
    missing_files = []
    for f in file_dict:
        if f not in files:
            missing_files.append(file_dict[f])

    return missing_files


def download_files(data_path, only_missing=True):
    """

    """
    if only_missing:
        urls = check_files(data_path)
    else:
        urls = list(file_dict.values())

    print('Downloading: {}'.format(', '.join([os.path.split(url)[-1] for url in urls])))
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for url in urls:
            file_name = os.path.split(url)[-1]
            new_path = os.path.join(data_path, file_name)
            f = executor.submit(url_to_file, url, new_path)
            futures.append(f)
        _ = concurrent.futures.wait(futures)


def get_down_way(node_id, node_way, way):
    """

    """
    base_ways0 = set(node_way[int(node_id)])

    for way_id in base_ways0:
        nodes = way[int(way_id)]
        if node_id != nodes[-1]:
            way_down = way_id
            break

    return way_down


def make_kdtree(coords):
    """

    """
    kdtree = KDTree(coords)

    return kdtree


def nearest(kdtree, coords, nodes, node_way, way, max_distance=np.inf):
    """
    Function to find the nearest nodes and ways from coords. Uses the scipy function cKDTree.

    Parameters
    ----------
    kdtree : KDTree init object
        Already initialized KDTree.
    coords : np.array
        An array of (2) shape for coordiantes to query.
    nodes : np.array
        An array of node ids ordered by the original data of the kdtree.
    node_way : dict-like
        A dict of nodes to ways.
    max_distance : non-negative int, optional
        Return only neighbors within this distance. This is used to prune tree searches, so if you are doing a series of nearest-neighbor queries, it may help to supply the distance to the nearest neighbor of the most recent point.

    Returns
    -------
    distance, nodes, ways
    """
    coords1 = (np.asarray(coords) * 10000000).round().astype('int32')

    if isinstance(max_distance, int):
    	max_distance1 = 100 * max_distance
    else:
        max_distance1 = np.inf

    dist, idx = kdtree.query(coords1, k=1, distance_upper_bound=max_distance1)
    out_node = nodes[idx]
    out_way = get_down_way(out_node, node_way, way)

    return int(round(dist*0.01, 0)), out_node, out_way


def nearest_within_catchments(kdtree, coords, nodes, node, node_way, way, catch, max_distance=np.inf):
    """

    """
    coords1 = (np.asarray(coords) * 10000000).round().astype('int32')

    if isinstance(max_distance, int):
    	max_distance1 = 100 * max_distance
    else:
        max_distance1 = np.inf

    k = [1]
    while True:
        dist, idx = kdtree.query(coords1, k=k, distance_upper_bound=max_distance1)
        out_node = nodes[idx[0]]
        out_way = get_down_way(out_node, node_way, way)
        out_catch = catch[out_way]
        check = out_catch.intersects(Point(node[out_node] * 0.0000001))
        if check:
            distance = int(round(dist[0]*0.01, 0))
            break
        else:
            if k[0] > 100:
                raise ValueError('Cannot find any catchments.')
            k = [k[0] + 1]

    return distance, out_node, out_way


def find_upstream(way_id, node_way, way, way_index):
    """

    """
    ways_up = set([way_id])

    new_ways = set(way_index[int(way_id)]).difference(ways_up)

    down_node = way[int(way_id)][-1]
    down_ways = set(node_way[down_node])

    new_ways = new_ways.difference(down_ways)

    while new_ways:
        ways_up.update(new_ways)
        old_ways = copy(new_ways)
        new_ways = set()
        for old_way in old_ways:
            new_ways1 = set(way_index[old_way])
            new_ways.update(new_ways1)
        new_ways = new_ways.difference(ways_up)

    return ways_up


def find_downstream(way_id, node_way, way):
    """

    """
    way_down = way_id
    ways_down = [way_down]
    append = ways_down.append

    while True:
        down_node = way[int(way_down)][-1]

        down_ways = list(node_way[int(down_node)])
        down_ways.remove(way_down)

        if down_ways:
            for down_way in down_ways:
                up_node = way[int(down_way)][0]
                if up_node == down_node:
                    append(down_way)
                    way_down = down_way
                    break
        else:
            break

    return ways_down


# def make_reaches(ways, way, node, output='shapely'):
#     """

#     """
#     way_ids = []
#     reach_list = []
#     for way_id in ways:
#         nodes = way[int(way_id)]
#         reach = np.array([node[int(node_id)] for node_id in nodes])

#         if output in ('shapely', 'geopandas'):
#             reach = LineString(reach)

#         reach_list.append(reach)
#         way_ids.append(way_id)

#     if output == 'geopandas':
#         reach_out = gpd.GeoDataFrame(way_ids, geometry=reach_list, columns=['way_id'], crs=4326)
#     else:
#         reach_out = dict(zip(way_ids, reach_list))

#     return reach_out


# def make_catchment(ways_up, catch):
#     """

#     """
#     catch_list = []
#     append = catch_list.append
#     for way_id in ways_up:
#         catch0 = catch[int(way_id)]
#         append(catch0)

#     catch1 = shapely.ops.unary_union(catch_list).buffer(0.0001)

#     return catch1


