import os, os.path, time
from stat import * # ST_SIZE etc

import platform
import tarfile, zipfile

import binascii

#
class file_manager:
    """ Template model of Gaia """
    id = "file_manager";
    inventory = {};
    inventory_id = "";

    operation_options = ['int_to_hex', 'hex_to_int']

    def __init__(self, id):
        self.id = id;
        print("_gaia object [%s] is born\n" % self.id);

    def get_file_size(self, file_path):
        number_of_bytes = os.path.getsize(file_path)

        return number_of_bytes

    def get_file_owner_name(self, file_path):
        file_owner_name = ""

        try:
            st = os.stat(file_path)
        except IOError:
            print("failed to get information about", file_path)

        try:
            import pwd  # not available on all platforms
            userinfo = pwd.getpwuid(st[ST_UID])
        except (ImportError, KeyError):
            print("failed to get the owner name for", file_path)
        else:
            file_owner_name = userinfo[0]
            print("file owned by:", file_owner_name)

        return file_owner_name

    def get_file_creation_time(self, path_to_file):
        """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
        if platform.system() == 'Windows':
            return os.path.getctime(path_to_file)
        else:
            stat = os.stat(path_to_file)
            try:
                return stat.st_birthtime
            except AttributeError:
                # We're probably on Linux. No easy way to get creation dates here,
                # so we'll settle for when its content was last modified.
                return stat.st_mtime

    def get_file_activity_times(self, file_path):   # __file__
        time_created = time.ctime(self.get_file_creation_time(file_path))
        time_last_accessed = time.ctime(os.path.getatime(file_path))
        time_last_modified = time.ctime(os.path.getmtime(file_path))
        time_last_changed = time.ctime(os.path.getctime(file_path))

        return [time_created, time_last_accessed, time_last_modified, time_last_changed]

    def read_file_into_byte_array(self, path_to_file):
        in_file = open(path_to_file, "rb")
        file_in_byte_array = in_file.read() # opening for [r]eading as [b]inary. # if only to read 512 bytes, do .read(512)

        in_file.close()

        return file_in_byte_array

    def read_file_into_hex_string(self, path_to_file): # write byte arrays as a file
        file_in_byte_array = open(path_to_file, "rb").read()
        hex_string = binascii.hexlify(file_in_byte_array)

        return hex_string

    def write_byte_array_into_file (self, path_to_file, file_in_byte_array):
        with open(path_to_file, "wb") as out_file:  # open for [w]riting as [b]inary
            out_file.write(file_in_byte_array)

        out_file.close()

        return None

    def write_hex_string_into_file (self, path_to_file, hex_string):
        hex_string = hex_string.decode("utf-8")
        hex_string_byte_array = bytearray.fromhex(hex_string)   # to bytearray
        # print(hex_string_byte_array)

        with open(path_to_file, "wb") as out_file:  # open for [w]riting as [b]inary
            out_file.write(hex_string_byte_array)

        out_file.close()

        return None

    def read_file_into_string_buffer (self, path_to_file):
        file_handler = open(path_to_file, 'r')
        string_buffer = file_handler.read()
        file_handler.close()

        return string_buffer

    def write_string_buffer_into_file (self, path_to_file, string_buffer):
        file_handler = open(path_to_file, 'w')
        string_buffer = file_handler.write(string_buffer)
        file_handler.close()

        return None

    def get_common_path (self, paths):
        common_path = os.path.dirname(os.path.commonprefix(paths))

        return common_path

    def tar_files (self, files_with_paths, zip_file_name):
        tar_file = tarfile.open(zip_file_name, "w:gz") # to create a tar.bz2 compressed file, replace file extension name with ".tar.bz2" and "w:gz" with "w:bz2".

        for file_to_be_zipped in files_with_paths:
            tar_file.add(file_to_be_zipped)

        tar_file.close()

        return None

    """
    tar = tarfile.open("sample.tar.gz", "w:gz")
    
    for name in ["file1", "file2", "file3"]:
        tar.add(name)
    tar.close()
    """

    def zip_files (self, files_with_paths, zip_file_name):
        zip_in = zipfile.ZipFile(zip_file_name, 'w')

        for file_to_be_zipped in files_with_paths:
            zip_in.write(file_to_be_zipped, compress_type=zipfile.ZIP_DEFLATED)

        zip_in.close()

        return None

    def extract_zip_file (self, zip_extract_path, zip_file_name):
        zip_out = zipfile.ZipFile(zip_file_name)
        zip_out.extractall(zip_extract_path) # exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
        zip_out.close()
        return None

    def read_zip_file_list (self, zip_file_name):
        zip_out = zipfile.ZipFile(zip_file_name)
        zip_files_list = zip_out.namelist()

        number_of_files_in_zip = len(zip_files_list)
        file_size_unzipped_total, file_size_zipped_total = 0, 0

        for i in range(0, number_of_files_in_zip):
            zip_file_info = zip_out.getinfo(zip_files_list[i])
            file_size_unzipped_total = file_size_unzipped_total + zip_file_info.file_size
            file_size_zipped_total = file_size_zipped_total + zip_file_info.compress_size

        number_of_decimal_places = 5
        zip_files_compression_ratio = (round(file_size_unzipped_total / file_size_zipped_total, number_of_decimal_places)) # 'Compressed file is %sx smaller!' % zip_files_compression_ratio

        zip_out.close()
        return [zip_files_list, zip_files_compression_ratio]


    def who_am_i(self):  #
        """ Introspection """
        self.line_storage = [];

        print("My name is Gaia [" + self.id + "].")

        return

    def __del__(self):
        print("_gaia object [%s] removed\n" % self.id);


####################################
## main
####################################
if __name__ == "__main__":
    id_file_manager = "Library Agent: Internal Agent <file_manager>"
    print("=====[" + id_file_manager + " Start]===== \n")
    file_manager_object = file_manager(id_file_manager)
    file_manager_object.who_am_i()

    # import _Gaia._gaia
    # help(file_manager) # introspect

    print("=====[" + id_file_manager + " End]===== \n");

"""
# version: 2017-11-22_1434hr_19sec
"""
