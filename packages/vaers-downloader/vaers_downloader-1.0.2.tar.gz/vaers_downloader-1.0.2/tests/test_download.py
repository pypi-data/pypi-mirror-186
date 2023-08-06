# WWW Logic Software Testing
 
import os
import shutil

import unittest

from vaers_downloader import download

tempDir = '/tmp'


class TestDownload(unittest.TestCase):
    def test_download(self):
        download.downloadVAERSdata(years=[], directory=tempDir)
        self.assertTrue(os.path.exists(os.path.join(tempDir, 'VAERS', 'NonDomesticVAERSDATA.csv')))
        self.assertTrue(os.path.exists(os.path.join(tempDir, 'VAERS', 'NonDomesticVAERSSYMPTOMS.csv')))
        self.assertTrue(os.path.exists(os.path.join(tempDir, 'VAERS', 'NonDomesticVAERSVAX.csv')))
        shutil.rmtree(os.path.join(tempDir, 'VAERS'), ignore_errors=True)

if __name__ == "__main__":
    unittest.main()
