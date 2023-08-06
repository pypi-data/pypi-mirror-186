#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import logging
import subprocess
import time
import glob
import os
import calendar
import shutil

from datetime import datetime
from datetime import timedelta
from pathlib import Path
from shutil import copy
from shutil import copytree
from tempfile import mkdtemp

from .geo import BoundingBox
try:
    import ogr
except ImportError:
    from osgeo import ogr

try:
    import osr
except ImportError:
    from osgeo import osr

try:
    import gdal
except ImportError:
    from osgeo import gdal

import numpy as np
from shapely.geometry import box

KEEP_FILENAME = ".tondor_keep"


log = logging.getLogger(__name__)

def run_subprocess(args, work_dir):
    log.debug("Calling subprocess, args={:s}.".format(repr(args)))
    cmd_output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log.info("Subprocess exited with code {:d}, args={:s}.".format(cmd_output.returncode, repr(args)))

def log_subprocess(args, work_dir, log_filepath, timeout=None):
    log.debug("Calling subprocess: {:s}, logging to {:s}.".format(repr(args), str(log_filepath)))
    with open(str(log_filepath), "at", encoding="utf-8") as logf:
        logf.write("\n{:s} Calling subprocess: {:s}.\n".format(datetime.utcnow().isoformat()[:23], repr(args)))
        logf.flush()
        pr = subprocess.run(args, cwd=work_dir, stdout=logf, stderr=logf, timeout=timeout, check=False)
        log.info("Subprocess exited with code {:d}, args={:s}.".format(pr.returncode, repr(args)))
        logf.write("\n{:s} Subprocess exited with code {:d}.\n".format(datetime.utcnow().isoformat()[:23], pr.returncode))
    pr.check_returncode()


def read_tool_def(tool_def_filepath):
    tool_def = json.loads(tool_def_filepath.read_text())
    return tool_def


def set_input_param(job_step_params, ident, value):
    for input_p in job_step_params["parameters"]:
        if input_p["ident"] == ident:
            input_p["value"] = value


def get_input_param(job_step_params, ident):
    for input_p in job_step_params["parameters"]:
        if input_p["ident"] == ident:
            return input_p["value"]
    return None


def generate_yearmonths(ym_from, ym_till):
    year = int(ym_from[:4])
    month = int(ym_from[4:6])
    yearmonths = []
    while True:
        yearmonth = "{:d}{:02}".format(year, month)
        if yearmonth > ym_till:
            break
        yearmonths.append(yearmonth)
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return yearmonths

#################################################################################################
#################################################################################################
def yearmonth_parse(yearmonth):
    start_final_date = [ym.strip() for ym in yearmonth.split("-")]
    start_date = datetime.strptime(start_final_date[0],"%Y%m%d")
    final_date   = datetime.strptime(start_final_date[1],"%Y%m%d")
    start_date_basename = start_date.strftime("%Y%m%d")
    final_date_basename = final_date.strftime("%Y%m%d")
    return yearmonth, start_date, final_date, start_date_basename, final_date_basename

def generate_timeperiod_monthly(year, month):
    year = int(year)
    month = int(month)
    startmonth = month
    endmonth = month
    enddate = calendar.monthrange(year, endmonth)[1]

    yearmonth_start = "{:d}{:02}01".format(year, startmonth)
    yearmonth_end = "{:d}{:02}{:02}".format(year, month, enddate)
    yearmonth_timeperiod = str(yearmonth_start) + '-' + str(yearmonth_end)

    return yearmonth_timeperiod

def generate_timeperiod_quaterly(year, month):
    startmonth = month
    endmonth = month + 2
    enddate = calendar.monthrange(year, endmonth)[1]

    yearmonth_start = "{:d}{:02}01".format(year, startmonth)
    yearmonth_end = "{:d}{:02}{:02}".format(year, endmonth, enddate)
    yearmonth_timeperiod = str(yearmonth_start) + '-' + str(yearmonth_end)

    return yearmonth_timeperiod


def generate_quarters(year_from, year_till):
    year = int(year_from)
    quarters = [1, 2, 3, 4]
    yearquarters = []
    while True:
        for quarter in quarters:
            yearquarter = "{:d}Q{:d}".format(year, quarter)
            yearquarters.append(yearquarter)
        if year > year_till:
            break
    return yearquarters


def month_range(yearmonth):
    year = int(yearmonth[0:4])
    month = int(yearmonth[4:6])
    start_date = datetime(year, month, 1)
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    final_date = datetime(year, month, 1)
    return (start_date, final_date)


