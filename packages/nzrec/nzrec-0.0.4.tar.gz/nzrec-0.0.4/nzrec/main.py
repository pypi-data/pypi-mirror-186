# -*- coding: utf-8 -*-
"""
Functions to delineate catchments.
"""
import os
import numpy as np
import pandas as pd
from shapely.geometry import Point, Polygon, box, LineString
import shapely
import geopandas as gpd
from scipy.spatial import KDTree
import zstandard as zstd
import orjson
import pathlib
import booklet

# import utils
from . import utils

#####################################################
### Parameters


#####################################################
#### MFE REC streams network


class Water:
    """

    """
    def __init__(self, data_path, download_files=False, only_missing=True):
        """

        """
        ## File check
        missing_files = utils.check_files(data_path)
        if missing_files:
            if download_files:
                utils.download_files(data_path, only_missing=only_missing)
            else:
                raise ValueError('There are missing data files. Files would have been downloaded if download_files=True (but it is not). Othersize if this was a mistake, please check/change the data_path: {}'.format(', '.join([os.path.split(f)[-1] for f in missing_files])))

        self.data_path = pathlib.Path(data_path)

        ## Open files for reading
        self._node = booklet.open(self.data_path.joinpath('node.blt'))
        self._catch = booklet.open(self.data_path.joinpath('catch.blt'))
        self._node_way_index = booklet.open(self.data_path.joinpath('node_way_index.blt'))
        self._way = booklet.open(self.data_path.joinpath('way.blt'))
        self._way_index = booklet.open(self.data_path.joinpath('way_index.blt'))
        self._way_tag = booklet.open(self.data_path.joinpath('way_tag.blt'))

        with open(self.data_path.joinpath('btree.node_ids.np.zstd'), 'rb') as f:
            self._all_node_ids = np.frombuffer(zstd.decompress(f.read()), 'i4')

        self._all_way_ids = tuple(self._way.keys())

        self.ids = None
        self._type = None

        ## Create spatial index
        with open(self.data_path.joinpath('btree.node_coords.np.zstd'), 'rb') as f:
            self._kdtree = KDTree(np.frombuffer(zstd.decompress(f.read()), 'i4').reshape(len(self._node), 2))


    def close(self):
        self._node.close()
        self._catch.close()
        self._node_way_index.close()
        self._way.close()
        self._way_index.close()
        self._way_tag.close()


    def __exit__(self, *args):
        self.close()


    def nearest_node(self, coords, max_distance=np.inf):
        """

        """
        dist, node, way = utils.nearest(self._kdtree, coords, self._all_node_ids, self._node_way_index, self._way, max_distance=max_distance)

        self.source_coords = coords
        self.distance = dist
        self._node_id = node
        self._way_id = way

        return Node(self)


    def nearest_way(self, coords, max_distance=np.inf):
        """

        """
        dist, node, way = utils.nearest(self._kdtree, coords, self._all_node_ids, self._node_way_index, self._way, max_distance=max_distance)

        self.source_coords = coords
        self.distance = dist
        self._node_id = node
        self._way_id = way

        return Way(self)


    def nearest_node_within_catchments(self, coords, max_distance=np.inf):
        """

        """
        dist, node, way = utils.nearest_within_catchments(self._kdtree, coords, self._all_node_ids, self._node, self._node_way_index, self._way, self._catch, max_distance=max_distance)

        self.source_coords = coords
        self.distance = dist
        self._node_id = node
        self._way_id = way

        return Node(self)


    def nearest_way_within_catchments(self, coords, max_distance=np.inf):
        """

        """
        dist, node, way = utils.nearest_within_catchments(self._kdtree, coords, self._all_node_ids, self._node, self._node_way_index, self._way, self._catch, max_distance=max_distance)

        self.source_coords = coords
        self.distance = dist
        self._node_id = node
        self._way_id = way

        return Way(self)


    def add_node(self, node_id=None):
        """

        """
        if node_id is None:
            if self._node_id is None:
                raise ValueError('node_id must be passed to the add_node method.')
        else:
            if node_id in self._all_node_ids:
                way_down = utils.get_down_way(node_id, self._node_way_index, self._way)
                self._node_id = node_id
                self._way_id = way_down
                self.distance = 0
                self.source_coords = None
            else:
                raise KeyError(node_id)

        return Node(self)


    def add_way(self, way_id=None):
        """

        """
        if way_id is None:
            if self._way_id is None:
                raise ValueError('way_id must be passed to the add_way method.')
        else:
            if way_id in self._all_way_ids:
                node_id = self._way[way_id][0]
                self._node_id = node_id
                self._way_id = way_id
                self.distance = 0
                self.source_coords = None
            else:
                raise KeyError(way_id)

        return Way(self)



