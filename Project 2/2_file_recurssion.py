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