def quarter_range(yearquarter):
    year = int(yearquarter[0:4])
    quarter_index = int(yearquarter[5:6]) - 1
    quarter_start_months = [1, 4, 7, 10]
    start_month = quarter_start_months[quarter_index]
    start_date = datetime(year, start_month, 1)

    quarter_final_months = [3, 6, 9, 12]
    final_month = quarter_final_months[quarter_index]
    if final_month == 12:
        final_month = 1
        year += 1
    else:
        final_month += 1
    final_date = datetime(year, final_month, 1)
    return (start_date, final_date)

#################################################################################################
#################################################################################################
def generate_yearmonth_monthly(year, month):
    startmonth = month
    endmonth = month
    enddate = calendar.monthrange(year, endmonth)[1]

    yearmonth_start = "{:d}{:02}01".format(year, startmonth)
    yearmonth_end = "{:d}{:02}{:02}".format(year, month, enddate)
    yearmonth_timeperiod = str(yearmonth_start) + '-' + str(yearmonth_end)

    return yearmonth_timeperiod

def generate_yearmonth_quaterly(year, month):
    startmonth = month
    endmonth = month + 2
    enddate = calendar.monthrange(year, endmonth)[1]

    yearmonth_start = "{:d}{:02}01".format(year, startmonth)
    yearmonth_end = "{:d}{:02}{:02}".format(year, endmonth, enddate)
    yearmonth_timeperiod = str(yearmonth_start) + '-' + str(yearmonth_end)

    return yearmonth_timeperiod

def generate_yearmonth_monthbin(year, month, monthbin):
    startmonth = month
    endmonth = month + monthbin
    enddate = calendar.monthrange(year, endmonth)[1]

    yearmonth_start = "{:d}{:02}01".format(year, startmonth)
    yearmonth_end = "{:d}{:02}{:02}".format(year, endmonth, enddate)
    yearmonth_timeperiod = str(yearmonth_start) + '-' + str(yearmonth_end)

    return yearmonth_timeperiod

def generate_quarters_or_yearmonths(year_from, year_till, monthbins=None):
    q_or_ym = []

    year = int(str(year_from)[:4])
    month = int(str(year_from)[4:6])

    end_year = int(str(year_till)[:4])
    end_month = int(str(year_till)[4:6])

    while True:
        if year <= 2015:
            yearmonth = generate_yearmonth_quaterly(year, month)
            month = month + 3
        else:
            if monthbins is None:
                yearmonth = generate_yearmonth_monthly(year, month)
                month = month + 1
            if monthbins is not None:
                q_or_ym_bins = []
                for monthbin in monthbins:
                    yearmonth = generate_yearmonth_monthbin(year, month, monthbin - 1)
                    q_or_ym_bins.append(yearmonth)
                    month = month + monthbin

                    if month > 12:
                        year += 1
                        month = 1

                    if year == end_year and month > end_month:
                        return q_or_ym_bins
                return q_or_ym_bins
        q_or_ym.append(yearmonth)

        if year == end_year and month > end_month:
            break

        if month > 12:
            year += 1
            month = 1
    return q_or_ym
#################################################################################################
#################################################################################################
def archive_results(tmp_dir_tpl, src_dst_pairs):
    # Create temporary directory dedicated for this function call.
    tmp_dir = Path(mkdtemp(prefix="{:s}.".format(tmp_dir_tpl.name), suffix=".d", dir=tmp_dir_tpl.parent))

    # Create all destination directories.
    dst_dirs = [dst_path.parent for (src_path, dst_path) in src_dst_pairs]
    dst_dirs = set(dst_dirs)
    dst_dirs = sorted(dst_dirs, key=str)
    for dst_dir in dst_dirs:
        # Before any move begins, the result directory should have updated timestamp.
        # Such updated timestamp should eliminate a race condition
        # when some other process is just removing empty directories.
        # While mkdir() does not update the timestamp if the directory already exists,
        # we must update the timestamp explicitly.
        keep_filepath = dst_dir.joinpath(KEEP_FILENAME)
        try:
            keep_filepath.touch(exist_ok=True)
            keep_filepath.unlink()
        except FileNotFoundError:
            pass
        dst_dir.mkdir(parents=True, exist_ok=True)

    # Copy all source items into temporary directory.
    #
    # To ensure two items with the same name do not collide,
    # give all the items in temporary directory special suffix.
    tmp_dst_pairs = []
    for (i, (src_path, dst_path)) in enumerate(src_dst_pairs, start=1):
        tmp_path = tmp_dir.joinpath("{:s}.{:d}".format(src_path.name, i))
        if src_path.is_dir():
            copytree(str(src_path), str(tmp_path))
            log.info("Directory tree {:s} has been copied to temporary {:s}."
                     .format(str(src_path), str(tmp_path)))
        else:
            copy(str(src_path), str(tmp_path))
            log.info("File {:s} has been copied to temporary {:s}."
                     .format(str(src_path), str(tmp_path)))
        tmp_dst_pairs.append((tmp_path, dst_path))

    # Move already copied items into final destination.
    for tmp_path, dst_path in tmp_dst_pairs:
        tmp_path.rename(dst_path)
        log.info("Temporary file/dir {:s} has been moved to final {:s}."
                 .format(str(tmp_path), str(dst_path)))

    # Remove the temporary directory.
    tmp_dir.rmdir()
    log.info("Temporary directory {:s} has been removed.".format(str(tmp_dir)))