class Feature:
    """

    """
    def coords(self):
        """

        """
        if issubclass(type(self), Node):
            node_coords = {int(i): self._water._node[int(i)] * 0.0000001 for i in self.nodes}
            return node_coords
        elif issubclass(type(self), Way):
            way_coords = {}
            for way_id in self.ways:
                nodes = self._water._way[int(way_id)]
                way_coords[int(way_id)] = np.array([self._water._node[int(i)] * 0.0000001 for i in nodes])
            return way_coords
        elif issubclass(type(self), Catchment):
            catch_coords = {i: self._water._catch[i] for i in self.ways}
            return catch_coords


    def to_gpd(self, add_attrs=False):
        """

        """
        if issubclass(type(self), Node):
            geo = [Point(self._water._node[int(i)] * 0.0000001) for i in self.nodes]
            gdf = gpd.GeoDataFrame({'node_id': self.nodes}, geometry=geo, crs=4326)
        elif issubclass(type(self), Way):
            geo = []
            for way_id in self.ways:
                nodes = self._water._way[int(way_id)]
                geo.append(LineString(np.array([self._water._node[int(i)] * 0.0000001 for i in nodes])))

            if add_attrs:
                data = []
                append = data.append
                for i in self.ways:
                    d1 = {'way_id': int(i)}
                    d1.update(self._water._way_tag[int(i)])
                    append(d1)
            else:
                data = [{'way_id': int(i)} for i in self.ways]

            gdf = gpd.GeoDataFrame(data, geometry=geo, crs=4326)

        elif issubclass(type(self), Catchment):
            geo = shapely.ops.unary_union([self._water._catch[int(i)] for i in self.ways]).buffer(0.0001)

            gdf = gpd.GeoDataFrame({'way_id': [self.id]}, geometry=[geo], crs=4326)

        return gdf


    def __repr__(self):
        if issubclass(type(self), Node):
            str1 = 'Node ID: {}'
        elif issubclass(type(self), (Way, Catchment)):
            str1 = 'Way ID: {}'
        return str1.format(self.id)


    def __enter__(self):
        return self






class Node(Feature):
    """

    """
    def __init__(self, water):
        """

        """
        self.id = water._node_id
        self._water = water
        self.nodes = set([water._node_id])
        self.distance = water.distance


    def ways(self):
        """

        """
        return Way(self._water)





class Way(Feature):
    """

    """
    def __init__(self, water):
        """

        """
        self.id = water._way_id
        self._water = water
        self.ways = set([water._way_id])
        self.distance = water.distance


    def nodes(self):
        """

        """
        return Node(self._water)


    def upstream(self):
        """

        """
        ways_up = utils.find_upstream(self.id, self._water._node_way_index, self._water._way, self._water._way_index)

        new_way = Way(self._water)
        new_way.ways.update(ways_up)

        return new_way


    def downstream(self):
        """

        """
        ways_down = utils.find_downstream(self.id, self._water._node_way_index, self._water._way)

        new_way = Way(self._water)
        new_way.ways.update(ways_down)

        return new_way


    def catchments(self):
        """

        """
        return Catchment(self)


    def attrs(self):
        """

        """
        data = []
        append = data.append
        for i in self.ways:
            d1 = {'way_id': int(i)}
            d1.update(self._water._way_tag[int(i)])
            append(d1)

        df1 = pd.DataFrame(data)

        return df1



class Catchment(Feature):
    """

    """
    def __init__(self, way_obj):
        """

        """
        self._water = way_obj._water
        self.id = way_obj.id
        self.ways = way_obj.ways




#####################################################
### Combo functions



def between(objs):
    """

    """
    ## Checks
    bool_way = all([isinstance(obj, Way) for obj in objs])
    bool_catch = all([isinstance(obj, Catchment) for obj in objs])

    new_list = []
    if bool_way or bool_catch:

        for obj in objs:
            diff_options = {len(obj.ways.difference(o.ways)): i for i, o in enumerate(objs) if obj.id != o.id}
            min_diff_len = min(diff_options)
            if min_diff_len > 0:
                next_up_way_pos = diff_options[min_diff_len]
                diff_ways = obj.ways.difference(objs[next_up_way_pos].ways)
                new_way_obj = Way(obj._water)
                new_way_obj.ways = diff_ways
            else:
                new_way_obj = obj

            if bool_catch:
                new_list.append(new_way_obj.catchments())
            else:
                new_list.append(new_way_obj)
    else:
        raise TypeError('Input objs must be all either Way or Cathcment objects.')

    return new_list



























































