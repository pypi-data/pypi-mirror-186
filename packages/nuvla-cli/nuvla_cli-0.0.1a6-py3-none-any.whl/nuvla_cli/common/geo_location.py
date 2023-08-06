"""

"""
import re
import logging
from typing import List, Tuple
import random

import requests
import shapefile
from shapely.geometry import shape, Point
from rich import print
from nuvla_cli.nuvlaio.cli_api import CliApi as NuvlaAPI

from nuvla_cli.common.common import print_warning
from nuvla_cli.common.constants import (COUNTRIES_FILE_DBF, COUNTRIES_FILE_SHP,
                                        COUNTRIES_DBF_LINK, COUNTRIES_SHP_LINK,
                                        GEOLOCATION_PATH)

logger: logging.Logger = logging.getLogger(__name__)


def locate_nuvlaedge(nuvla: NuvlaAPI, location: Tuple, nuvlaedge_uuid: str):
    """

    :param nuvla:
    :param location:
    :param nuvlaedge_uuid:
    :return:
    """
    nuvla.edit(nuvlaedge_uuid, data={'location': location})


def get_countries_location_files():
    """
    If not existent, gathers the required files
    :return: None
    """
    GEOLOCATION_PATH.mkdir(exist_ok=True)
    try:
        if not COUNTRIES_FILE_SHP.exists():
            print('Downloading shp file')
            response: requests.Response = requests.get(COUNTRIES_SHP_LINK)
            with COUNTRIES_FILE_SHP.open('wb') as file:
                file.write(response.content)

        if not COUNTRIES_FILE_DBF.exists():
            print('Downloading DBF file')
            response: requests.Response = requests.get(COUNTRIES_DBF_LINK)
            with COUNTRIES_FILE_DBF.open('wb') as file:
                file.write(response.content)

    except requests.Timeout:
        print_warning('Cannot download files, geolocation not possible')
        exit(1)


def generate_random_coordinate(count: int, country: str) -> List[Tuple]:
    """
    Inspired by
    https://gis.stackexchange.com/questions/164005/getting-random-coordinates-based-on-country
    :param count:
    :param country:
    :param shp_location:
    :return:
    """
    logger.info(f'Gathering {count} random locations in {country}')

    # Retrieve
    get_countries_location_files()

    # reading shapefile with pyshp library
    shapes = shapefile.Reader(COUNTRIES_FILE_SHP)

    # getting feature(s) that match the country name
    country = [s for s in shapes.records() if country in s][0]

    # getting feature(s)'s id of that match
    country_id = int(re.findall(r'\d+', str(country))[0])

    shape_records = shapes.shapeRecords()
    feature = shape_records[country_id].shape.__geo_interface__

    shp_geom = shape(feature)

    minx, miny, maxx, maxy = shp_geom.bounds

    random_locations: List[Tuple] = []
    for i in range(count):
        while True:
            p = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
            if shp_geom.contains(p):
                random_locations.append((p.x, p.y))
                break

    return random_locations
