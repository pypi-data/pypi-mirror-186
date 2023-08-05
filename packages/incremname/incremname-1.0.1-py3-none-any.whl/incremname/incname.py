""" incremname
    Version 1.0.1 (2023-01-15)
    Copyright (c) 2023 Evgenii Shirokov
    MIT License
"""

from os.path import exists, splitext


def incname(path, z_fill=2, sep_1=".", sep_2="", start=1):
    """Increment a file/folder name if it already exists."""

    def get_path():
        if i > start - 1:
            return f"{root}{sep_1}{str(i).zfill(z_fill)}{sep_2}{ext}"
        else:
            return path

    root, ext = splitext(path)
    i = start - 1
    while exists(inc_name := get_path()):
        i += 1
    return inc_name