#################################################################################################
#################################################################################################
#
# Utility functions for detecting missing L2A scenes.
#

def parse_sentinel2_name(name):
    if name.endswith(".SAFE"):
        name = name[:-5]
    name_parts = name.split("_")
    info = {"name": name,
            "mission": name_parts[0][2],
            "level": name_parts[1][3:].upper(),
            "obs_date": datetime.strptime(name_parts[2], "%Y%m%dT%H%M%S"),
            "baseline": name_parts[3][1:],
            "rel_orbit": name_parts[4][1:],
            "tile": name_parts[5][1:],
            "produced_date": datetime.strptime(name_parts[6], "%Y%m%dT%H%M%S"),
            "satellite": "sentinel-2"}
    return info


def pair_sentinel2_scene_infos(scene_infos):
    # Build table of paired L1C and L2A items.
    scene_idx = {}
    for scene_info in scene_infos:
        scene_key = (scene_info["obs_date"], scene_info["tile"])
        if scene_key not in scene_idx:
            scene_idx[scene_key] = ([], [])
        if scene_info["level"] == "L1C":
            scene_idx[scene_key][0].append(scene_info)
        elif scene_info["level"] == "L2A":
            scene_idx[scene_key][1].append(scene_info)
        else:
            log.warning("Unknown level {:s} of the scene {:s}.".format(scene_info["level"], scene_info["name"]))

    # Sort the items within a pair by produced_date property.
    for (l1c, l2a) in scene_idx.values():
        l1c.sort(key=lambda info: info["produced_date"])
        l2a.sort(key=lambda info: info["produced_date"])

    return scene_idx


def filter_cloud_cover(scene_idx, max_cloud_cover):
    new_scene_idx = {}
    for (key, (l1c, l2a)) in scene_idx.items():
        item_cloud_cover = max(info["cloud_cover"] for info in [*l1c, *l2a])
        if item_cloud_cover > max_cloud_cover:
            key_date, tile = key
            log.debug("All items of the date {:s} and tile {:s} has been removed,"
                      " while the cloud cover {:f} is above {:f}."
                      .format(key_date.isoformat(), tile, item_cloud_cover, max_cloud_cover))
        else:
            new_scene_idx[key] = (l1c, l2a)
    return new_scene_idx


def compile_sentinel2level2a_glob(l1c_name):
    name_parts = l1c_name.split("_")
    mission = name_parts[0]
    obs_date = name_parts[2]
    tile = name_parts[5]
    year = obs_date[:4]
    month = obs_date[4:6]
    day = obs_date[6:8]
    name_glob = "{:s}_MSIL2A_{:s}_*_*_{:s}_*.SAFE".format(mission, obs_date, tile)
    path = Path("Sentinel2", year, month, day)
    return path, name_glob


def compile_sentinel2level2a_eodata_glob(l1c_name):
    path, name_glob = compile_sentinel2level2a_glob(l1c_name)
    path = Path(str(path).replace("Sentinel2/", "Sentinel-2/MSI/L2A/"))
    return path, name_glob

#################################################################################################
#################################################################################################
def compile_monthly_composite_filepath(archive_root, year, sitecode, month):
    countrycode = sitecode[0:2]
    yearmonth = "{:04d}{:02d}".format(int(year), month)
    startdate, enddate = month_range(yearmonth)
    # month_range returns (first day of the month, first day of the next month).
    # OPT composite naming convention uses (first day of the month, last day of the month).
    startdate = startdate.strftime("%Y%m%d")
    enddate = (enddate - timedelta(hours=12)).strftime("%Y%m%d")
    basename = "MTC_{startdate}_{enddate}_{sitecode}_OPT.tif"
    basename = basename.format(startdate=startdate, enddate=enddate, sitecode=sitecode)
    return archive_root.joinpath(str(year), countrycode, sitecode, "MTC", "OPT", basename)


