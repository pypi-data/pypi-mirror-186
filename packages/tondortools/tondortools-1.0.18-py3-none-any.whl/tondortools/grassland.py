#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import osgeo.ogr as ogr


KEEP_FILENAME = ".tondor_keep"


log = logging.getLogger(__name__)


def has_grassland_polygons(lulc_vector_filepath):
    CLASS_ATTRIBUTE = "LULC_L1"
    CLASS_VALUE = 4
    source = ogr.Open(str(lulc_vector_filepath), update=False)
    layer = source.GetLayer()
    layer_defn = layer.GetLayerDefn()
    field_names = [layer_defn.GetFieldDefn(i).GetName() for i in range(layer_defn.GetFieldCount())]
    if CLASS_ATTRIBUTE not in field_names:
        msg = "File {:s} does not have expected attribute {:s}".format(str(lulc_vector_filepath), CLASS_ATTRIBUTE)
        raise Exception(msg)
    num_matching_polygons = 0
    feature = layer.GetNextFeature()
    while feature is not None:
        # for feature in layer:
        lulc_value = feature.GetField(CLASS_ATTRIBUTE)
        if lulc_value == CLASS_VALUE:
            num_matching_polygons += 1
        feature = layer.GetNextFeature()
    source = None
    if num_matching_polygons == 0:
        log.warning("File {:s} does not have any polygons with {attribute}={class_value}."
                       .format(str(lulc_vector_filepath), attribute=CLASS_ATTRIBUTE, class_value=CLASS_VALUE))
        return False
    else:
        return True
