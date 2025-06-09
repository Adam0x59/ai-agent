import unittest
from functions.get_files_info import *
from functions.get_files_content import *

class test_get_files_info(unittest.TestCase):
    '''
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
    
    def test_get_file_content(self):
        output = get_file_content("calculator", "lorem.txt")
        print(output)
    '''
    def test_get_file_content_main(self):
        output = get_file_content("calculator", "main.py")
        print(output)
    
    def test_get_file_content_pkg_calc(self):
        output = get_file_content("calculator", "pkg/calculator.py")
        print(output)
    
    def test_get_file_content_bin_cat(self):
        output = get_file_content("calculator", "/bin/cat")
        print(output)

if __name__ == '__main__':
    unittest.main(verbosity=2)