def compile_quarterly_composite_filepath(archive_root, year, sitecode, quarter):
    countrycode = sitecode[0:2]
    yearquarter = "{:04d}{:02d}".format(int(year), quarter)
    log.debug(yearquarter)
    startdate, enddate = quarter_range(yearquarter)
    # month_range returns (first day of the month, first day of the next month).
    # OPT composite naming convention uses (first day of the month, last day of the month).
    startdate = startdate.strftime("%Y%m%d")
    enddate = (enddate - timedelta(hours=12)).strftime("%Y%m%d")
    basename = "MTC_{startdate}_{enddate}_{sitecode}_OPT.tif"
    basename = basename.format(startdate=startdate, enddate=enddate, sitecode=sitecode)
    return archive_root.joinpath(str(year), countrycode, sitecode, "MTC", "OPT", basename)

def locate_training_polygons(training_polygon_parent_path, year, bioregion, training_epsg):
    year = int(year)
    training_polygons_basename = "trainingdata_{bioregion}_{year}_{epsg}.gpkg".format(
        bioregion=bioregion, year=year, epsg=training_epsg)
    log.debug("looking for training polygon with name: {}".format(training_polygons_basename))
    training_polygons_filepath = Path(training_polygon_parent_path).joinpath(bioregion, str(year), "training_data", training_polygons_basename)
    log.debug("looking for training polygon in: {}".format(training_polygons_filepath))
    return training_polygons_filepath

#################################################################################################
#################################################################################################
def find_file_in_archives(relative_path, archive_roots, error_on_missing=True):
    for archive_root in archive_roots:
        log.debug("Searching for {:s} in {:s}".format(str(relative_path), str(archive_root)))
        filepath = archive_root.joinpath(relative_path)
        if filepath.is_file():
            log.info("Found {:s} at {:s}".format(filepath.name, str(filepath)))
            return filepath
    if error_on_missing:
        # If we got up to here, then nothing is found and we must raise FileNotFoundError.
        msg = "Expected file {:s} was not found in any of the archives.".format(str(relative_path))
        log.error(msg)
        raise FileNotFoundError

def find_files_in_archives_pattern(relative_path, archive_roots):
    filepaths = []
    for archive_root in archive_roots:
        log.debug("Searching for {:s} in {:s}".format(str(relative_path), str(archive_root)))
        path_fullpath = archive_root.joinpath(relative_path)

        filepath = glob.glob(str(path_fullpath))
        if len(filepath)>0:
           log.info("Found {} in {}".format(filepath, archive_root))
           filepaths.extend(filepath)
    log.debug("Found the following opt composite files:{}".format(filepaths))
    return filepaths

def copy_files_from_archive(scrfiles_path, dst_folder):
    if type(scrfiles_path) == list:
        for scrfile_path_item in scrfiles_path:
            if 's3archive' in str(scrfile_path_item):
                pass
            else:
                copied_path = Path(dst_folder).joinpath(Path(scrfile_path_item).name)
                copy_singlefile_from_archive(scrfile_path_item, copied_path)
    else:
        copied_path = Path(dst_folder).joinpath(Path(scrfiles_path).name)
        copy_singlefile_from_archive(scrfiles_path, copied_path)

def copy_singlefile_from_archive(scrfile_path, dstfile_path):
    shutil.copy(str(scrfile_path), str(dstfile_path))
#################################################################################################
#################################################################################################
def mosaic_tifs(tile_filepaths, mosaic_filepath):
    if mosaic_filepath.is_file():
        mosaic_filepath.unlink()
    args = ["gdal_merge.py",
            "-co", "TILED=YES",
            "-co", "COMPRESS=DEFLATE",
            "-n", "0",
            "-a_nodata", "0",
            "-o", str(mosaic_filepath),
            "-pct"] + [str(fp) for fp in tile_filepaths]

    cmd_output = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log.debug(f"exit code {cmd_output.returncode} --> {args}")

