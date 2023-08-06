# -*- coding: utf-8 -*-

"""
VAERS DATA DOWNLOADER
~~~~~~~~~~~~~~~~

:copyright: © 2022 WWW Logic LLC
:license: MIT, see LICENSE for more details.
"""

from .metadata import (
    __author__,
    __copyright__,
    __email__,
    __license__,
    __maintainer__,
    __version__,
)

from vaers_downloader import download

__all__ = [
    '__author__', '__copyright__', '__email__', '__license__',
    '__maintainer__', '__version__', 'download',
]

if __name__ == "__main__":
  download.main()