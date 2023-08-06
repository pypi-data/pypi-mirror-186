import subprocess
import sys
from typing import List, Optional
import requests
from packaging.version import parse as parse_version
from pkg_resources import get_distribution
import json
import logging
import pkg_resources
from .install import install_package

def last_version(package: str):
    """Check if last version"""
    url = f'https://pypi.org/pypi/{package}/json'    
    req = requests.get(url)
    version = parse_version('0')
    if req.status_code == requests.codes.ok:
        j = json.loads(req.text.encode(req.encoding))
        releases = j.get('releases', [])
        for release in releases:
            ver = parse_version(release)
            if not ver.is_prerelease:
                version = max(version, ver)
    return version

def check_last(package: str) -> Optional[str]:
    pypi = last_version(package)
    current = parse_version(get_distribution(package).version)
    if pypi > current:
        return pypi


def check_last_masterdac(args: List[str]):
    better_version = check_last("master_dac")

    if better_version:
        logging.info("Updating the package")
        requirement, = pkg_resources.parse_requirements(f"master_dac=={better_version}")
        install_package(requirement)
        logging.info("Updating")
        subprocess.check_call(args)
        sys.exit()

        