def read_raster_info(raster_filepath):
    ds = gdal.Open(str(raster_filepath))

    RasterXSize = ds.RasterXSize
    RasterYSize = ds.RasterYSize
    gt = ds.GetGeoTransform()
    ulx_raster = gt[0]
    uly_raster = gt[3]
    lrx_raster = gt[0] + gt[1] * ds.RasterXSize + gt[2] * ds.RasterYSize
    lry_raster = gt[3] + gt[4] * ds.RasterXSize + gt[5] * ds.RasterYSize
    imagery_extent_box = box(lrx_raster, uly_raster, ulx_raster, lry_raster)

    xmin = gt[0]
    ymax = gt[3]
    pixel_width = gt[1]
    yres = gt[5]

    projection = ds.GetProjection()
    datatype = ds.GetRasterBand(1).DataType
    n_bands = ds.RasterCount
    epsg = ds.GetSpatialRef().GetAuthorityCode(None)
    ds = None
    return (xmin, ymax, RasterXSize, RasterYSize, pixel_width, projection, epsg, datatype, n_bands, imagery_extent_box)


def clip_project_multibandraster_toextent(composite_filepath, warped_filepath, target_epsg, xmin, xmax, ymin, ymax, work_dir, method ='bilinear'):
    cmd = ["gdalwarp",
           "-t_srs", "EPSG:{}".format(target_epsg),
           "-te",str(xmin),str(ymin),str(xmax),str(ymax),
           "-r", method,
           "-co", "COMPRESS=DEFLATE",
           str(composite_filepath),
           str(warped_filepath)
           ]
    run_subprocess(cmd, work_dir)

def reproject_multibandraster_toextent(composite_filepath, warped_filepath, target_epsg, pixel_size, xmin, xmax, ymin, ymax, work_dir, method ='bilinear'):

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

def reproject_multibandraster_toextent_withnodata(composite_filepath, warped_filepath, target_epsg, pixel_size, xmin, xmax, ymin, ymax, work_dir, nodata_value, method ='bilinear'):

    cmd = ["gdalwarp",
           "-t_srs", "EPSG:{}".format(target_epsg),
           "-tr", str(pixel_size), str(pixel_size),
           "-te",str(xmin),str(ymin),str(xmax),str(ymax),
           "-r", method,
           "-ot", "Float32",
           "-dstnodata", nodata_value,
           "-co", "COMPRESS=DEFLATE",
           str(composite_filepath),
           str(warped_filepath)
           ]
    run_subprocess(cmd, work_dir)

def reproject_multibandraster(composite_filepath, warped_filepath, target_epsg, pixel_size, work_dir, method ='bilinear'):

    cmd = ["gdalwarp",
           "-t_srs", "EPSG:{}".format(target_epsg),
           "-tr", str(pixel_size), str(pixel_size),
           "-r", method,
           "-co", "COMPRESS=DEFLATE",
           str(composite_filepath),
           str(warped_filepath)
           ]
    run_subprocess(cmd, work_dir)


#################################################################################################
#################################################################################################
def locate_optcomposites(archive_roots, year, sitecode, training_selection, site_selection):
    # training_selection: indices of months that should be used for the training, typically 111111111111.
    # site_selection: indices of months with suitable composites for the given site, e.g.  001111111110.
    # site_selection can have four digits or 12 digits
    # Constructs expected paths to OPT composites for a given year, site and selection.
    # Months with unsuitable composite are given the value of path=None.
    log.debug("Searching for OPT composites from site={}, year={}, training_selection={}, site_selection={}"
              .format(sitecode, year, training_selection, site_selection))
    countrycode = sitecode[0:2]
    num_timesteps = len(training_selection)
    if len(site_selection) != num_timesteps:
        raise Exception("training_selection and site_selection length must have equal number of timesteps.")

    log.info("Training selection is {:s}".format(repr(training_selection)))
    log.info("Site selection is {:s}".format(repr(site_selection)))

    # Check length of the site selection depending on the year.
    if int(year) >= 2016 and num_timesteps != 12:
        raise Exception("Number of selection items for sitecode {:s} is {:d}, but it should be 12.".format(sitecode, len(site_selection)))
    if int(year) <= 2015 and num_timesteps != 4:
        raise Exception("Number of selection items for sitecode {:s} is {:d}, but it should be 12.".format(sitecode,len(site_selection)))

    optcomposite_filepaths = []
    training_timesteps = []
    site_timesteps = []

    # The site selection is a 12-character or 4-character string of ones and zeros, e.g. 011111100100.
    # The character '1' means that the month is selected.
    # The character '0' means that the month is not selected.
    for ts_index, ts_status in enumerate(training_selection):
        if int(ts_status) == 1:
            training_timesteps.append(ts_index + 1)
    log.info("training_months or quarters: {}.".format(repr(training_timesteps)))

    # Here the indexes of the timesteps from which values should be taken are used.
    for timestep_index, timestep_status in enumerate(site_selection):
        if int(timestep_status) == 1:
            site_timesteps.append(timestep_index + 1)
    log.info("site_months or quarters: {}.".format(repr(site_timesteps)))

    for timestep in training_timesteps:
        if timestep in site_timesteps:
            composite_filepath = None
            for archive_root in archive_roots:
                if num_timesteps == 12:
                    composite_filepath = compile_monthly_composite_filepath(archive_root, year, sitecode, timestep)
                else:
                    composite_filepath = compile_quarterly_composite_filepath(archive_root, year, sitecode, timestep)
                log.info("Searching for composite at {:s}.".format(str(composite_filepath)))
                if composite_filepath.is_file():
                    # If composite is found, then add it to list.
                    log.info("Found composite for site {:s}, timestep {:d} at {:s}"
                             .format(sitecode, timestep, str(composite_filepath)))
                    optcomposite_filepaths.append(composite_filepath)
                    break
            if composite_filepath is None:
                log.error("No composite was found for site {:s}, selected timestep {:d}".format(sitecode, timestep))
                raise FileNotFoundError
        else:
            # If an OPTCOMPOSITE is not in selection then it is set to NONE.
            log.info("Set optcomposite for site {:s}, timestep {:d} to None.".format(sitecode, timestep))
            optcomposite_filepaths.append(None)

    log.info("selected OPT composites for site={}, year={}, training_selection={}, site_selection={} are:"
             .format(sitecode, year, training_selection, site_selection))
    for timestep, fp in enumerate(optcomposite_filepaths):
        log.info("timestep: {:d}, composite: {:s}".format(timestep, str(fp)))
    return training_timesteps, optcomposite_filepaths


