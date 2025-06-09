import unittest
from functions.get_files_info import *

class test_get_files_info(unittest.TestCase):
    def test_get_files_info_working_dir(self):
        output = get_files_info("calculator", ".")
        print(output)
    
    def test_get_files_info_pkg_dir(self):
        output = get_files_info("calculator", "pkg")
        print(output)

    def test_get_files_info_abso_bin(self):
        output = get_files_info("calculator", "/bin")
        print(output)

    def test_get_files_info_dot_dot(self):
        output = get_files_info("calculator", "../")
        print(output)


if __name__ == '__main__':
    unittest.main(verbosity=2)