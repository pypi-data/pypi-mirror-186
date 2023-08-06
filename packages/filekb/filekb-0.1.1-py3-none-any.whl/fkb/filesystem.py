# fkb v0.1.1
# A knowledge base with file tracking and document note integration
# Copyright (C) 2023, ArktisDev
# See /LICENSE for licensing information

from pathlib import Path
from typing import List
import shutil
import os
import tempfile

def ListFiles(directory: str) -> List[str]:
    '''
    List all files contained in a directory recursively,
    similarly to the 'find' UNIX command
    Args:
    directory       - a string representing the target directory
    Returns:
    A list of strings representing the path of files contained
    in the directory
    '''
    dirpath = Path(directory)

    # Get list of files in the form: file1, dir1/file2, ...
    files = [str(f.relative_to(dirpath)) for f in dirpath.rglob('*') if f.is_file()]
    return files


def ListDirectories(directory: str) -> List[str]:
    '''
    List all sub-directories contained in a directory
    Args:
    directory       - a string representing the path to a directory
    Returns:
    A list of strings representing the path of directories contained
    in the provided directory
    '''
    dirpath = Path(directory)

    # Get list of files in the form: file1, dir1/file2, ...
    files = [str(f.relative_to(dirpath)) for f in dirpath.rglob('*') if f.is_dir()]
    return files


def TouchFile(filename: str) -> None:
    '''
    Creates a new empty file, in the style of the UNIX
    touch program.
    Arguments:
    filename    - a path to a filename
    '''
    Path(filename).touch()


def GetFileBasename(filename: str) -> str:
    '''
    Get basename for a file
    Arguments:
    filename    - a path to a filename
    Returns:
    The basename of the provided file
    '''
    return Path(filename).name


def CopyFile(source: str, dest: str) -> None:
    '''
    Copies a file to the provided destination
    Arguments:
    source    - the path to the source file to copy
    dest      - the destination path of the copy
    '''
    shutil.copy2(Path(source), Path(dest))


def RemoveFile(filename: str) -> None:
    '''
    Removes a file from the filesystem
    Arguments:
    filename    - the file to remove from the kb directory
    '''
    try:
        Path(filename).unlink()
    except FileNotFoundError:
        pass


def RemoveDirectory(directory: str) -> None:
    '''
    Removes a directory from the filesystem
    Arguments:
    directory    - the directory to remove from the kb system
    '''
    shutil.rmtree(directory)


def CreateDirectory(directory: str) -> None:
    '''
    Create a directory if it does not exist.
    Arguments:
    directory    - the directory path to be created
    '''
    os.makedirs(Path(directory), exist_ok=True)


def IsDirectory(path: str) -> bool:
    '''
    Checks if the provided path is a directory.
    Arguments:
    path        - the path to check
    Returns:
    A boolean, if true, the path corresponds to a directory
    '''
    return os.path.isdir(path)


def IsFile(path: str) -> bool:
    '''
    Checks if the provided path corresponds to a regular file.
    Arguments:
    path        - the path to check
    Returns:
    A boolean, if true, the path corresponds to a regular file
    '''
    return os.path.isfile(path)


def CountFiles(directory: str) -> int:
    '''
    Count the number of files in a directory
    Arguments:
    directory    - the directory where to count files
    Returns:
    the number of files contained in the directory
    '''
    return len(list(Path(directory).iterdir()))


def MoveFile(source: str, dest: str) -> None:
    '''
    Moves a file to the provided destination
    Arguments:
    source    - the path to the source file to copy
    dest      - the destination path of the copy
    '''
    shutil.move(source, dest)


def GetTempFilepath() -> str:
    '''
    Generates a temporary file path.
    Returns:
    A boolean, True if the file is of type text.
    '''
    tmpfilename = None
    while tmpfilename is None:
        random_tmp_path = str(Path(tempfile.gettempdir(),
                                   os.urandom(24).hex()))
        if not os.path.isfile(random_tmp_path):
            tmpfilename = random_tmp_path
    return tmpfilename


def IsTextFile(filename: str) -> bool:
    '''
    Determines if a file is textual (that can be
    nicely viewed in a text editor) or belonging
    to other types.
    Arguments:
    filename        - the file name/path to check
    Returns:
    A boolean, True if the file is of type text.
    '''
    txt_extensions = ('', '.conf', '.ini', '.txt',
                      '.md', '.rst', '.ascii', '.org', '.tex')

    file_ext = os.path.splitext(filename)[1]

    return file_ext in txt_extensions


def GetFilenamePartsWOPrefix(
        filename: str,
        prefix_to_remove: str) -> List[str]:
    '''
    Get filename parts without the provided prefix.
    E.g., if the filename is '/path/to/data/dir1/file2.txt'
    and the prefix to remove is '/path/to/data' then the
    returned will be a tuple containing ('dir1','file2.txt')
    Arguments:
    filename          - a string or path provided by pathlib
    prefix_to_remove  - a string or path provided by pathlib that
                        will be removed from the filename
    Returns:
    The provided filename without the provided prefix
    '''
    prefix_path = Path(prefix_to_remove)
    file_path = Path(filename)

    try:
        return file_path.relative_to(prefix_path).parts
    except ValueError:
        file_path.parts