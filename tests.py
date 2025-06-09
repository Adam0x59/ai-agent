import unittest
from functions.get_files_info import *
from functions.get_files_content import *
from functions.write_file import *

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
    
    def test_get_file_content_main(self):
        output = get_file_content("calculator", "main.py")
        print(output)
    
    def test_get_file_content_pkg_calc(self):
        output = get_file_content("calculator", "pkg/calculator.py")
        print(output)
    
    def test_get_file_content_bin_cat(self):
        output = get_file_content("calculator", "/bin/cat")
        print(output)
    '''

    def test_write_file_lorem(self):
        output = write_file("calculator", "lorem.txt", "Wait, this isn't lorem ipsum")
        print(output)

    def test_write_file_pkg_morelorem(self):
        output = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(output)

    def test_write_file_tmp_temp(self):
        output = write_file("calculator", "/tmp/temp.text", "this should not be allowed")
        print(output)

if __name__ == '__main__':
    unittest.main(verbosity=2)