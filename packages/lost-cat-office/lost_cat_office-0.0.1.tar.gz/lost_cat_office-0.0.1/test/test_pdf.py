"""A test case for the path utils module"""
import logging
import glob
import os
import sys
import unittest

from lost_cat_office.parsers.pdf_parser import PDFParser

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG
file_handler = logging.FileHandler(f"logs/test_ocr.log")
logger.addHandler(file_handler)

class TestPDF(unittest.TestCase):
    """A container class for the build path modeule test cases"""

    @classmethod
    def setUpClass(self):
        """ Set up for Trie Unit Tests..."""
        uri = os.path.join("data")
        if not os.path.exists(uri):
            os.makedirs(uri)
            logger.info("Creating %s", uri)
        self.files = []

        uri = os.path.join(uri, "*")
        for f in glob.glob(uri):
            _, ext = os.path.splitext(f)
            if ext.lower() in [".pdf"]:
                self.files.append(f)

    @classmethod
    def tearDownClass(self):
        """ Tear down for Trie Unit Tests"""
        pass

    def test_avail_config(self):
        """Check the available config is correct
        Expected:
            options str
            uritypes list str
            source [list]
                table
                key
                value list
        """
        config = PDFParser.avail_config()
        logger.info("Config: %s", config)

        self.assertIn("options", config, msg="Missing 'options'")
        self.assertIn("uritypes", config, msg="Missing 'uritypes'")
        self.assertIn("source", config, msg="Missing 'source'")

        # check tghe uritypes is pdf
        self.assertIn("file", config.get("uritypes",[]))

        source = config.get("source",[])
        self.assertGreater(len(source), 0, msg="Missing 'source' specs")

        self.assertEqual(source[0].get("table"), "URIMD", msg="Missing 'URIMD' table label")
        self.assertEqual(source[0].get("key"), "ext", msg="Missing 'ext' field label")
        self.assertIn(".pdf", source[0].get("values",[]), msg="Missing 'pdf' in selection")

    def test_availfunctions(self):
        """checks the class returns the relevant available fucntions"""
        pass

    def test_metadata(self):
        """Will load the contours for an image..."""
        for fidx, f in enumerate(self.files):
            logger.info("File: [%s] => %s", fidx, f)
            pdf = PDFParser(uri=f)

            # get the metadata directly
            md01 = pdf.get_metadata()

            # get the md via the avail functions
            fn = pdf.avail_functions().get("metadata")
            md02 = fn()

            self.assertDictEqual(md01, md02, msg="Function call is returning incorrect info")
            logger.info("Metadata: [%s] => %s", fidx, md01)

    def test_thumbnails(self):
        """Generate and compare the thumbanils"""
        for fidx, f in enumerate(self.files):
            logger.info("File: [%s] => %s", fidx, f)
            pdf = PDFParser(uri=f)

            # get the thumbnail
            fn = pdf.avail_functions().get("thumbnails")
            self.assertIsNotNone(fn, msg="Missing 'thumbnails' function")
            imgs = fn()
            self.assertEqual(len(imgs), 1, msg="Return incorrect number of 'thumbnails'")
            for iidx, img in enumerate(imgs):
                self.assertEqual(img.width, 300, msg="Width is not 300")
                self.assertEqual(img.height, 300, msg="Width is not 300")

            # now to get the full
            imgs = fn(first_page=False, size=100, use_aspect=True)
            self.assertGreaterEqual(len(imgs), 1, msg="Return incorrect number of 'thumbnails'")
            for iidx, img in enumerate(imgs):
                img.save(f"data\TNS{fidx}.{iidx}.png")
                self.assertEqual(img.width, 100, msg="Width is not 300")

    def test_screenshots(self):
        """Generate and compare the screenshots"""
        for fidx, f in enumerate(self.files):
            logger.info("File: [%s] => %s", fidx, f)
            pdf = PDFParser(uri=f)

            # get the thumbnail
            fn = pdf.avail_functions().get("screenshots")
            self.assertIsNotNone(fn, msg="Missing 'screenshots' function")
            imgs = fn()
            self.assertGreaterEqual(len(imgs), 1, msg="Return incorrect number of 'screenshots'")
            for iidx, img in enumerate(imgs):
                img.save(f"data\IMG{fidx}.{iidx}.png")
