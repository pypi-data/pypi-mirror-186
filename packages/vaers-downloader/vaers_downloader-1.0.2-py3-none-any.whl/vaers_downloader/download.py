import os
import sys
from datetime import date

import argparse

from .VAERSFileDownloader import updateVAERSFiles


def downloadVAERSdata(years, directory = os.getcwd()):
  """
  from datetime import date
  downloadVAERSdata(years=getYears(start=2019, end=date.today().year))
  """
  updateVAERSFiles(
    years = years,
    workingDirectory = directory)


def getYears(start=2019, end=date.today().year):
  return [i for i in range(start, end + 1)]

def main(argv):
  parser = argparse.ArgumentParser(
    add_help=False, description=('Download VAERS Data')
  )
  parser.add_argument(
    '--help', '-h', action='help', default=argparse.SUPPRESS, help='Show this help message and exit'
  )
  parser.add_argument(
    '--start', '-s', help='Start year', type=int, default=date.today().year
  )
  parser.add_argument(
    '--end', '-e', help='End year', type=int,default=date.today().year
  )
  parser.add_argument(
    '--directory', '-d', help='Directory where to download VAERS data', default=os.getcwd()
  )

  args = parser.parse_args(argv)
  start = args.start
  end = args.end
  directory = args.directory
  
  downloadVAERSdata(
    years=getYears(
      start=start,
      end=end,
    ),
    directory=directory,
  )
