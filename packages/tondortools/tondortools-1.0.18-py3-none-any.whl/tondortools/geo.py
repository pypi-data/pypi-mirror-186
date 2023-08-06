#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import ceil
from math import floor

import osgeo.ogr as ogr
import osgeo.osr as osr


def count_features(src_filepath):
    src_ds = ogr.Open(str(src_filepath))
    lyr = src_ds.GetLayer()
    return lyr.GetFeatureCount()


def create_transformation(src_epsg, dest_epsg):
    src_srs = osr.SpatialReference()
    src_srs.ImportFromEPSG(src_epsg)
    try:
        src_srs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    except Exception:
        pass
    dest_srs = osr.SpatialReference()
    dest_srs.ImportFromEPSG(dest_epsg)
    try:
        dest_srs.SetAxisMappingStrategy(osr.OAMS_TRADITIONAL_GIS_ORDER)
    except Exception:
        pass
    transformation = osr.CoordinateTransformation(src_srs, dest_srs)
    return transformation


def transform_geom(geom, src_epsg, dest_epsg):
    if src_epsg == dest_epsg:
        dest_geom = geom.Clone()
    else:
        transformation = create_transformation(src_epsg, dest_epsg)
        dest_geom = geom.Clone()
        dest_geom.Transform(transformation)
    return dest_geom

def read_raster_info(raster_filepath):
    ds = gdal.Open(str(raster_filepath))
    xmin, pixel_width, _, ymax, _, yres = ds.GetGeoTransform()
    projection = ds.GetProjection()
    datatype = ds.GetRasterBand(1).DataType
    n_bands = ds.RasterCount
    epsg = ds.GetSpatialRef().GetAuthorityCode(None)
    return (xmin, ymax, ds.RasterXSize, ds.RasterYSize, pixel_width, projection, epsg, datatype, n_bands)

def reproject_multibandraster(composite_filepath, warped_filepath, target_epsg, pixel_size, xmin, xmax, ymin, ymax, work_dir, method ='bilinear'):

    cmd = ["gdalwarp",
           "-t_srs", "EPSG:{}".format(target_epsg),
           "-tr", str(pixel_size), str(pixel_size),
           "-te",str(xmin),str(ymin),str(xmax),str(ymax),
           "-r", method,
           "-co", "COMPRESS=DEFLATE",
           str(composite_filepath),
           str(warped_filepath)
           ]
    run_subprocess(cmd, work_dir)
    
    
def compile_catalog_geom(aoi_wkt, aoi_epsg, aoi_buffer, catalog_epsg):
    aoi_geom = ogr.CreateGeometryFromWkt(aoi_wkt)
    aoi_geom = aoi_geom.Buffer(aoi_buffer)
    catalog_geom = transform_geom(aoi_geom, aoi_epsg, catalog_epsg)
    (xmin, xmax, ymin, ymax) = catalog_geom.GetEnvelope()
    catalog_bbox_tuple = (xmin, ymin, xmax, ymax)
    return catalog_geom, catalog_bbox_tuple


class BoundingBox():
    """Utility class for various bounding box handling."""

    def __init__(self, xmin, ymin, xmax, ymax, epsg):
        # Ensure min is always less than max.
        if xmin > xmax:
            xmin, xmax = xmax, xmin
        if ymin > ymax:
            ymin, ymax = ymax, ymin

        # Set up members.
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.epsg = epsg

    def pixel_count(self, size):
        width = int((self.xmax - self.xmin) / size)
        height = int((self.ymax - self.ymin) / size)
        return width * height

    def enlarge(self, size):
        xmin = self.xmin - size
        ymin = self.ymin - size
        xmax = self.xmax + size
        ymax = self.ymax + size
        bbox = type(self)(xmin, ymin, xmax, ymax, self.epsg)
        return bbox

    def enlarge_to_grid(self, size):
        xmin = floor(self.xmin / size) * size
        ymin = floor(self.ymin / size) * size
        xmax = ceil(self.xmax / size) * size
        ymax = ceil(self.ymax / size) * size
        bbox = type(self)(xmin, ymin, xmax, ymax, self.epsg)
        return bbox

    @classmethod
    def from_geom(cls, geom, epsg):
        (xmin, xmax, ymin, ymax) = geom.GetEnvelope()
        bbox = cls(xmin, ymin, xmax, ymax, epsg)
        return bbox

    def to_geom(self):
        ring_geom = ogr.Geometry(ogr.wkbLinearRing)
        ring_geom.AddPoint(self.xmin, self.ymin)
        ring_geom.AddPoint(self.xmax, self.ymin)
        ring_geom.AddPoint(self.xmax, self.ymax)
        ring_geom.AddPoint(self.xmin, self.ymax)
        ring_geom.AddPoint(self.xmin, self.ymin)
        geom = ogr.Geometry(ogr.wkbPolygon)
        geom.AddGeometry(ring_geom)
        geom.FlattenTo2D()
        return geom

    def transform(self, dest_epsg):
        """Transform the instance to dest_epsg coordinate system."""
        if self.epsg == dest_epsg:
            return self

        # Create a new instance with destination epsg.
        dest_geom = transform_geom(self.to_geom(), self.epsg, dest_epsg)
        (xmin, xmax, ymin, ymax) = dest_geom.GetEnvelope()
        dest_bbox = type(self)(xmin, ymin, xmax, ymax, dest_epsg)
        return dest_bbox

    def __repr__(self):
        return "{:s}({:f}, {:f}, {:f}, {:f}, epsg={:d})".format(type(self).__name__,
                                                                self.xmin, self.ymin, self.xmax, self.ymax,
                                                                self.epsg)
                                                                
                                                                
                                                                
