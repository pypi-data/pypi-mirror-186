"""
Release pull and check for local files control module
"""
import json
import logging
import time
from typing import List, Dict, Optional
from pathlib import Path

import rich
from rich.progress import track
from rich.table import Table
from rich.console import Console
import requests
from pydantic import BaseModel

from nuvla_cli.common.constants import RELEASES_PATH, RELEASES_LINK, RELEASE_DOWNLOAD_LINK
from nuvla_cli.common.common import print_warning, print_success


class ReleaseSchema(BaseModel):
    version: str
    downloaded: bool
    downloaded_components: List[str] = []
    downloadable_assets: List[str] = []
    prerelease: str = 'False'


class Release(str):
    major: int
    medium: int
    minor: int

    def __new__(cls, value, *args, **kwargs):
        versions: List[int] = [int(i) for i in value.split('.')]
        if len(versions) != 3:
            raise ValueError(f'Version provided {value} does not correspond with '
                             f'NuvlaEge format X.X.X )')
        cls.major = versions[0]
        cls.medium = versions[1]
        cls.minor = versions[2]
        return super(Release, cls).__new__(cls, value)


class ReleaseControl:
    """
    NuvlaEdge Release control class
    """
    releases: Dict[str, ReleaseSchema] = {}

    def __init__(self):
        self.logger: logging.Logger = logging.getLogger(self.__class__.__name__)

        # 1. Silently gather local downloads (If any)
        self.gather_local_downloads()
        self.gather_remote_releases()

    def gather_remote_releases(self):
        """
        Retrieves the available releases for NuvlaEdge and composes its download links
        """
        available_releases: requests.Response = requests.get(RELEASES_LINK)

        for release in available_releases.json():

            it_assets: List = [i.get('name') for i in release.get('assets')
                               if i.get('name').endswith('.yml')]
            it_tag: str = release.get('tag_name')
            self.releases[release.get('tag_name')] = ReleaseSchema(
                version=it_tag,
                downloadable_assets=it_assets,
                downloaded=False,
                prerelease=release.get('prerelease')
            )

    def download_release(self, version: str) -> Optional[Path]:
        """
        Downloads the provided release and saves it into the local nuvla-cli folder
        TODO: add provide file option
        :param version: Version to be downloaded
        :return: The path of the location of the files
        """
        req_release: ReleaseSchema = self.releases.get(version)
        if not req_release:
            print_warning(f'Requested engine version {version} is not among the available'
                          f' releases')
            return None

        print('Starting download')
        for file_name in track(req_release.downloadable_assets,
                               description=f'Downloading files for version: {version}'):
            it_link: str = RELEASE_DOWNLOAD_LINK.format(version=req_release.version,
                                                        file=file_name)
            release_location = RELEASES_PATH / version
            release_location.mkdir(exist_ok=True)
            it_file = release_location / file_name

            req_release.downloaded_components.append(file_name)
            if it_file.exists():
                continue

            response: requests.Response = requests.get(it_link, timeout=5)
            with it_file.open('w') as file:
                file.write(response.content.decode('UTF-8'))
        return RELEASES_PATH / version

    def gather_local_downloads(self):
        """
        Retrieves the local downloaded releases
        :return: None
        """
        if not RELEASES_PATH.exists():
            self.logger.error('Local path empty, no downloaded engine releases')
            RELEASES_PATH.mkdir(exist_ok=True)
            return

        for release in RELEASES_PATH.glob('*'):
            self.releases[release.name] = ReleaseSchema(
                version=release.name,
                downloaded=True
            )

    def list(self) -> List[str]:
        """
        Pretty prints a list of available engine releases and prereleases
        :return: None
        """
        release_table: Table = Table("Index", "Version", "Pre-Release")
        version_list: List[str] = sorted(self.releases, reverse=True)
        for i, release in enumerate(version_list):
            it_release: ReleaseSchema = self.releases.get(release)
            release_table.add_row(str(i+1), release, it_release.prerelease)

        console: Console = Console()
        console.print(release_table)
        return version_list

