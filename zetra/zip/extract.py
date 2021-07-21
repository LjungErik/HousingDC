"""
Extractor for extracting the content from a zip file.
Requirements:
 * Efficent unzipping without using a lot of memory.
 * Efficent way for reading the zipped files.
 * Allow streaming of files to prevent memory overflow.
 * Allow special settings to extract a line from a file at a time
   without using too much memory.
"""
import logging

logger = logging.getLogger(__name__)

import zipfile

# solutions:
# save zip file to a tmp directory locally
# utilize zipfile tool in python
# extract file to a tmp directory
# Stream through each of the relevant files
# Allow the ability to take a line from the file at a time
_FILENAME_OFFSET = 30

class ZipFileExtractor():
    """
    Extractor for pulling out files from zip folder efficiently
    """

    #pylint: disable=no-self-use
    def extract_zip_files(self, zip_file, output_dir):
        """
        Extract all files from a zip folder into output dir
        """
        with open(zip_file, 'rb') as src:
            with  zipfile.ZipFile(src) as zf:
                logger.debug(f"Unzipping file: {zip_file} to directory {output_dir}")
                for m in zf.infolist():
                    logger.debug(f"Zipped document: {m.filename}")
                    logger.debug(f"Zipped header offset: {m.header_offset}")
                    logger.debug(f"Zipped compress size: {m.compress_size}")
                    logger.debug(f"Zipped file size: {m.file_size}")

                    zf.extract(m, path=output_dir)
