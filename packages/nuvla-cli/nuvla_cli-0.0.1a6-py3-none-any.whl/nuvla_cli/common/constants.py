from pathlib import Path

# Local files handling
LOCAL_PATH: Path = Path('~/.nuvla/').expanduser()

# Release handling
RELEASES_PATH: Path = LOCAL_PATH / 'releases'
RELEASES_LINK: str = 'https://api.github.com/repos/nuvlaedge/deployment/releases'
RELEASE_DOWNLOAD_LINK: str = 'https://github.com/nuvlaedge/deployment/releases/' \
                             'download/{version}/{file}'


# GeoLocation Handling
GEOLOCATION_PATH: Path = LOCAL_PATH / 'geo_location'

# continents
CONTINENTS_FILE: Path = GEOLOCATION_PATH / 'World_Continents.{format}'
CONTINENTS_DBF_LINK: str = 'https://github.com/nuvla/cli/raw/main/data/geo/' \
                           'World_Continents.dbf'
CONTINENTS_SHP_LINK: str = 'https://github.com/nuvla/cli/raw/main/data/geo/' \
                           'World_Continents.shp'

# countries
COUNTRIES_FILE_DBF: Path = GEOLOCATION_PATH / 'World_Countries.dbf'
COUNTRIES_FILE_SHP: Path = GEOLOCATION_PATH / 'World_Countries.shp'
DBF_MD5_SUM: str = '2cbdd25f1f93c788909023686acfd90e'
COUNTRIES_DBF_LINK: str = 'https://raw.githubusercontent.com/nuvla/cli/main/data/geo/' \
                          'World_Countries.dbf'

SHP_MD5_SUM: str = '340e6fba7d3595b2147ac318d3c2215e'
COUNTRIES_SHP_LINK: str = 'https://raw.githubusercontent.com/nuvla/cli/main/data/geo/' \
                          'World_Countries.shp'