def get_sitecode_aoiwkt(geom_info, aoi_epsg, TONDOR_CONNECTION_PARAMS):
    #################### geometry extent and pixel ###############################
    log.debug("Aoi wkt kwargs {}".format(geom_info))
    if type(geom_info) == list:
       sitecodes = geom_info
       log.debug("tiles given as list: {}".format(sitecodes))
    elif str(geom_info).endswith('.gpkg'):
       log.debug("Geo package file given as input. Finding tiles from processing gpkg files to process")
       sitecodes, composite_sitecodes = get_sitecode_from_aoiwkt_parse(geom_info, aoi_epsg)
    elif "polygon" in geom_info.lower():
       log.debug("Extent given. Finding tiles from processing gpkg files to process")
       sitecodes, composite_sitecodes = get_sitecode_from_aoiwkt_parse(geom_info, aoi_epsg)

    sitecode_geom_dict = {}
    for sitecode in sitecodes:
        sitecode_geom = sitecode_extent(sitecode, aoi_epsg)
        sitecode_geom_dict[sitecode] = sitecode_geom

    log.debug("aoi: {}".format(sitecode_geom_dict))
    return sitecode_geom_dict

def get_sitecode_from_aoiwkt_parse(aoi_wkt, t_srs):
    if aoi_wkt.endswith(".gpkg"):
       log.debug("aoi is specified as an gpkg file")
       aoi_ds = ogr.Open(aoi_wkt)
       aoi_lyr = aoi_ds.GetLayer()
       aoi_feat = aoi_lyr.GetNextFeature()
       aoi_geom = aoi_feat.GetGeometryRef()
       aoi_geom_wkt = aoi_geom.ExportToWkt()
       aoi_srs = aoi_lyr.GetSpatialRef()
       aoi_epsg = aoi_srs.GetAttrValue('AUTHORITY', 1)
       log.debug("Espg of input gpkg file: {}".format(aoi_epsg))

       aoi_geom = get_aoi_geometry(aoi_wkt, int(aoi_epsg))
       if aoi_geom["status"] == "ERROR":
          logger.error(aoi_geom["message"])
       else:
          aoi_geom = aoi_geom["output"]

       log.debug("aoi_geom: {}".format(aoi_geom))
    else:
       aoi_geom = aoi_wkt
    if True:
       compositing_grid = get_grid_file(t_srs)
       if compositing_grid["status"] == "OK":
          log.debug("grid geopackage:{}".format(compositing_grid["output"]))
          compositing_squares = get_composite_squares(aoi_geom, compositing_grid["output"])
    return compositing_squares


