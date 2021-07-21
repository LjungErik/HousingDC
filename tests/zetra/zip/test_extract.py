"""
Test class for testing zip extractor
"""
from os import listdir, mkdir, rmdir
from os.path import isfile, join, exists
from shutil import rmtree

from zetra.zip.extract import ZipFileExtractor

def test_extract_zip_files():
    """
    Testing extracting files from zip file
    """
    output = "tmp-output/extracted-zips"
    if not exists(output):
        mkdir(output)

    ex = ZipFileExtractor()
    ex.extract_zip_files("tests/zetra/zip/test_zip.zip", output)
    files = [ f for f in listdir(output) if isfile(join(output, f)) ]
    assert "A.txt" in files
    assert "B.txt" in files
    assert "C.txt" in files

    rmtree(output)
