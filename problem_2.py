import os

def find_files_helper(suffix, path, file_list):
    if suffix == "" or path == "":
        return
    
    if not os.path.isdir(path):
        if path.endswith(suffix):
            file_list.append(path)
            return file_list
        return
    
    for file in os.listdir(path):
        find_files_helper(suffix, os.path.join(path, file), file_list)

    return file_list

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    file_list = []
    return find_files_helper(suffix, path, file_list)

print(find_files(".py", os.getcwd()))
print(find_files("", os.getcwd())) #should return None because suffix is empty
print(find_files(".jpg", "/Users/manavale/Documents"))
print(find_files(".py", "C:/path/does/not/exist")) #should return None because path doesn't exist
print(find_files(".py", "./solution/problem2/problem2.py"))