def get_composite_squares(aoi_geom, grid_geopackage):
    '''
    Return list of dictionaries - compositing squares in target Spatial Reference System.
    :param aoi_geom:
    :param grid_geopackage:
    :return:
    '''
    aoi_geom_inner = ogr.CreateGeometryFromWkt(aoi_geom).Buffer(-1)

    # output dictionary
    composite_squares = list()

    # get grid geopackage layer
    grid_ds = ogr.Open(grid_geopackage)
    grid_lyr = grid_ds.GetLayer()
    aoi_geom = ogr.CreateGeometryFromWkt(aoi_geom)
    grid_lyr.SetSpatialFilter(aoi_geom)
    feat = grid_lyr.GetNextFeature()

    while feat is not None:
        feat_geom = feat.GetGeometryRef().Buffer(-1)

        # create little inner buffer to exclude neighbour squares
        if feat_geom.Intersects(aoi_geom_inner):

            # feat = grid_lyr.GetNextFeature()
            composite_square = {"id": feat.GetField("id"),
                                "sitecode":feat.GetField("sitecode"),
                                "xmin": feat.GetField("xmin"),
                                "xmax": feat.GetField("xmax"),
                                "ymin": feat.GetField("ymin"),
                                "ymax": feat.GetField("ymax"),
                                "sen2_tiles": feat.GetField("sen2_tiles").split(","),
                                "ls_tiles": feat.GetField("ls_tiles").split(","),
                                "sen1_orbits": feat.GetField("sen1_orb").split(",")}
            composite_squares.append(composite_square)
        feat = grid_lyr.GetNextFeature()
    # Sort the results by id.
    composite_squares = sorted(composite_squares, key=lambda sq: sq["sitecode"])
    sitecodes = [composite_square["sitecode"] for composite_square in composite_squares]
    return sitecodes, composite_squares

def tile_aoi(geom_wkt):
    """
    Check if aoi is large enough to split into tiles (larger than 4 compositing tiles).
    :param geom_wkt: aoi geometry wkt
    :return: True in case of large aoi; False in case of small aoi
    """
    geom = ogr.CreateGeometryFromWkt(geom_wkt)
    area = geom.GetArea()
    if area > 9e8:
        return True
    else:
        return False

def get_grid_file(epsg_code):
    """
    Get absolute path to compositing grid file.
    :param epsg_code: EPSG code of target Spatial Reference System.
    :return: absolute path to compositing grid file.
    """
    gridfile = os.path.abspath(os.path.join("/tondor/tiles_gpkgfiles", "{0}_withsitecode.gpkg".format(epsg_code)))
    if os.path.isfile(gridfile):
        return {"status": "OK",
                "output": gridfile}
    else:
        return {"status": "ERROR",
                "message": "Target SRS specified with EPSG code: {0} either does not exist or is not currently supported.".format(epsg_code)}

def get_aoi_geometry(aoi_file, epsg_code):
    """
    Get Union geometry WKT from vector spatial data file.
    :param aoi_file: file path to vector spatial data file (e.g.: .shp, .geojson, .gpkg...)
    :param epsg_code: EPSG code of target SRS (e.g.: 5514 for S-JTSK, 4326 for WGS-84...)
    :return: WKT of union geometry
    """

    if not os.path.isfile(aoi_file):
        return {"status": "ERROR",
                "message": "AOI file does not exist."}

    ds = ogr.Open(aoi_file)
    if ds is None:
        return {"status": "ERROR",
                "message": "AOI file is not in supported format."}
    lyr = ds.GetLayer()
    s_srs = lyr.GetSpatialRef()
    t_srs = osr.SpatialReference()
    t_srs.ImportFromEPSG(epsg_code)
    transform = osr.CoordinateTransformation(s_srs, t_srs)

    if lyr.GetFeatureCount() == 1:

        feat = lyr.GetNextFeature()
        geom = feat.GetGeometryRef()
        geom.Transform(transform)
        return {"status": "OK",
                "output": geom.ExportToWkt()}
    else:
        feat = lyr.GetNextFeature()
        geom = feat.GetGeometryRef()
        geom.Transform(transform)
        geom = geom.Clone()
        feat = lyr.GetNextFeature()

        while feat is not None:
            geom_next = feat.GetGeometryRef()
            geom_next.Transform(transform)
            geom = geom.Union(geom_next)
            feat = lyr.GetNextFeature()
        return {"status": "OK",
                "output": geom.ExportToWkt()}

def sitecode_extent(sitecode,  epsg_code):
    gridfile = os.path.abspath(os.path.join("/tondor/tiles_gpkgfiles", "{0}_withsitecode.gpkg".format(epsg_code)))
    processing_tiles_ds = ogr.Open(gridfile)
    processing_tiles_lyr = processing_tiles_ds.GetLayer()
    processing_tiles_srs = processing_tiles_lyr.GetSpatialRef()
    processing_tiles_epsg = processing_tiles_srs.GetAttrValue('AUTHORITY', 1)

    for feature in processing_tiles_lyr:

        if feature['sitecode'] == sitecode:
           return feature.geometry().ExportToWkt()                                                                
                                                                
                                                                
