# I have used recurssion to solve this problem.
# 1. Iterate over the list of files in current path.
# 2. Save the item to list if it satisfies the criteria.
# 3. If any of the path is a sub-directory, repeat step 1 with the path.
# 4. Append all the paths found from Step 3 to the current list.
#
# The number of times we have to iterate is equal to total number of files
# and sub-directories present inside a directory and all of its sub-directories.
# The time complexity is O(n), where n is the total number files + sub-directories
# at all levels inside a directory.

import os


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

    paths = []

    for file_path in os.listdir(path):
        # Creat the full path of file
        full_file_path = os.path.join(path, file_path)

        # If the file path is a directory
        if os.path.isdir(full_file_path):

            # Recursively find for more files in sub directories
            sub_paths = find_files(suffix, full_file_path)

            # Append the found files to current list
            paths.extend(sub_paths)

        elif os.path.isfile(file_path) and file_path.endswith(suffix):
            # File satisfies the siffux criteria, append it to the list
            paths.append(full_file_path)

    return paths


for file_path in find_files(".c", "./testdir"):
    print(file_path)