def locate_sarcomposites(archive_roots, year, sitecode):
    # Constructs expected paths to SAR composites for a given year and site.
    countrycode = sitecode[0:2]
    composite_filepaths = []
    months = [m for m in range(1, 13)]
    for month in months:
        # Get the start date and end date of a given yearmonth.
        yearmonth = "{:04d}{:02d}".format(int(year), month)
        startdate, enddate = month_range(yearmonth)
        startdate = startdate.strftime("%Y%m%d")
        enddate = enddate.strftime("%Y%m%d")
        composite_basename = "MTC_{startdate}_{enddate}_{sitecode}_SAR.tif"
        composite_basename = composite_basename.format(startdate=startdate, enddate=enddate, sitecode=sitecode)
        composite_path = None
        for archive_root in archive_roots:
            base_dir = archive_root.joinpath(str(year), countrycode, sitecode, "MTC", "SAR")
            log.debug("Searching for {:s} at {:s}".format(composite_basename, str(base_dir)))
            composite_path = base_dir.joinpath(composite_basename)
            if composite_path.is_file():
                log.debug("Found {:s}".format(str(composite_path)))
                break
        if composite_path is None:
            log.warning("No SAR composite for sitecode={:s}, yearmonth={:s} found.".format(sitecode, yearmonth))
        composite_filepaths.append(composite_path)
    if len(composite_filepaths) != 12:
        raise Exception("Some SAR composites are missing for sitecode={:s} and year={:s}. Expected count is 12, number of found composites is {:d}."
                        .format(sitecode, str(year), len(composite_filepaths)))
    return composite_filepaths

#################################################################################################
#################################################################################################
def copy_file_from_s3(s3path, dstpath, retries, timeout, sleep_time):
    # FIXME use better mapping of object name from the mapped S3 path.
    object_name = str(s3path).replace("/s3archive/", "")
    if not object_name.startswith("output"):
        object_name = "output/" + object_name

    cmd = ["swift", "download",
           "--output", str(dstpath),
           "cop4n2k-archive", str(object_name)]
    downloaded = False
    try:
        log.debug(" ".join(cmd))
        subprocess.run(cmd, timeout=timeout, check=True)
        downloaded = True
        log.info("Downloaded cop4n2k-archive:{} to {}".format(object_name, dstpath))
    except Exception as ex:
        log.warning(str(ex))
        for retry in range(retries):
            log.warning("retrying download after {}s ..".format(sleep_time))
            time.sleep(sleep_time)
            try:
                log.debug(" ".join(cmd))
                subprocess.run(cmd, timeout=timeout, check=True)
                log.info("Downloaded cop4n2k-archive:{} to {}".format(object_name, dstpath))
                downloaded = True
                break
            except Exception as ex:
                log.warning(str(ex))
                continue
    if downloaded:
        return dstpath
    else:
        log.warning("Object cop4n2k-archive:{} could not be downloaded.".format(object_name))
        return None

