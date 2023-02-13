import unittest
import pycodestyle


class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
        
     
     
     
     
        
# import pycodestyle

# fchecker = pycodestyle.Checker('testsuite/E27.py', show_source=True)
# file_errors = fchecker.check_all()

# print("Found %s errors (and warnings)" % file_errors)        