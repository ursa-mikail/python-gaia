import os, stat

def is_user_readable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IRUSR)

def is_user_writeable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IWUSR)

def is_user_executable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IXUSR)

def is_group_readable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IRGRP)

def is_group_writeable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IWGRP)

def is_group_executable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IXGRP)

def is_others_readable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IROTH)

def is_others_writeable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IWOTH)

def is_others_executable(filepath):
	st = os.stat(filepath)
	return bool(st.st_mode & stat.S_IXOTH)

####################################
## main
####################################
if __name__ == "__main__":
    file_target = './data/logs_event/2018-04-24_1912hr_20sec.txt'

    user_rights = is_user_readable(file_target), is_user_writeable(file_target), is_user_executable(file_target)
    print("user_rights: ", user_rights)

    group_rights = is_group_readable(file_target), is_group_writeable(file_target), is_group_executable(file_target)
    print("group_rights: ", group_rights)

    others_rights = is_others_readable(file_target), is_others_writeable(file_target), is_others_executable(file_target)
    print("others_rights: ", others_rights)

    # os.chmod(file_target, stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH)
    os.chmod(file_target, stat.S_IWGRP | stat.S_IRGRP | stat.S_IRUSR | stat.S_IWUSR | stat.S_IWOTH | stat.S_IROTH)

    user_rights = is_user_readable(file_target), is_user_writeable(file_target), is_user_executable(file_target)
    print("user_rights: ", user_rights)

    group_rights = is_group_readable(file_target), is_group_writeable(file_target), is_group_executable(file_target)
    print("group_rights: ", group_rights)

    others_rights = is_others_readable(file_target), is_others_writeable(file_target), is_others_executable(file_target)
    print("others_rights: ", others_rights)

    file_status = "{0:b}".format(stat.S_IRUSR)
    file_status = "{0:b}".format(stat.S_IWUSR)
    file_status = "{0:b}".format(stat.S_IRUSR | stat.S_IWUSR)  # this is read and write for the user
    file_status = "{0:b}".format(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)

    print("file_status: ", file_status)

    """
    [data_type][owner][group][others]
    drwxrwxrwx 
       b     Block special file.
       c     Character special file.
       d     Directory.
       l     Symbolic link.
       s     Socket link.
       p     FIFO.
       -     Regular file.
       
       
       # os.access(r'C:\donthaveaccess', os.R_OK) # os.access() with flags os.R_OK, os.W_OK, and os.X_OK

import tempfile

def can_create_file(folder_path):
    try:
        tempfile.TemporaryFile(dir=folder_path)
        return True
    except OSError:
        return False

def can_create_folder(folder_path):
    try:
        name = tempfile.mkdtemp(dir=folder_path)
        os.rmdir(name)
        return True
    except OSError:
        return False


st = os.stat('C:\foo')
mode = st[stat.ST_MODE]
mode & stat.S_IWRITE == True 

os.chmod('manage.py', 0o666)
os.chmod(filename, 0o644) 
stat.S_IRUSR  # this means user read permissions

# 666
os.chmod('manage.py', stat.S_IWGRP | stat.S_IRGRP | stat.S_IRUSR | stat.S_IWUSR | stat.S_IWOTH | stat.S_IROTH)

    """