#################################################################################################
#################################################################################################

def get_sitecode_aoiwkt(geom_info, aoi_epsg, gpkg_folder_path):
    #################### geometry extent and pixel ###############################
    log.debug("Aoi wkt kwargs {}".format(geom_info))
    if type(geom_info) == list:
       sitecodes = geom_info
       log.debug("tiles given as list: {}".format(sitecodes))
    elif str(geom_info).endswith('.gpkg'):
       log.debug("Geo package file given as input. Finding tiles from processing gpkg files to process")
       sitecodes, composite_sitecodes = get_sitecode_from_aoiwkt_parse(geom_info, aoi_epsg, gpkg_folder_path)
    elif "polygon" in geom_info.lower():
       log.debug("Extent given. Finding tiles from processing gpkg files to process")
       sitecodes, composite_sitecodes = get_sitecode_from_aoiwkt_parse(geom_info, aoi_epsg, gpkg_folder_path)
    log.debug("tiles: {}".format(sitecodes))

    sitecode_geom_dict = {}
    for sitecode in sitecodes:
        sitecode_geom = sitecode_extent(sitecode, aoi_epsg, gpkg_folder_path)
        sitecode_geom_dict[sitecode] = sitecode_geom

    log.debug("aoi: {}".format(sitecode_geom_dict))
    return sitecode_geom_dict

def get_sitecode_from_aoiwkt_parse(aoi_wkt, t_srs, gpkg_folder_path):
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
          log.error(aoi_geom["message"])
       else:
          aoi_geom = aoi_geom["output"]

       log.debug("aoi_geom: {}".format(aoi_geom))
    else:
       aoi_geom = aoi_wkt
    if True:
       compositing_grid = get_grid_file(t_srs, gpkg_folder_path)
       if compositing_grid["status"] == "OK":
          log.debug("grid geopackage:{}".format(compositing_grid["output"]))
          sitecodes, composite_squares = get_composite_squares(aoi_geom, compositing_grid["output"])
    return sitecodes, composite_squares


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

def get_grid_file(epsg_code, gpkg_folder_path):
    """
    Get absolute path to compositing grid file.
    :param epsg_code: EPSG code of target Spatial Reference System.
    :return: absolute path to compositing grid file.
    """
    gridfile = os.path.abspath(os.path.join(str(gpkg_folder_path), "{0}_withsitecode.gpkg".format(epsg_code)))
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

def sitecode_extent(sitecode,  epsg_code, gpkg_folder_path):
    # fix me:
    if 'CZTILE' in str(sitecode) and int(epsg_code) == 32633:
       gridfile = os.path.abspath(os.path.join(str(gpkg_folder_path), "CZGRID.gpkg"))
    elif 'CZTILE' in str(sitecode) and int(epsg_code) != 32633:
       log.error("sitecode has CZTILE while epsg is not 32633. check it.")
    else:
       gridfile = os.path.abspath(os.path.join(str(gpkg_folder_path), "{0}_withsitecode.gpkg".format(epsg_code)))

    processing_tiles_ds = ogr.Open(gridfile)
    processing_tiles_lyr = processing_tiles_ds.GetLayer()
    processing_tiles_srs = processing_tiles_lyr.GetSpatialRef()
    processing_tiles_epsg = processing_tiles_srs.GetAttrValue('AUTHORITY', 1)

    for feature in processing_tiles_lyr:

        if feature['sitecode'] == sitecode:
            xmin = feature['xmin']
            xmax = feature['xmax']
            ymin = feature['ymin']
            ymax = feature['ymax']
            b_box_instance = BoundingBox(xmin, ymin, xmax, ymax, epsg_code)
            b_box_instance_geom = b_box_instance.to_geom()
            return b_box_instance_geom.ExportToWkt()

#################################################################################################
#################################################################################################
def find_firstdate(days_interval, firstdate_giveninterval, acq_frequency):
    acq_date_ymd = firstdate_giveninterval.strftime("%Y%m%d")

    for interval_start in days_interval:
        interval_end = interval_start + timedelta(days=acq_frequency)
        interval_start_ymd = interval_start.strftime("%Y%m%d")
        interval_end_ymd = interval_end.strftime("%Y%m%d")
        if interval_start_ymd <= acq_date_ymd < interval_end_ymd:
            return interval_start

def get_sardateinterval(start_date, end_date, acq_frequency=None):

    MASTER_START_DATE = datetime(2015, 5, 1)

    if not acq_frequency:
        acq_frequency = 6

    days_interval_master = np.ndarray.tolist(
        np.arange(MASTER_START_DATE, end_date, timedelta(days=acq_frequency), dtype='datetime64[D]'))

    givendateinterval = np.ndarray.tolist(
        np.arange(start_date, end_date, timedelta(days=acq_frequency), dtype='datetime64[D]'))
    firstdate_giveninterval = givendateinterval[0]
    firstdate_timeperiod =  find_firstdate(days_interval_master, firstdate_giveninterval, acq_frequency)

    days_interval = np.ndarray.tolist(
        np.arange(firstdate_timeperiod, end_date, timedelta(days=acq_frequency), dtype='datetime64[D]'))

    return days_interval

#################################################################################################
#################################################################################################

class satellite_band():
    def __init__(self):
        self.landsat_band_lookup_table = {
            "landsat-9": {
                "coastal_aerosol": "SR_B1",
                "vis-b": "SR_B2",
                "vis-g": "SR_B3",
                "vis-r": "SR_B4",
                "nir": "SR_B5",
                "swir1": "SR_B6",
                "swir2": "SR_B7",
                "pan": "SR_B8",
                "cirrus": "SR_B9",
                "tir-10900": "SR_B10",
                "tir-12000": "SR_B11"
            },
            "landsat-8": {
                "coastal_aerosol": "SR_B1",
                "vis-b": "SR_B2",
                "vis-g": "SR_B3",
                "vis-r": "SR_B4",
                "nir": "SR_B5",
                "swir1": "SR_B6",
                "swir2": "SR_B7",
                "pan": "SR_B8",
                "cirrus": "SR_B9",
                "tir-10900": "SR_B10",
                "tir-12000": "SR_B11"
            },
            "landsat-7": {
                "vis-b": "SR_B1",
                "vis-g": "SR_B2",
                "vis-r": "SR_B3",
                "nir": "SR_B4",
                "swir1": "SR_B5",
                "swir2": "SR_B7",
                "tir-11450": "SR_B6"
            },
            "landsat-5": {
                "vis-b": "SR_B1",
                "vis-g": "SR_B2",
                "vis-r": "SR_B3",
                "nir": "SR_B4",
                "swir1": "SR_B5",
                "swir2": "SR_B7",
                "tir_11450": "SR_B6"
            },
            "landsat-4": {
                "vis_b": "SR_B1",
                "vis_g": "SR_B2",
                "vis_r": "SR_B3",
                "nir": "SR_B4",
                "swir1": "SR_B5",
                "swir2": "SR_B7",
                "tir_11450": "SR_B6"
            }
        }
        self.sentinel2_band_lookup_10m_table = {"vis-b": "B02_10m",
                                 "vis-g": "B03_10m",
                                 "vis-r": "B04_10m",
                                 "nir": "B08_10m"}

        self.sentinel2_band_lookup_20m_table = {"vis-b": "B02_20m",
                                 "vis-g": "B03_20m",
                                 "vis-r": "B04_20m",
                                 "re-705": "B05_20m",
                                 "re-740": "B06_20m",
                                 "re-781": "B07_20m",
                                 "nir": "B8A_20m",
                                 "swir1": "B11_20m",
                                 "swir2": "B12_20m"
                                 }

    def landsat_band_lookup(self, sat_label, band_label):
        return self.landsat_band_lookup_table[sat_label][band_label]

    def sentinel2_band_lookup(self, band_label, resolution):
        if resolution >= 20:
            band_expr = self.sentinel2_band_lookup_20m_table[band_label]
        else:
            try:
                band_expr = self.sentinel2_band_lookup_10m_table[band_label]
            except KeyError:
                band_expr = self.sentinel2_band_lookup_20m_table[band_label]

        return band_expr

    def satellite_band_check(self, band_label, satellites, resolution=20):
        for sat in satellites:
            if sat.startswith("landsat"):
                 if not band_label in self.landsat_band_lookup_table[sat].keys():
                    log.warning("{} doesnot have data for band {}".format(sat, band_label))
            elif sat.startswith("sentinel"):
                 if band_label in self.sentinel2_band_lookup_10m_table.keys() or self.sentinel2_band_lookup_20m_table.keys():
                    log.debug("{} has data for band {}".format(sat, band_label))
                 else:
                    log.warning("{} doesnot have data for band {}".format(sat, band_label))

    def satellite_bandlist_check(self, bandlist, satellites, resolution = 20):
        for band_label in bandlist:
            self.satellite_band_check(band_label, satellites, resolution)
